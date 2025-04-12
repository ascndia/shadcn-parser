from dataclasses import dataclass
from typing import Dict, Set, Optional

@dataclass
class Variant:
    name: str
    classes: Set[str]
    props: Dict[str, str] = None

@dataclass
class Component:
    name: str
    tag: str
    base_classes: Set[str]
    variants: Dict[str, Variant] = None
    default_variant: Optional[str] = None
    ignore_attrs: Set[str] = None  
    self_closing: bool = False  


    def match(self, tag_name: str, element_classes: Set[str]) -> bool:
        return (
            tag_name == self.tag and 
            self.base_classes.issubset(element_classes)
        )
    
    def extract_variant(self, element_classes: Set[str]) -> Optional[Variant]:
        if not self.variants:
            return None
            
        for variant in self.variants.values():
            if variant.classes.issubset(element_classes):
                return variant
        return None
    
    def get_extra_classes(self, element_classes: Set[str], variant: Optional[Variant]) -> Set[str]:
        base_and_variant = self.base_classes.copy()
        if variant:
            base_and_variant.update(variant.classes)
        return element_classes - base_and_variant

class ComponentAdapter:
    @classmethod
    def from_cva(
        cls, 
        name: str, 
        tag: str, 
        cva_config: dict, 
        ignore_attrs: Set[str] = None,
        self_closing: bool = False):

        base_classes_str = cva_config.get("base_classes", "")
        base_classes = set(base_classes_str.split()) if isinstance(base_classes_str, str) else set()
        
        # Process variants
        variants = {}
        for var_type, var_options in cva_config.get("variants", {}).items():
            variants[var_type] = {}
            for var_name, var_classes in var_options.items():
                # Ensure var_classes is a string before splitting
                if isinstance(var_classes, str):
                    variants[var_type][var_name] = Variant(
                        name=var_name,
                        classes=set(var_classes.split())
                    )
                else:
                    # Handle the case where var_classes might not be a string
                    variants[var_type][var_name] = Variant(
                        name=var_name,
                        classes=set(str(var_classes).split()) if var_classes else set()
                    )
        
        # Get the default variant if specified
        default_variant = cva_config.get("default_variant")
        
        # Return Component instance instead of trying to construct a ComponentAdapter
        return Component(
            name=name,
            tag=tag,
            base_classes=base_classes,
            variants=variants,
            default_variant=default_variant,
            ignore_attrs=ignore_attrs or set(),
            self_closing=self_closing
        )

    @classmethod    
    def from_base(
        cls, 
        name: str, 
        tag: str, 
        base_classes: str, 
        ignore_attrs: Set[str] = None,
        self_closing: bool = False
    ) -> Component:
        return Component(
            name=name,
            tag=tag,
            base_classes=set(base_classes.split()),
            variants={},
            ignore_attrs=ignore_attrs or set(),
            self_closing=self_closing
        )
        