from dataclasses import dataclass, field
from typing import Dict, Set, Optional, Any
from tailwind_merge import TailwindMerge

@dataclass
class Component:
    name: str
    tag: str
    match_pattern: Dict[str, Any] = field(default_factory=lambda: {
        'signature_classes': set(),
        'data_attributes': dict(),
        'variant_patterns': dict(),
        'style_classes': set()
    })
    config: Dict = field(default_factory=lambda: {
        'self_closing': False,
        'ignore_children': False,
        'output_blacklist': set(),
        'default_variants': dict(),
        'skip_this_element': False,
    })
    tw_merger: TailwindMerge = field(init=False, repr=False)

    def __post_init__(self):
        self.tw_merger = TailwindMerge()

    def match_core(self, tag_name: str, element_classes: Set[str]) -> bool:
        """Check if element matches component's core identity"""
        return (
            tag_name == self.tag and
            self.match_pattern['signature_classes'].issubset(element_classes)
        )

    def detect_variants(self, element_classes: Set[str]) -> Dict[str, str]:
        """Identify active variants with fallback to defaults"""
        detected = {}
        for var_type, variants in self.match_pattern['variant_patterns'].items():
            # Check existing variants
            variant_found = False
            for var_name, var_classes in variants.items():
                if var_classes.issubset(element_classes):
                    detected[var_type] = var_name
                    variant_found = True
                    break
            
            # Fallback to default variant
            if not variant_found:
                default_var = self.config['default_variants'].get(var_type)
                if default_var:
                    detected[var_type] = default_var
        return detected

    def get_custom_classes(self, element_classes: Set[str]) -> str:
        """Get merged custom classes after removing component-managed ones"""
        managed_classes = self.match_pattern['signature_classes'].copy()
        managed_classes.update(self.match_pattern['style_classes'])
        
        # Add all possible variant classes
        for var_type in self.match_pattern['variant_patterns']:
            for var_classes in self.match_pattern['variant_patterns'][var_type].values():
                managed_classes.update(var_classes)
        
        custom_classes = element_classes - managed_classes
        return self.tw_merger.merge(" ".join(custom_classes))