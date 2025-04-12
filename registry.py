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
        "BadgeLegacy": Component(
            name="Badge",
            tag="div", # Based on the React component rendering a div
            match_pattern={
                'signature_classes': {
                    # Base classes from cva related to interaction/state
                    "transition-colors",
                    "focus:outline-none",
                    "focus:ring-2",
                    "focus:ring-ring",
                    "focus:ring-offset-2",
                },
                'data_attributes': {}, # No specific data attributes in the React example
                'variant_patterns': {
                    "variant": {
                        "default": {
                            "border-transparent", "bg-primary", "text-primary-foreground",
                            "hover:bg-primary/80"
                        },
                        "secondary": {
                            "border-transparent", "bg-secondary", "text-secondary-foreground",
                            "hover:bg-secondary/80"
                        },
                        "destructive": {
                            "border-transparent", "bg-destructive", "text-destructive-foreground",
                            "hover:bg-destructive/80"
                        },
                        "outline": {
                            "text-foreground"
                        },
                    }
                },
                'style_classes': {
                    # Base classes from cva related to layout/appearance
                    "inline-flex", "items-center", "rounded-full", "border",
                    "px-2.5", "py-0.5", "text-xs", "font-semibold",
                }
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': set() # No attributes to blacklist from the example
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
        "Progress": Component(
            name="Progress",
            tag="div", # Radix ProgressPrimitive.Root renders a div
            match_pattern={
                'signature_classes': set(),
                'data_attributes': {"data-slot": "progress"},
                'variant_patterns': {},
                'style_classes': {
                    "relative", "h-2", "w-full", "overflow-hidden", "rounded-full", "bg-primary/20"
                } 
            },
            config={
                'self_closing': True,
                'ignore_children': True, 
                'output_blacklist': {"data-slot", "aria-valuemax", "aria-valuemin", "data-max", "aria-label", "data-state", "role"} 
            }
        ),
                "NavigationMenu": Component(
            name="NavigationMenu",
            tag="nav", # Radix NavigationMenuPrimitive.Root
            match_pattern={
                'signature_classes': {
                    "group/navigation-menu", 
                },
                'data_attributes': {"data-slot": "navigation-menu"},
                'variant_patterns': {},
                'style_classes': {
                    "relative", "flex", "max-w-max", "flex-1", 
                    "items-center", "justify-center"
                }
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': {"data-slot", "data-viewport"}
            }
        ),
        "NavigationMenuList": Component(
            name="NavigationMenuList",
            tag="ul", # Radix NavigationMenuPrimitive.List
            match_pattern={
                'signature_classes': {
                    "group", "list-none",
                },
                'data_attributes': {"data-slot": "navigation-menu-list"},
                'variant_patterns': {},
                'style_classes': {
                    "flex", "flex-1", "items-center", "justify-center", "gap-1"
                }
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': {"data-slot"}
            }
        ),
        "NavigationMenuItem": Component(
            name="NavigationMenuItem",
            tag="li", # Radix NavigationMenuPrimitive.Item
            match_pattern={
                'signature_classes': set(),
                'data_attributes': {"data-slot": "navigation-menu-item"},
                'variant_patterns': {},
                'style_classes': {"relative"}
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': {"data-slot"}
            }
        ),
        "NavigationMenuTrigger": Component(
            name="NavigationMenuTrigger",
            tag="button", # Radix NavigationMenuPrimitive.Trigger
            match_pattern={
                'signature_classes': {
                    "group", "disabled:pointer-events-none", "disabled:opacity-50",
                    "data-[state=open]:hover:bg-accent", "data-[state=open]:text-accent-foreground",
                    "data-[state=open]:focus:bg-accent", "data-[state=open]:bg-accent/50",
                },
                'data_attributes': {"data-slot": "navigation-menu-trigger"},
                'variant_patterns': {},
                'style_classes': {
                    "focus-visible:ring-ring/50", "focus-visible:ring-[3px]", "focus-visible:outline-1",
                    "inline-flex", "h-9", "w-max", "items-center", "justify-center",
                    "rounded-md", "bg-background", "px-4", "py-2", "text-sm", "font-medium",
                    "hover:bg-accent", "hover:text-accent-foreground", "focus:bg-accent",
                    "focus:text-accent-foreground", "outline-none", "transition-[color,box-shadow]"
                }
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': {"data-slot", "data-state", "aria-controls", "aria-expanded", "data-radix-collection-item", "id"}
            }
        ),
        "NavigationMenuContent": Component(
            name="NavigationMenuContent",
            tag="div", # Radix NavigationMenuPrimitive.Content
            match_pattern={
                'signature_classes': {
                    # Motion animations
                    "data-[motion^=from-]:animate-in", "data-[motion^=to-]:animate-out",
                    "data-[motion^=from-]:fade-in", "data-[motion^=to-]:fade-out",
                    "data-[motion=from-end]:slide-in-from-right-52",
                    "data-[motion=from-start]:slide-in-from-left-52",
                    "data-[motion=to-end]:slide-out-to-right-52",
                    "data-[motion=to-start]:slide-out-to-left-52",
                    # Viewport=false specific styles/animations (complex selectors)
                    "group-data-[viewport=false]/navigation-menu:bg-popover",
                    "group-data-[viewport=false]/navigation-menu:text-popover-foreground",
                    "group-data-[viewport=false]/navigation-menu:data-[state=open]:animate-in",
                    "group-data-[viewport=false]/navigation-menu:data-[state=closed]:animate-out",
                    "group-data-[viewport=false]/navigation-menu:data-[state=closed]:zoom-out-95",
                    "group-data-[viewport=false]/navigation-menu:data-[state=open]:zoom-in-95",
                    "group-data-[viewport=false]/navigation-menu:data-[state=open]:fade-in-0",
                    "group-data-[viewport=false]/navigation-menu:data-[state=closed]:fade-out-0",
                    "group-data-[viewport=false]/navigation-menu:top-full",
                    "group-data-[viewport=false]/navigation-menu:mt-1.5",
                    "group-data-[viewport=false]/navigation-menu:overflow-hidden",
                    "group-data-[viewport=false]/navigation-menu:rounded-md",
                    "group-data-[viewport=false]/navigation-menu:border",
                    "group-data-[viewport=false]/navigation-menu:shadow",
                    "group-data-[viewport=false]/navigation-menu:duration-200",
                    # Descendant link focus styles (complex selectors, assuming **: means descendant)
                    "**:data-[slot=navigation-menu-link]:focus:ring-0", 
                    "**:data-[slot=navigation-menu-link]:focus:outline-none"
                },
                'data_attributes': {"data-slot": "navigation-menu-content"},
                'variant_patterns': {},
                'style_classes': {
                    # General layout and positioning (more likely to be customized)
                    "top-0", "left-0", "w-full", "p-2", "pr-2.5",
                    "md:absolute", "md:w-auto"
                }
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': {
                    "data-slot", "data-state", "data-motion",
                    "aria-labelledby", "data-orientation", "id", 
                    "dir"
                }
            }
        ),
        "NavigationMenuViewport": Component(
            name="NavigationMenuViewport",
            tag="div", # Radix NavigationMenuPrimitive.Viewport
            match_pattern={
                'signature_classes': {
                    # State-based animations
                    "data-[state=open]:animate-in", "data-[state=closed]:animate-out",
                    "data-[state=closed]:zoom-out-95", "data-[state=open]:zoom-in-90"
                },
                'data_attributes': {"data-slot": "navigation-menu-viewport"},
                'variant_patterns': {},
                'style_classes': {
                    # Layout, positioning, appearance (more likely to be customized)
                    "origin-top-center", "bg-popover", "text-popover-foreground",
                    "relative", "mt-1.5", "overflow-hidden", "rounded-md", "border", "shadow",
                    "h-[var(--radix-navigation-menu-viewport-height)]", # Added
                    "w-full", # Added
                    "md:w-[var(--radix-navigation-menu-viewport-width)]" # Added
                }
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': {"data-slot", "data-state", "data-orientation"},
                'skip_this_element': True
            }
        ),
        "NavigationMenuLink": Component(
            name="NavigationMenuLink",
            tag="a", # Radix NavigationMenuPrimitive.Link
            match_pattern={
                'signature_classes': {
                    "data-[active=true]:focus:bg-accent", "data-[active=true]:hover:bg-accent",
                    "data-[active=true]:bg-accent/50", "data-[active=true]:text-accent-foreground",
                    "focus-visible:outline-1", 
                    "[&_svg:not([class*='text-'])]:text-muted-foreground",
                    "[&_svg:not([class*='size-'])]:size-4"
                },
                'data_attributes': {"data-slot": "navigation-menu-link"},
                'variant_patterns': {},
                'style_classes': {
                    "focus-visible:ring-ring/50", "focus-visible:ring-[3px]",
                    "hover:bg-accent", "hover:text-accent-foreground", "focus:bg-accent",
                    "focus:text-accent-foreground", "flex", "flex-col", "gap-1", 
                    "rounded-sm", "p-2", "text-sm", "transition-all", "outline-none"
                }
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': {"data-slot", "data-active", "data-radix-collection-item"}
            }
        ),
        "NavigationMenuIndicator": Component(
            name="NavigationMenuIndicator",
            tag="div", # Radix NavigationMenuPrimitive.Indicator
            match_pattern={
                'signature_classes': {
                    "data-[state=visible]:animate-in", "data-[state=hidden]:animate-out",
                    "data-[state=hidden]:fade-out", "data-[state=visible]:fade-in"
                },
                'data_attributes': {"data-slot": "navigation-menu-indicator"},
                'variant_patterns': {},
                'style_classes': {
                    "top-full", "z-[1]", "flex", "h-1.5", "items-end", "justify-center",
                    "overflow-hidden"
                }
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': {"data-slot", "data-state"}
            }
        ),
                "DialogTrigger": Component(
            name="DialogTrigger",
            tag="button", # Radix DialogPrimitive.Trigger (often a button)
            match_pattern={
                'signature_classes': set(),
                'data_attributes': {"data-slot": "dialog-trigger"},
                'variant_patterns': {},
                'style_classes': set() # Styles are typically added via Button component or className
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': {"data-slot", "data-state", "aria-controls", "aria-haspopup", "aria-expanded", "type"}
            }
        ),
        "DialogPortal": Component(
            name="DialogPortal",
            tag="div", # Radix DialogPrimitive.Portal renders a div by default
            match_pattern={
                'signature_classes': set(),
                'data_attributes': {"data-slot": "dialog-portal"},
                'variant_patterns': {},
                'style_classes': set()
            },
            config={
                'self_closing': False,
                'ignore_children': False, # Renders children elsewhere
                'output_blacklist': {"data-slot"},
                'skip_this_element': True # Portal itself is not styled or directly rendered in place
            }
        ),
        "DialogClose": Component(
            name="DialogClose",
            tag="button", # Radix DialogPrimitive.Close (often a button)
            match_pattern={
                'signature_classes': set(),
                'data_attributes': {"data-slot": "dialog-close"},
                'variant_patterns': {},
                'style_classes': set() # Styles are typically added via Button component or className
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': {"data-slot", "data-state", "type"}
            }
        ),
        "DialogOverlay": Component(
            name="DialogOverlay",
            tag="div", # Radix DialogPrimitive.Overlay renders a div
            match_pattern={
                'signature_classes': {
                    # State-based animations
                    "data-[state=open]:animate-in", "data-[state=closed]:animate-out", 
                    "data-[state=closed]:fade-out-0", "data-[state=open]:fade-in-0"
                },
                'data_attributes': {"data-slot": "dialog-overlay"},
                'variant_patterns': {},
                'style_classes': {
                    # Positioning and appearance
                    "fixed", "inset-0", "z-50", "bg-black/50"
                }
            },
            config={
                'self_closing': False, # Can have content, though usually doesn't
                'ignore_children': False,
                'output_blacklist': {"data-slot", "data-state"}
            }
        ),
        "DialogContent": Component(
            name="DialogContent",
            tag="div", # Radix DialogPrimitive.Content renders a div
            match_pattern={
                'signature_classes': {
                    # State-based animations
                    "data-[state=open]:animate-in", "data-[state=closed]:animate-out", 
                    "data-[state=closed]:fade-out-0", "data-[state=open]:fade-in-0", 
                    "data-[state=closed]:zoom-out-95", "data-[state=open]:zoom-in-95"
                },
                'data_attributes': {"data-slot": "dialog-content"},
                'variant_patterns': {},
                'style_classes': {
                    # Appearance, layout, positioning
                    "bg-background", "fixed", "top-[50%]", "left-[50%]", "z-50", "grid", 
                    "w-full", "max-w-[calc(100%-2rem)]", "translate-x-[-50%]", "translate-y-[-50%]", 
                    "gap-4", "rounded-lg", "border", "p-6", "shadow-lg", "duration-200", 
                    "sm:max-w-lg"
                }
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': {"data-slot", "data-state", "role", "aria-describedby", "aria-labelledby", "tabindex", "id"}
            }
        ),
        "DialogHeader": Component(
            name="DialogHeader",
            tag="div",
            match_pattern={
                'signature_classes': set(),
                'data_attributes': {"data-slot": "dialog-header"},
                'variant_patterns': {},
                'style_classes': {
                    # Layout and text alignment
                    "flex", "flex-col", "gap-2", "text-center", "sm:text-left"
                }
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': {"data-slot"}
            }
        ),
        "DialogFooter": Component(
            name="DialogFooter",
            tag="div",
            match_pattern={
                'signature_classes': set(),
                'data_attributes': {"data-slot": "dialog-footer"},
                'variant_patterns': {},
                'style_classes': {
                    # Layout and justification
                    "flex", "flex-col-reverse", "gap-2", "sm:flex-row", "sm:justify-end"
                }
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': {"data-slot"}
            }
        ),
        "DialogTitle": Component(
            name="DialogTitle",
            tag="h2", # Radix DialogPrimitive.Title renders h2 by default
            match_pattern={
                'signature_classes': set(),
                'data_attributes': {"data-slot": "dialog-title"},
                'variant_patterns': {},
                'style_classes': {
                    # Typography
                    "text-lg", "leading-none", "font-semibold"
                }
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': {"data-slot", "id"}
            }
        ),
        "DialogDescription": Component(
            name="DialogDescription",
            tag="p", # Radix DialogPrimitive.Description renders p by default
            match_pattern={
                'signature_classes': set(),
                'data_attributes': {"data-slot": "dialog-description"},
                'variant_patterns': {},
                'style_classes': {
                    # Typography and color
                    "text-muted-foreground", "text-sm"
                }
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': {"data-slot", "id"}
            }
        ),
    }
