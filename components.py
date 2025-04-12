from dataclasses import dataclass, field
from typing import Dict, Set, Optional, List
from tailwind_merge import TailwindMerge

@dataclass
class Component:
    name: str
    tag: str
    core_classes: Set[str]  # Immutable fingerprint classes
    variant_map: Dict[str, Dict[str, Set[str]]]  # {variant_type: {variant_name: classes}}
    style_classes: Set[str]  # Default styles that can be customized
    default_variants: Dict[str, str] = field(default_factory=dict)  # {variant_type: default_name}
    ignore_attrs: Set[str] = field(default_factory=set)
    self_closing: bool = False
    config: Dict = field(default_factory=lambda: {
        'self_closing': False,
        'ignore_children': False,
        'preserve_aspect': True,
        'ignore_classes': set(),
    })
    tw_merger: TailwindMerge = field(init=False, repr=False)

    def __post_init__(self):
        self.tw_merger = TailwindMerge()

    def match_core(self, tag_name: str, element_classes: Set[str]) -> bool:
        """Check if element matches component's core identity"""
        return (
            tag_name == self.tag and
            self.core_classes.issubset(element_classes))
    
    def detect_variants(self, element_classes: Set[str]) -> Dict[str, str]:
        """Identify active variants based on class matches"""
        detected = {}
        for var_type, variants in self.variant_map.items():
            for var_name, var_classes in variants.items():
                if var_classes.issubset(element_classes):
                    detected[var_type] = var_name
                    break  # First match wins
            else:  # No variant matched, use default
                if var_type in self.default_variants:
                    detected[var_type] = self.default_variants[var_type]
        return detected
    
    def get_custom_classes(self, element_classes: Set[str]) -> str:
        """Get merged custom classes after removing component-managed ones"""
        managed_classes = self.core_classes.copy()
        managed_classes.update(self.style_classes)
        
        # Add variant classes to managed set
        for var_type, variants in self.variant_map.items():
            for var_classes in variants.values():
                managed_classes.update(var_classes)
        
        custom_classes = element_classes - managed_classes
        return self.tw_merger.merge(" ".join(custom_classes))

class ComponentAdapter:
    @classmethod
    def from_fingerprint(
        cls,
        name: str,
        tag: str,
        core_classes: Set[str],
        variant_map: Dict[str, Dict[str, Set[str]]],
        style_classes: Set[str],
        default_variants: Dict[str, str] = None,
        ignore_attrs: Set[str] = None,
        self_closing: bool = False
    ) -> Component:
        return Component(
            name=name,
            tag=tag,
            core_classes=core_classes,
            variant_map=variant_map,
            style_classes=style_classes,
            default_variants=default_variants or {},
            ignore_attrs=ignore_attrs or set(),
            self_closing=self_closing
        )

        