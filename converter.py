from bs4 import BeautifulSoup, Tag, Doctype
from components import Component, Variant, ComponentAdapter
from typing import Dict, Tuple, Optional

class JSXConverter:
    SELF_CLOSING_TAGS = {
        "img", "input", "br", "hr", "meta", "link",
        "area", "base", "col", "embed", "param",
        "source", "track", "wbr"
    }

    def __init__(self, components: Dict[str, Component]):
        self.components = components
        
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
            
        # Component matching logic
        component, variant = self._find_matching_component(el)
        
        if component:
            return self._render_component(el, component, variant, indent_level)
            
        return self._render_html_element(el, indent_level)
    
    def _find_matching_component(self, el: Tag):
        element_classes = set(el.get("class", []))
        
        for component in self.components.values():
            if el.name != component.tag:
                continue
                
            if not component.base_classes.issubset(element_classes):
                continue

            detected_variants = {}
            
            # Check all variant types (variant, size)
            for variant_type, variants in component.variants.items():
                for var_name, variant_obj in variants.items():
                    if variant_obj.classes.issubset(element_classes):
                        detected_variants[variant_type] = var_name
                        break  # Only match one variant per type

            return component, detected_variants
            
        return None, None

    def _render_component(self, el: Tag, component: Component, variant: Variant, indent_level: int) -> str:
        # Build attributes FIRST
        attrs = self._build_component_attrs(el, component, variant)
        attrs_str = " ".join(attrs)
        if attrs_str:
            attrs_str = " " + attrs_str  # Add leading space

        indent = "  " * indent_level

        # Handle self-closing components early
        if component.self_closing:
            return f"{indent}<{component.name}{attrs_str} />"

        # Process children only for non-self-closing components
        children = [self.process_element(child, indent_level + 1) for child in el.contents]
        children_str = "\n".join(filter(None, children))

        # Format output based on children content
        if not children_str.strip():
            return f"{indent}<{component.name}{attrs_str} />"
            
        return (
            f"{indent}<{component.name}{attrs_str}>\n"
            f"{children_str}\n"
            f"{indent}</{component.name}>"
        )
    
    def _build_component_attrs(self, el: Tag, component: Component, variants: dict) -> list:
        attrs = []
        el_classes = set(el.get("class", []))
        
        # Add variant props
        for var_type, var_name in variants.items():
            attrs.append(f'{var_type}="{var_name}"')
        
        # Calculate extra classes (base + variants)
        all_component_classes = component.base_classes.copy()
        for var_obj in component.variants.values():
            for v in var_obj.values():
                all_component_classes.update(v.classes)
        
        extra_classes = el_classes - all_component_classes
        if extra_classes:
            preserved_classes = [c for c in el["class"] if c in extra_classes]
            attrs.append(f'className="{" ".join(preserved_classes)}"')
        
        # Other attributes
        for attr, value in el.attrs.items():
                if attr == "class":
                    continue
                if attr in component.ignore_attrs:
                    continue
                attrs.append(f'{attr}="{value}"')
        
        return attrs
        
    def _render_html_element(self, el: Tag, indent_level: int) -> str:
        # Similar structure to component rendering but simpler
        indent = "  " * indent_level
        attrs = [f'className="{" ".join(el["class"])}"'] if "class" in el.attrs else []
        
        for attr, value in el.attrs.items():
            if attr != "class":
                attrs.append(f'{attr}="{value}"')
                
        children = [self.process_element(child, indent_level + 1) 
                   for child in el.contents]
        children_str = "\n".join(filter(None, children))
        
        if not children_str and el.name in self.SELF_CLOSING_TAGS:
            return f"{indent}<{el.name} {' '.join(attrs)} />"
            
        return (
            f"{indent}<{el.name} {' '.join(attrs)}>\n"
            f"{children_str}\n"
            f"{indent}</{el.name}>"
        )
    
    def _format_text(self, text: str, indent_level: int) -> str:
        if not text:
            return ""
        return "  " * indent_level + text
