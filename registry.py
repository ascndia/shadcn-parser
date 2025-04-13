from components import Component
from typing import Dict, Tuple, Optional
from tailwind_merge import TailwindMerge

COMPONENTS = {
        "Button": Component(
            name="Button",
            tag="button",
            match_pattern={
                'signature_classes': {

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
                    "focus-visible:outline-none",
                    "focus-visible:ring-2",
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
        "Button": Component(
            name="Button",
            tag="button",
            match_pattern={
                'signature_classes': {
                    # Core interaction/state classes from cva base
                    "focus-visible:ring-1", "focus-visible:ring-ring",
                    "disabled:pointer-events-none", "disabled:opacity-50",
                    "[&_svg]:pointer-events-none", "[&_svg]:size-4", "[&_svg]:shrink-0",
                },
                'data_attributes': {},
                'variant_patterns': {
                    "variant": {
                        "default": {"bg-primary", "text-primary-foreground", "shadow", "hover:bg-primary/90"},
                        "destructive": {"bg-destructive", "text-destructive-foreground", "shadow-sm", "hover:bg-destructive/90"},
                        "outline": {"border", "border-input", "bg-background", "shadow-sm", "hover:bg-accent", "hover:text-accent-foreground"},
                        "secondary": {"bg-secondary", "text-secondary-foreground", "shadow-sm", "hover:bg-secondary/80"},
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
                    "inline-flex", "items-center", "justify-center", "gap-2",
                    "whitespace-nowrap", "rounded-md", "text-sm", "font-medium",
                    "transition-colors", "focus-visible:outline-none",
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
            tag="div", 
            match_pattern={
                'signature_classes': {
                    
                    "transition-colors",
                    "focus:outline-none",
                    "focus:ring-2",
                    "focus:ring-ring",
                    "focus:ring-offset-2",
                },
                'data_attributes': {}, 
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
                    
                    "inline-flex", "items-center", "rounded-full", "border",
                    "px-2.5", "py-0.5", "text-xs", "font-semibold",
                }
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': set() 
            }
        ),
        "Separator": Component(
            name="Separator",
            tag="div",  
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
                'signature_classes': {"bg-card", "text-card-foreground"},
                'data_attributes': {},
                'variant_patterns': {},  
                'style_classes': {
                    "rounded-xl", "border", "bg-card", "text-card-foreground", "shadow"
                }
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
                'variant_patterns': {},  
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
                'ignore_children': True,  
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
            tag="label", 
            match_pattern={
                'signature_classes': {
                    
                    "leading-none", "select-none",
                    "group-data-[disabled=true]:pointer-events-none",
                    "group-data-[disabled=true]:opacity-50",
                    "peer-disabled:cursor-not-allowed",
                    "peer-disabled:opacity-50",
                    
                    "data-[error=true]:text-destructive"
                 },
                'data_attributes': {"data-slot": "form-label"},
                'variant_patterns': {},
                'style_classes': {
                    
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
            tag="Slot", 
            match_pattern={
                'signature_classes': set(), 
                'data_attributes': {"data-slot": "form-control"},
                'variant_patterns': {},
                'style_classes': set()
            },
            config={
                'self_closing': False, 
                'ignore_children': False,
                 
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
            tag="div", 
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
            tag="nav", 
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
            tag="ul", 
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
            tag="li", 
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
            tag="button", 
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
            tag="div", 
            match_pattern={
                'signature_classes': {
                    
                    "data-[motion^=from-]:animate-in", "data-[motion^=to-]:animate-out",
                    "data-[motion^=from-]:fade-in", "data-[motion^=to-]:fade-out",
                    "data-[motion=from-end]:slide-in-from-right-52",
                    "data-[motion=from-start]:slide-in-from-left-52",
                    "data-[motion=to-end]:slide-out-to-right-52",
                    "data-[motion=to-start]:slide-out-to-left-52",
                    
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
                    
                    "**:data-[slot=navigation-menu-link]:focus:ring-0", 
                    "**:data-[slot=navigation-menu-link]:focus:outline-none"
                },
                'data_attributes': {"data-slot": "navigation-menu-content"},
                'variant_patterns': {},
                'style_classes': {
                    
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
            tag="div", 
            match_pattern={
                'signature_classes': {
                    
                    "data-[state=open]:animate-in", "data-[state=closed]:animate-out",
                    "data-[state=closed]:zoom-out-95", "data-[state=open]:zoom-in-90"
                },
                'data_attributes': {"data-slot": "navigation-menu-viewport"},
                'variant_patterns': {},
                'style_classes': {
                    
                    "origin-top-center", "bg-popover", "text-popover-foreground",
                    "relative", "mt-1.5", "overflow-hidden", "rounded-md", "border", "shadow",
                    "h-[var(--radix-navigation-menu-viewport-height)]", 
                    "w-full", 
                    "md:w-[var(--radix-navigation-menu-viewport-width)]" 
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
            tag="a", 
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
            tag="div", 
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
            tag="button", 
            match_pattern={
                'signature_classes': set(),
                'data_attributes': {"data-slot": "dialog-trigger"},
                'variant_patterns': {},
                'style_classes': set() 
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': {"data-slot", "data-state", "aria-controls", "aria-haspopup", "aria-expanded", "type"}
            }
        ),
        "DialogPortal": Component(
            name="DialogPortal",
            tag="div", 
            match_pattern={
                'signature_classes': set(),
                'data_attributes': {"data-slot": "dialog-portal"},
                'variant_patterns': {},
                'style_classes': set()
            },
            config={
                'self_closing': False,
                'ignore_children': False, 
                'output_blacklist': {"data-slot"},
                'skip_this_element': True 
            }
        ),
        "DialogClose": Component(
            name="DialogClose",
            tag="button", 
            match_pattern={
                'signature_classes': set(),
                'data_attributes': {"data-slot": "dialog-close"},
                'variant_patterns': {},
                'style_classes': set() 
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': {"data-slot", "data-state", "type"}
            }
        ),
        "DialogOverlay": Component(
            name="DialogOverlay",
            tag="div", 
            match_pattern={
                'signature_classes': {
                    
                    "data-[state=open]:animate-in", "data-[state=closed]:animate-out", 
                    "data-[state=closed]:fade-out-0", "data-[state=open]:fade-in-0"
                },
                'data_attributes': {"data-slot": "dialog-overlay"},
                'variant_patterns': {},
                'style_classes': {
                    
                    "fixed", "inset-0", "z-50", "bg-black/50"
                }
            },
            config={
                'self_closing': False, 
                'ignore_children': False,
                'output_blacklist': {"data-slot", "data-state"}
            }
        ),
        "DialogContent": Component(
            name="DialogContent",
            tag="div", 
            match_pattern={
                'signature_classes': {
                    
                    "data-[state=open]:animate-in", "data-[state=closed]:animate-out", 
                    "data-[state=closed]:fade-out-0", "data-[state=open]:fade-in-0", 
                    "data-[state=closed]:zoom-out-95", "data-[state=open]:zoom-in-95"
                },
                'data_attributes': {"data-slot": "dialog-content"},
                'variant_patterns': {},
                'style_classes': {
                    
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
        "DialogContentLegacy": Component(
            name="DialogContent",
            tag="div", 
            match_pattern={
                'signature_classes': set(),
                'data_attributes': {"role": "dialog"},
                'variant_patterns': {},
                'style_classes': {
                    "data-[state=open]:zoom-in-95",
                    "data-[state=open]:slide-in-from-left-1/2", "data-[state=closed]:slide-out-to-left-1/2", 
                    "data-[state=closed]:slide-out-to-top-[48%]", "data-[state=open]:slide-in-from-top-[48%]", 
                    "data-[state=closed]:fade-out-0", "data-[state=open]:animate-in",
                    "data-[state=open]:fade-in-0","data-[state=closed]:zoom-out-95","data-[state=closed]:animate-out",
                    "bg-background", "fixed", "top-[50%]", "left-[50%]", "z-50", "grid", 
                    "w-full", "max-w-lg", "translate-x-[-50%]", "translate-y-[-50%]", 
                    "gap-4", "rounded-lg", "border", "p-6", "shadow-lg", "duration-200", 
                    "sm:max-w-lg", "outline-hidden", "sm:rounded-lg"
                }
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': {"style","data-slot", "data-state", "role", "aria-describedby", "aria-labelledby", "tabindex", "id"}
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
            tag="h2", 
            match_pattern={
                'signature_classes': set(),
                'data_attributes': {"data-slot": "dialog-title"},
                'variant_patterns': {},
                'style_classes': {
                    
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
            tag="p", 
            match_pattern={
                'signature_classes': set(),
                'data_attributes': {"data-slot": "dialog-description"},
                'variant_patterns': {},
                'style_classes': {
                    
                    "text-muted-foreground", "text-sm"
                }
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': {"data-slot", "id"}
            }
        ),
                "Tabs": Component(
            name="Tabs",
            tag="div", 
            match_pattern={
                'signature_classes': set(),
                'data_attributes': {"data-slot": "tabs"},
                'variant_patterns': {},
                'style_classes': {"flex", "flex-col", "gap-2"}
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': {"data-slot", "data-orientation"}
            }
        ),
        "TabsList": Component(
            name="TabsList",
            tag="div", 
            match_pattern={
                'signature_classes': set(),
                'data_attributes': {"data-slot": "tabs-list"},
                'variant_patterns': {},
                'style_classes': {
                    "bg-muted", "text-muted-foreground", "inline-flex", "h-9", "w-fit",
                    "items-center", "justify-center", "rounded-lg", "p-[3px]"
                }
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': {"data-slot", "role", "aria-orientation", "tabindex", "data-orientation"}
            }
        ),
        "TabsTrigger": Component(
            name="TabsTrigger",
            tag="button", 
            match_pattern={
                'signature_classes': {
                    "data-[state=active]:bg-background", "dark:data-[state=active]:text-foreground",
                    "focus-visible:border-ring", "focus-visible:ring-ring/50", "focus-visible:outline-ring",
                    "dark:data-[state=active]:border-input", "dark:data-[state=active]:bg-input/30",
                    "transition-[color,box-shadow]", "focus-visible:ring-[3px]", "focus-visible:outline-1",
                    "disabled:pointer-events-none", "disabled:opacity-50", "data-[state=active]:shadow-sm",
                    "[&_svg]:pointer-events-none", "[&_svg]:shrink-0", "[&_svg:not([class*='size-'])]:size-4"
                },
                'data_attributes': {"data-slot": "tabs-trigger"},
                'variant_patterns': {},
                'style_classes': {
                    "text-foreground", "dark:text-muted-foreground", "inline-flex", "h-[calc(100%-1px)]",
                    "flex-1", "items-center", "justify-center", "gap-1.5", "rounded-md", "border",
                    "border-transparent", "px-2", "py-1", "text-sm", "font-medium", "whitespace-nowrap"
                }
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': {
                    "data-radix-collection-item", "data-orientation", 
                    "data-slot", "role", "aria-selected", "data-state", "tabindex", "type", "id", "aria-controls"
                }   
            }
        ),
        "TabsContent": Component(
            name="TabsContent",
            tag="div", 
            match_pattern={
                'signature_classes': set(),
                'data_attributes': {"data-slot": "tabs-content"},
                'variant_patterns': {},
                'style_classes': {"flex-1", "outline-none"}
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': {"data-slot", "role", "aria-labelledby", "data-state", "tabindex", "data-orientation", "id"}
            }
        ),
        "DialogClose": Component(
            name="DialogClose",
            tag="button", 
            match_pattern={
                'signature_classes': {
                    "ring-offset-background", "focus:ring-ring",
                    "data-[state=open]:bg-accent", "data-[state=open]:text-muted-foreground",
                    "transition-opacity", "hover:opacity-100",
                    "focus:ring-2", "focus:ring-offset-2", "focus:outline-hidden", 
                    "disabled:pointer-events-none",
                    "[&_svg]:pointer-events-none", "[&_svg]:shrink-0", "[&_svg:not([class*='size-'])]:size-4"
                },
                'data_attributes': {},
                'variant_patterns': {},
                'style_classes': {                    
                    "absolute", "top-4", "right-4", "rounded-xs", "opacity-70"
                }
            },
            config={
                'self_closing': True,
                'ignore_children': True,
                'output_blacklist': {"data-slot", "data-state", "type"},
                'skip_this_element': True

            }
        ),
         "ButtonNew": Component( # Renamed to avoid conflict, adjust name as needed
            name="Button", # Or potentially a different name like "StyledButton"
            tag="button",
            match_pattern={
                'signature_classes': {
                    # Interaction, state, and transition classes
                    "transition-all", # Different transition
                    "disabled:pointer-events-none", "disabled:opacity-50",
                    "focus-visible:border-ring", # Different focus style
                    "focus-visible:ring-ring/50", # Different focus style
                    "focus-visible:ring-[3px]", # Different focus style
                    "aria-invalid:ring-destructive/20", # Added invalid state
                    "dark:aria-invalid:ring-destructive/40", # Added invalid state
                    "aria-invalid:border-destructive", # Added invalid state
                    "[&_svg]:pointer-events-none",
                    "[&_svg:not([class*='size-'])]:size-4", # Specific SVG sizing
                    "[&_svg]:shrink-0",
                },
                'data_attributes': {"data-slot": "button"}, # Added data-slot
                'variant_patterns': {
                    "variant": {
                        "default": {
                            "bg-primary", "text-primary-foreground",
                            "hover:bg-primary/90"
                            },
                        # Add other variants (destructive, outline, etc.) if they follow a similar pattern
                    },
                    "size": {
                        "default": { # Based on the example provided
                            "h-10", "px-6", "has-[>svg]:px-4" # Specific padding logic
                            },
                        # Add other sizes (sm, lg, icon) if needed
                    }
                },
                'style_classes': {
                    # Layout, appearance, typography
                    "inline-flex", "items-center", "justify-center", "gap-2",
                    "whitespace-nowrap", "text-sm", "font-medium",
                    "shrink-0", # Added shrink-0
                    "outline-none", # Added outline-none
                    "shadow-xs", # Added shadow-xs
                    "rounded-md",
                }
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': {"data-slot"} # Blacklist data-slot if needed
            }
        ),
        "Avatar": Component(
            name="Avatar",
            tag="span", # Radix AvatarPrimitive.Root renders a span
            match_pattern={
                'signature_classes': set(),
                'data_attributes': {"data-slot": "avatar"},
                'variant_patterns': {},
                'style_classes': {
                    "relative", "flex", "size-8", "shrink-0", "overflow-hidden", "rounded-full"
                }
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': {"data-slot"}
            }
        ),
        "AvatarImage": Component(
            name="AvatarImage",
            tag="img", # Radix AvatarPrimitive.Image renders an img
            match_pattern={
                'signature_classes': set(),
                'data_attributes': {"data-slot": "avatar-image"},
                'variant_patterns': {},
                'style_classes': {"aspect-square", "size-full"}
            },
            config={
                'self_closing': True,
                'ignore_children': True,
                'output_blacklist': {"data-slot"}
            }
        ),
        "AvatarFallback": Component(
            name="AvatarFallback",
            tag="span", # Radix AvatarPrimitive.Fallback renders a span
            match_pattern={
                'signature_classes': set(),
                'data_attributes': {"data-slot": "avatar-fallback"},
                'variant_patterns': {},
                'style_classes': {
                    "bg-muted", "flex", "size-full", "items-center", "justify-center", "rounded-full"
                }
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': {"data-slot"}
            }
        ),
        "AvatarLegacy": Component(
            name="Avatar",
            tag="span", # Radix AvatarPrimitive.Root renders a span
            match_pattern={
                'signature_classes': set(),
                'data_attributes': {},
                'variant_patterns': {},
                'style_classes': {
                    "relative", "flex", "size-8", "shrink-0", "overflow-hidden", "rounded-full"
                }
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': {}
            }
        ),
        "AvatarImageLegacy": Component(
            name="AvatarImage",
            tag="img", # Radix AvatarPrimitive.Image renders an img
            match_pattern={
                'signature_classes': set(),
                'data_attributes': {},
                'variant_patterns': {},
                'style_classes': {"aspect-square", "size-full"}
            },
            config={
                'self_closing': True,
                'ignore_children': True,
                'output_blacklist': {}
            }
        ),
        "AvatarFallbackLegacy": Component(
            name="AvatarFallback",
            tag="span", # Radix AvatarPrimitive.Fallback renders a span
            match_pattern={
                'signature_classes': set(),
                'data_attributes': {},
                'variant_patterns': {},
                'style_classes': {
                    "bg-muted", "flex", "size-full", "items-center", "justify-center", "rounded-full"
                }
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': {}
            }
        ),
        "Command": Component(
            name="Command",
            tag="div", # Based on CommandPrimitive
            match_pattern={
                'signature_classes': {"flex", "h-full", "w-full", "flex-col", "overflow-hidden", "rounded-md"},
                'data_attributes': {"data-slot": "command"},
                'variant_patterns': {},
                'style_classes': {"bg-popover", "text-popover-foreground"}
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': {"data-slot", "cmdk-root", "tabindex", "aria-hidden"}
            }
        ),
        "CommandLegacy": Component(
            name="Command",
            tag="div", # Based on CommandPrimitive
            match_pattern={
                'signature_classes': set(),
                'data_attributes': {"cmdk-root": ""},
                'variant_patterns': {},
                'style_classes': {
                    "bg-popover", "text-popover-foreground"
                    "flex", "h-full", "w-full", "flex-col", "overflow-hidden", "rounded-md"
                }
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': {"data-slot", "cmdk-root", "tabindex", "aria-hidden"},
            }
        ),
        # CommandDialog is skipped as it primarily composes Dialog and Command
        "CommandInput": Component( # Wrapper div for CommandInput
            name="CommandInput", # Custom name for the wrapper
            tag="div",
            match_pattern={
                'signature_classes': {"flex", "items-center", "border-b", "px-3"},
                'data_attributes': {"data-slot": "command-input-wrapper"},
                'variant_patterns': {},
                'style_classes': {"h-9", "gap-2"} # h-9 might vary based on CommandDialog usage
            },
            config={
                'self_closing': True,
                'ignore_children': True, # Contains Icon and Input
                'output_blacklist': {"data-slot", "cmdk-input-wrapper"}
            }
        ),
        "CommandInputLegacy": Component( # Wrapper div for CommandInput
            name="CommandInput", # Custom name for the wrapper
            tag="div",
            match_pattern={
                'signature_classes': set(),
                'data_attributes': {"cmdk-input-wrapper": ""},
                'variant_patterns': {},
                'style_classes': {
                    "h-9", "gap-2"
                    "flex", "items-center", "border-b", "px-3"
                } 
            },
            config={
                'self_closing': True,
                'ignore_children': True, # Contains Icon and Input
                'output_blacklist': {"data-slot", "cmdk-input-wrapper"},
                
            }
        ),
        # "CommandInput": Component(
        #     name="CommandInput",
        #     tag="input", # Based on CommandPrimitive.Input
        #     match_pattern={
        #         'signature_classes': {
        #             "flex", "w-full", "rounded-md", "bg-transparent", "text-sm", "outline-hidden",
        #             "disabled:cursor-not-allowed", "disabled:opacity-50"
        #         },
        #         'data_attributes': {"data-slot": "command-input"},
        #         'variant_patterns': {},
        #         'style_classes': {"placeholder:text-muted-foreground", "h-10", "py-3"} # h-10 might vary
        #     },
        #     config={
        #         'self_closing': True,
        #         'ignore_children': True,
        #         'output_blacklist': {
        #             "data-slot", "cmdk-input", "autocomplete", "autocorrect", "spellcheck",
        #             "aria-autocomplete", "role", "aria-expanded", "aria-controls",
        #             "aria-labelledby", "id", "type", "value", "placeholder" # placeholder might be needed
        #         }
        #     }
        # ),
        # "CommandInputLegacy": Component(
        #     name="CommandInput",
        #     tag="input", # Based on CommandPrimitive.Input
        #     match_pattern={
        #         'signature_classes': {                    
        #             "disabled:cursor-not-allowed", "disabled:opacity-50"
        #         },
        #         'data_attributes': {"cmdk-input": ""},
        #         'variant_patterns': {},
        #         'style_classes': {
        #             "placeholder:text-muted-foreground", "h-10", "py-3"
        #             "flex", "w-full", "rounded-md", "bg-transparent", "text-sm", "outline-hidden"
        #         }
        #     },
        #     config={
        #         'self_closing': True,
        #         'ignore_children': True,
        #         'output_blacklist': {
        #             "data-slot", "cmdk-input", "autocomplete", "autocorrect", "spellcheck",
        #             "aria-autocomplete", "role", "aria-expanded", "aria-controls",
        #             "aria-labelledby", "id", "type", "value", "placeholder" # placeholder might be needed
        #         }
        #     }
        # ),
        "CommandLabelIgnore": Component(
            name="CommandLabelIgnore",
            tag="label",
            match_pattern={
                'signature_classes': set(),
                'data_attributes': {"cmdk-label":""},
                'variant_patterns': {},
                'style_classes': set()
            },
            config={
                'self_closing': True,
                'ignore_children': True,
                'output_blacklist': {},
                'skip_this_element': True
            }
        ),
        "CommandList": Component(
            name="CommandList",
            tag="div", # Based on CommandPrimitive.List
            match_pattern={
                'signature_classes': {"overflow-x-hidden", "overflow-y-auto"},
                'data_attributes': {"cmdk-list": ""},
                'variant_patterns': {},
                'style_classes': {"max-h-[300px]", "scroll-py-1"}
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': {"data-slot", "cmdk-list", "role", "aria-label", "id", "style"} # style added
            }
        ),
        "CommandEmpty": Component(
            name="CommandEmpty",
            tag="div", # Based on CommandPrimitive.Empty
            match_pattern={
                'signature_classes': {"py-6", "text-center", "text-sm"},
                'data_attributes': {"data-slot": "command-empty"},
                'variant_patterns': {},
                'style_classes': set()
            },
            config={
                'self_closing': False, # Can contain text
                'ignore_children': False,
                'output_blacklist': {"data-slot", "cmdk-empty", "role"}
            }
        ),
        "CommandGroup": Component(
            name="CommandGroup",
            tag="div", # Based on CommandPrimitive.Group
            match_pattern={
                'signature_classes': {
                    "text-foreground", "overflow-hidden", "p-1",
                    "[&_[cmdk-group-heading]]:text-muted-foreground",
                    "[&_[cmdk-group-heading]]:px-2", "[&_[cmdk-group-heading]]:py-1.5",
                    "[&_[cmdk-group-heading]]:text-xs", "[&_[cmdk-group-heading]]:font-medium"
                },
                'data_attributes': {"data-slot": "command-group"},
                'variant_patterns': {},
                'style_classes': set()
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': {"data-slot", "cmdk-group", "role", "data-value"}
            }
        ),
        "CommandGroupLegacy": Component(
            name="CommandGroup",
            tag="div", # Based on CommandPrimitive.Group
            match_pattern={
                'signature_classes': set(),
                'data_attributes': {"cmdk-group-items": ""},
                'variant_patterns': {},
                'style_classes': set()
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': {"data-slot", "cmdk-group-items", "role", "data-value"}
            }
        ),
        "CommandSeparator": Component(
            name="CommandSeparator",
            tag="div", # Based on CommandPrimitive.Separator
            match_pattern={
                'signature_classes': {"bg-border", "-mx-1", "h-px"},
                'data_attributes': {"data-slot": "command-separator"},
                'variant_patterns': {},
                'style_classes': set()
            },
            config={
                'self_closing': True,
                'ignore_children': True,
                'output_blacklist': {"data-slot", "cmdk-separator", "role"}
            }
        ),
        "CommandItem": Component(
            name="CommandItem",
            tag="div", # Based on CommandPrimitive.Item
            match_pattern={
                'signature_classes': {                    
                    "data-[disabled=true]:pointer-events-none", "data-[disabled=true]:opacity-50",
                    "[&_svg]:pointer-events-none", "[&_svg]:shrink-0",
                    "[&_svg:not([class*='size-'])]:size-4",
                    "[&_svg:not([class*='text-'])]:text-muted-foreground",
                    "data-[selected=true]:bg-accent", "data-[selected=true]:text-accent-foreground"
                },
                'data_attributes': {"data-slot": "command-item"},
                'variant_patterns': {},
                'style_classes': {
                    "relative", "flex", "cursor-default", "items-center", "gap-2", "rounded-sm",
                    "px-2", "py-1.5", "text-sm", "outline-hidden", "select-none",
                }
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': {
                    "data-slot", "cmdk-item", "role", "aria-disabled", "aria-selected",
                    "data-disabled", "data-selected", "data-value", "id"
                }
            }
        ),
        "CommandItemLegacy": Component(
            name="CommandItem",
            tag="div", # Based on CommandPrimitive.Item
            match_pattern={
                'signature_classes': {                    
                    "data-[disabled=true]:pointer-events-none", "data-[disabled=true]:opacity-50",
                    "[&_svg]:pointer-events-none", "[&_svg]:shrink-0",
                    # "[&_svg:not([class*='size-'])]:size-4",
                    "[&_svg]:size-4",
                    # "[&_svg:not([class*='text-'])]:text-muted-foreground",
                    "data-[selected=true]:bg-accent", "data-[selected=true]:text-accent-foreground"
                },
                'data_attributes': {},
                'variant_patterns': {},
                'style_classes': {
                    "relative", "flex", "cursor-default", "items-center", "gap-2", "rounded-sm",
                    "px-2", "py-1.5", "text-sm", "outline-none", "select-none",
                }
            },
            config={
                'self_closing': False,
                'ignore_children': False,
                'output_blacklist': {
                    "data-slot", "cmdk-item", "role", "aria-disabled", "aria-selected",
                    "data-disabled", "data-selected", "data-value", "id"
                }
            }
        ),
        "CommandShortcut": Component(
            name="CommandShortcut",
            tag="span",
            match_pattern={
                'signature_classes': {"ml-auto", "text-xs", "tracking-widest"},
                'data_attributes': {"data-slot": "command-shortcut"},
                'variant_patterns': {},
                'style_classes': {"text-muted-foreground"}
            },
            config={
                'self_closing': False, # Contains text
                'ignore_children': False,
                'output_blacklist': {"data-slot"}
            }
        ),
    }
