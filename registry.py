from components import Component
from typing import Dict, Tuple, Optional
from tailwind_merge import TailwindMerge

COMPONENTS = {
        "Button": Component(
            name="Button",
            tag="button",
            match_pattern={
                'signature_classes': {
                    # Immutable identity classes (never customized)
                    "ring-offset-background",
                    "focus-visible:outline-none", "focus-visible:ring-2",
                    "disabled:pointer-events-none", "disabled:opacity-50",
                    "[&_svg]:pointer-events-none", "[&_svg]:size-4",
                    "focus-visible:ring-ring",
                    "focus-visible:ring-offset-2", "[&_svg]:shrink-0",
                },
                'data_attributes': {},
                'variant_patterns': {
                    "variant": {
                        "default": {"bg-primary", "text-primary-foreground", "hover:bg-primary/90"},
                        "destructive": {"bg-destructive", "text-destructive-foreground", "hover:bg-destructive/90"},
                        "outline": {"border", "border-input", "bg-background", "hover:bg-accent", "hover:text-accent-foreground"},
                        "secondary": {"bg-secondary", "text-secondary-foreground", "hover:bg-secondary/80"},
                        "ghost": {"hover:bg-accent", "hover:text-accent-foreground"},
                        "link": {"text-primary", "underline-offset-4", "hover:underline"}
                    },
                    "size": {
                        "default": {"h-10", "px-4", "py-2"},
                        "sm": {"h-9", "px-3"},
                        "lg": {"h-11", "px-8"},
                        "icon": {"h-10", "w-10"}
                    }
                },
                'style_classes': {
                    # Default styles that can be customized/overridden
                    "rounded-md", "text-sm", "font-medium",
                    "gap-2", "whitespace-nowrap", "transition-colors",
                    "inline-flex", "items-center", "justify-center",
                }
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': set()
            }
        ),
        "Badge": Component(
            name="Badge",
            tag="span",
            match_pattern={
                'signature_classes': {
                    "transition-[color,box-shadow]",
                    "focus-visible:ring-[3px]",
                    "focus-visible:border-ring", "focus-visible:ring-ring/50",
                    "aria-invalid:ring-destructive/20", "aria-invalid:border-destructive",
                    "dark:aria-invalid:ring-destructive/40",
                    "[&>svg]:pointer-events-none", "[&>svg]:size-3",
                },
                'data_attributes': {
                    "data-slot": "badge"
                },
                'variant_patterns': {
                    "variant": {
                        "default": {
                            "border-transparent", "bg-primary", "text-primary-foreground",
                            "[a&]:hover:bg-primary/90"
                        },
                        "secondary": {
                            "border-transparent", "bg-secondary", "text-secondary-foreground",
                            "[a&]:hover:bg-secondary/90"
                        },
                        "destructive": {
                            "border-transparent", "bg-destructive", "text-white",
                            "[a&]:hover:bg-destructive/90",
                            "focus-visible:ring-destructive/20",
                            "dark:focus-visible:ring-destructive/40",
                            "dark:bg-destructive/60"
                        },
                        "outline": {
                            "text-foreground", "[a&]:hover:bg-accent",
                            "[a&]:hover:text-accent-foreground"
                        },
                    }
                },
                'style_classes': {
                    "w-fit", "shrink-0", "overflow-hidden",
                    "inline-flex", "items-center", "justify-center", "gap-1",
                    "rounded-md", "border", "px-2", "py-0.5",
                    "text-xs", "font-medium", "whitespace-nowrap"
                }
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': {"data-slot"}
            }
        ),
        "Separator": Component(
            name="Separator",
            tag="div",  # Radix `SeparatorPrimitive.Root` renders a div by default
            match_pattern={
                'signature_classes': {
                    "shrink-0",
                    "bg-border",
                },
                'data_attributes': {
                    "data-slot": "separator-root",
                },
                'variant_patterns': {
                    "orientation": {
                        "horizontal": {
                            "data-[orientation=horizontal]:h-px",
                            "data-[orientation=horizontal]:w-full",
                        },
                        "vertical": {
                            "data-[orientation=vertical]:w-px",
                            "data-[orientation=vertical]:h-full",
                        },
                    }
                },
                'style_classes': set() 
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': {"role", "data-orientation", "data-slot"}
            },
        ),
        "Card": Component(
            name="Card",
            tag="div",
            match_pattern={
                'signature_classes': {
                    "rounded-xl", "border", "bg-card", "text-card-foreground", "shadow"
                },
                'data_attributes': {},
                'variant_patterns': {},  # No dynamic variants
                'style_classes': set()
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': set()
            }
        ),
        "CardHeader": Component(
            name="CardHeader",
            tag="div",
            match_pattern={
                'signature_classes': {
                    "flex", "flex-col", "space-y-1.5", "p-6"
                },
                'data_attributes': {},
                'variant_patterns': {},
                'style_classes': set()
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': set()
            }
        ),
        "CardTitle": Component(
            name="CardTitle",
            tag="div",
            match_pattern={
                'signature_classes': {
                    "font-semibold", "leading-none", "tracking-tight"
                },
                'data_attributes': {},
                'variant_patterns': {},
                'style_classes': set()
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': set()
            }
        ),
        "CardDescription": Component(
            name="CardDescription",
            tag="div",
            match_pattern={
                'signature_classes': {
                    "text-sm", "text-muted-foreground"
                },
                'data_attributes': {},
                'variant_patterns': {},
                'style_classes': set()
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': set()
            }
        ),
        "CardContent": Component(
            name="CardContent",
            tag="div",
            match_pattern={
                'signature_classes': {
                    "p-6", "pt-0"
                },
                'data_attributes': {},
                'variant_patterns': {},
                'style_classes': set()
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': set()
            }
        ),
       "CardFooter": Component(
            name="CardFooter",
            tag="div",
            match_pattern={
                'signature_classes': {
                    "flex", "items-center", "p-6", "pt-0"
                },
                'data_attributes': {},
                'variant_patterns': {},
                'style_classes': set()
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': set()
            }
        ),
        "Input": Component(
            name="Input",
            tag="input",
            match_pattern={
                'signature_classes': {
                    "flex", "w-full", "min-w-0", "outline-none", "bg-transparent",
                    "file:text-foreground", "file:inline-flex", "file:h-7", "file:border-0",
                    "file:bg-transparent", "file:text-sm", "file:font-medium",
                    "disabled:pointer-events-none", "disabled:cursor-not-allowed", "disabled:opacity-50",
                    "selection:bg-primary", "selection:text-primary-foreground",
                },
                'data_attributes': {"data-slot": "input"},
                'variant_patterns': {},  # no built-in variants in shadcn's Input
                'style_classes': {
                    "h-9", "rounded-md", "border", "border-input", "px-3", "py-1",
                    "text-base", "md:text-sm", "placeholder:text-muted-foreground",
                    "shadow-xs", "transition-[color,box-shadow]",
                    "focus-visible:border-ring", "focus-visible:ring-ring/50", "focus-visible:ring-[3px]",
                    "aria-invalid:border-destructive", "aria-invalid:ring-destructive/20", "dark:aria-invalid:ring-destructive/40",
                    "dark:bg-input/30",
                }
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': {"data-slot"}
            }
        ),
        "LucideIcon": Component(
            name="LucideIcon",
            tag="svg",
            match_pattern={
                'signature_classes': {"lucide"},
                'data_attributes': {},
                'variant_patterns': {},
                'style_classes': set()
            },
            config={
                'self_closing': True,
                'ignore_children': True,  # Prevents rendering inner SVG paths
                'output_blacklist': {
                    "xmlns", "stroke", "fill", "viewbox", "aria-hidden",
                    "focusable", "width", "height", "stroke-width", "color",
                    "xmlns:xlink", "xlink:href", "xlink:show", "xlink:title",
                    "xlink:role", "stroke-linecap", "stroke-linejoin"
                }
            }
        ),
        "Label": Component(
            name="Label",
            tag="label",
            match_pattern={
                'signature_classes': {
                    "leading-none", "select-none",
                    "group-data-[disabled=true]:pointer-events-none",
                    "group-data-[disabled=true]:opacity-50",
                    "peer-disabled:cursor-not-allowed",
                    "peer-disabled:opacity-50"
                },
                'data_attributes': {"data-slot": "label"},
                'variant_patterns': {},      
                'style_classes': {"gap-2", "font-medium", "text-sm", "items-center", "flex"}
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': {"data-slot"}
            }
        ),
                "FormItem": Component(
            name="FormItem",
            tag="div",
            match_pattern={
                'signature_classes': {"grid"},
                'data_attributes': {"data-slot": "form-item"},
                'variant_patterns': {},
                'style_classes': {"gap-2"}
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': {"data-slot"}
            }
        ),
        "FormLabel": Component(
            name="FormLabel",
            tag="label", # Inherits from Label component
            match_pattern={
                'signature_classes': {
                    # Inherited from Label
                    "leading-none", "select-none",
                    "group-data-[disabled=true]:pointer-events-none",
                    "group-data-[disabled=true]:opacity-50",
                    "peer-disabled:cursor-not-allowed",
                    "peer-disabled:opacity-50",
                    # Added by FormLabel
                    "data-[error=true]:text-destructive"
                 },
                'data_attributes': {"data-slot": "form-label"},
                'variant_patterns': {},
                'style_classes': {
                    # Inherited from Label
                    "gap-2", "font-medium", "text-sm", "items-center", "flex"
                }
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': {"data-slot", "data-error", "htmlFor"}
            }
        ),
        "FormControl": Component(
            name="FormControl",
            tag="Slot", # Special case: Slot merges props, doesn't render itself
            match_pattern={
                'signature_classes': set(), # Attributes are added dynamically
                'data_attributes': {"data-slot": "form-control"},
                'variant_patterns': {},
                'style_classes': set()
            },
            config={
                'self_closing': False, # Depends on the child
                'ignore_children': False,
                 # These attributes are dynamically added based on context
                'output_blacklist': {"data-slot", "aria-describedby", "aria-invalid"}
            }
        ),
        "FormDescription": Component(
            name="FormDescription",
            tag="p",
            match_pattern={
                'signature_classes': {},
                'data_attributes': {"data-slot": "form-description"},
                'variant_patterns': {},
                'style_classes': {"text-sm", "text-muted-foreground"}
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': {"data-slot"}
            }
        ),
        "FormMessage": Component(
            name="FormMessage",
            tag="p",
            match_pattern={
                'signature_classes': {},
                'data_attributes': {"data-slot": "form-message"},
                'variant_patterns': {},
                'style_classes': {"text-sm", "text-destructive"}
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': {"data-slot"}
            }
        ),
        "Form": Component(
            name="Form",
            tag="form",
            match_pattern={
                'signature_classes': set(),
                'data_attributes': {},
                'variant_patterns': {},
                'style_classes': set()
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': set()
            }
        ),
    }
