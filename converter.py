from bs4 import BeautifulSoup, Tag, Doctype
from components import Component
from typing import Dict, Tuple, Optional, Set
from tailwind_merge import TailwindMerge

class JSXConverter:
    SELF_CLOSING_TAGS = {
        "img", "input", "br", "hr", "meta", "link",
        "area", "base", "col", "embed", "param",
        "source", "track", "wbr"
    }

    def __init__(self, components: Dict[str, Component]):
        self.components = components
        self.tw_merger = TailwindMerge()

    def convert(self, html: str) -> str:
        soup = BeautifulSoup(html, "html.parser")
        output = []
        
        for element in soup.contents:
            processed = self.process_element(element)
            if processed:
                output.append(processed)
                
        return "\n".join(output)

    def process_element(self, el, indent_level=0) -> str:
        if isinstance(el, Doctype):
            return "<!DOCTYPE html>"
            
        if not isinstance(el, Tag):
            return self._format_text(str(el).strip(), indent_level)
            
        component, variants = self._find_matching_component(el)
        if component:
            return self._render_component(el, component, variants, indent_level)
            
        return self._render_html_element(el, indent_level)
    
    def _find_matching_component(self, el: Tag) -> Tuple[Optional[Component], dict]:
        el_classes = set(el.get("class", []))
        el_attrs = el.attrs

        for component in self.components.values():
            
            if el.name != component.tag:
                continue

            
            data_match = all(
                el_attrs.get(attr) == str(value)
                for attr, value in component.match_pattern['data_attributes'].items()
            )
            if not data_match:
                continue

            
            if not component.match_pattern['signature_classes'].issubset(el_classes):
                continue

            
            detected_variants = {}
            for var_type, variants in component.match_pattern['variant_patterns'].items():
                for var_name, var_classes in variants.items():
                    if var_classes.issubset(el_classes):
                        detected_variants[var_type] = var_name
                        break

            return component, detected_variants

        return None, {}
    

    def _render_component(self, el: Tag, component: Component, variants: dict, indent_level: int) -> str:
        
        if component.config.get('skip_this_element'):
            children = []
            for child in el.contents:
                # Process children at CURRENT indent level (no nesting increase)
                processed = self.process_element(child, indent_level)
                if processed:
                    children.append(processed)
            return "\n".join(children)
        
        attrs = self._build_component_attrs(el, component, variants)
        attrs_str = " ".join(attrs)
        indent = "  " * indent_level

        if component.config.get('self_closing') or component.config.get('ignore_children'):
            return f"{indent}<{component.name}{' ' + attrs_str if attrs_str else ''} />"
    
        children = [self.process_element(child, indent_level + 1) for child in el.contents]
        children_str = "\n".join(filter(None, children))

        if not children_str.strip():
            return f"{indent}<{component.name}{' ' + attrs_str if attrs_str else ''} />"
            
        return (
            f"{indent}<{component.name}{' ' + attrs_str if attrs_str else ''}>\n"
            f"{children_str}\n"
            f"{indent}</{component.name}>"
        )
    

    def _build_component_attrs(self, el: Tag, component: Component, variants: dict) -> list:
        attrs = []
        el_classes = set(el.get("class", []))
        
        managed_classes = (
            component.match_pattern['signature_classes'] |
            component.match_pattern['style_classes']
        )
        for var_classes in component.match_pattern['variant_patterns'].values():
            managed_classes.update({c for v in var_classes.values() for c in v})

        custom_classes = el_classes - managed_classes
        if custom_classes:
            merged = self.tw_merger.merge(" ".join(custom_classes))
            attrs.append(f'className="{merged}"')

        for var_type, var_name in variants.items():
            attrs.append(f'{var_type}="{var_name}"')

        for attr, value in el.attrs.items():
            if attr in component.config['output_blacklist']:
                continue
            if attr == "class":
                continue
            attrs.append(f'{attr}="{value}"')

        return attrs

    def _render_html_element(self, el: Tag, indent_level: int) -> str:
        indent = "  " * indent_level
        attrs = []
        
        if "class" in el.attrs:
            merged = self.tw_merger.merge(" ".join(el["class"]))
            attrs.append(f'className="{merged}"')

        for attr, value in el.attrs.items():
            if attr != "class":
                attrs.append(f'{attr}="{value}"')

        children = [self.process_element(child, indent_level + 1) for child in el.contents]
        children_str = "\n".join(filter(None, children))

        if not children_str and el.name in self.SELF_CLOSING_TAGS:
            return f"{indent}<{el.name}{' ' + ' '.join(attrs) if attrs else ''} />"
            
        return (
            f"{indent}<{el.name}{' ' + ' '.join(attrs) if attrs else ''}>\n"
            f"{children_str}\n"
            f"{indent}</{el.name}>"
        )

    def _format_text(self, text: str, indent_level: int) -> str:
        return "  " * indent_level + text if text.strip() else ""