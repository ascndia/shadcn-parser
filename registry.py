from components import Component, ComponentAdapter
from typing import Dict, Tuple, Optional
from tailwind_merge import TailwindMerge

COMPONENTS = {
        "Button": Component(
            name="Button",
            tag="button",
            core_classes={
                # Immutable identity classes (never customized)
                "ring-offset-background", 
                "focus-visible:outline-none", "focus-visible:ring-2",
                "disabled:pointer-events-none", "disabled:opacity-50",
                "[&_svg]:pointer-events-none", "[&_svg]:size-4",
                "focus-visible:ring-ring",
                "focus-visible:ring-offset-2", "[&_svg]:shrink-0",
            },
            variant_map={
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
            style_classes={
                # Default styles that can be customized/overridden
                "rounded-md", "text-sm", "font-medium",
                "gap-2", "whitespace-nowrap", "transition-colors",
                "inline-flex", "items-center", "justify-center",
            },
            # default_variant={"variant": "default", "size": "default"}
        ),
        "Badge": Component(
            name="Badge",
            tag="span",
            core_classes={
                "transition-[color,box-shadow]",
                "focus-visible:ring-[3px]",
                "focus-visible:border-ring", "focus-visible:ring-ring/50",
                "aria-invalid:ring-destructive/20", "aria-invalid:border-destructive",
                "dark:aria-invalid:ring-destructive/40",
                "[&>svg]:pointer-events-none", "[&>svg]:size-3",
            },
            variant_map={
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
            style_classes={
                "w-fit", "shrink-0", "overflow-hidden",
                "inline-flex", "items-center", "justify-center", "gap-1",
                "rounded-md", "border", "px-2", "py-0.5",
                "text-xs", "font-medium", "whitespace-nowrap"
            },
            ignore_attrs={"data-slot"},
            # default_variant={
            #     "variant": "default"
            # }
        ),
        "Separator": Component(
            name="Separator",
            tag="div",  # Radix `SeparatorPrimitive.Root` renders a div by default
            core_classes={
                "shrink-0",
                "bg-border",
            },
            variant_map={
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
            config={
                'ignore_classes': {
                    "data-[orientation=horizontal]:h-px",
                    "data-[orientation=horizontal]:w-full",
                    "data-[orientation=vertical]:w-px",
                    "data-[orientation=vertical]:h-full"
                },
            },
            style_classes=set(),  # Not really customizable styles in this one
            # default_variant={
            #     "orientation": "horizontal"
            # },
            ignore_attrs={"role", "data-orientation", "data-slot"}
        ),
        "Card": Component(
            name="Card",
            tag="div",
            core_classes={
                "rounded-xl", "border", "bg-card", "text-card-foreground", "shadow"
            },
            variant_map={},  # No dynamic variants
            style_classes=set(),
        ),
        "CardHeader": Component(
            name="CardHeader",
            tag="div",
            core_classes={
                "flex", "flex-col", "space-y-1.5", "p-6"
            },
            variant_map={},
            style_classes=set(),
        ),
        "CardTitle": Component(
            name="CardTitle",
            tag="div",
            core_classes={
                "font-semibold", "leading-none", "tracking-tight"
            },
            variant_map={},
            style_classes=set(),
        ),
        "CardDescription": Component(
            name="CardDescription",
            tag="div",
            core_classes={
                "text-sm", "text-muted-foreground"
            },
            variant_map={},
            style_classes=set(),
        ),
        "CardContent": Component(
            name="CardContent",
            tag="div",
            core_classes={
                "p-6", "pt-0"
            },
            variant_map={},
            style_classes=set(),
        ),
       "CardFooter": Component(
            name="CardFooter",
            tag="div",
            core_classes={
                "flex", "items-center", "p-6", "pt-0"
            },
            variant_map={},
            style_classes=set(),
        ),
        "Input": Component(
            name="Input",
            tag="input",
            core_classes={
                "flex", "w-full", "min-w-0", "outline-none", "bg-transparent",
                "file:text-foreground", "file:inline-flex", "file:h-7", "file:border-0",
                "file:bg-transparent", "file:text-sm", "file:font-medium",
                "disabled:pointer-events-none", "disabled:cursor-not-allowed", "disabled:opacity-50",
                "selection:bg-primary", "selection:text-primary-foreground",
            },
            style_classes={
                "h-9", "rounded-md", "border", "border-input", "px-3", "py-1",
                "text-base", "md:text-sm", "placeholder:text-muted-foreground",
                "shadow-xs", "transition-[color,box-shadow]",
                "focus-visible:border-ring", "focus-visible:ring-ring/50", "focus-visible:ring-[3px]",
                "aria-invalid:border-destructive", "aria-invalid:ring-destructive/20", "dark:aria-invalid:ring-destructive/40",
                "dark:bg-input/30",
            },
            variant_map={},  # no built-in variants in shadcn's Input
            # default_variant={}
            ignore_attrs={"data-slot"},
        ),
        "LucideIcon": Component(
            name="LucideIcon",
            tag="svg",
            core_classes={"lucide"},
            variant_map={},
            style_classes=set(),
            ignore_attrs={
                "xmlns", "stroke", "fill", "viewbox", "aria-hidden",
                "focusable", "width", "height", "stroke-width", "color",
                "xmlns:xlink", "xlink:href", "xlink:show", "xlink:title",
                "xlink:role", "stroke-linecap", "stroke-linejoin"
            },
            config={
                'self_closing': True,
                'ignore_children': True,  # Prevents rendering inner SVG paths
                'preserve_size': True     # Automatically handles size via className
            }
        ),
        "Label": Component(
            name="Label",
            tag="label",
            core_classes={
                "leading-none", "select-none",
                "group-data-[disabled=true]:pointer-events-none",
                "group-data-[disabled=true]:opacity-50",
                "peer-disabled:cursor-not-allowed",
                "peer-disabled:opacity-50"
            },
            style_classes={"gap-2", "font-medium", "text-sm", "items-center", "flex"},  # could optionally move "gap-2", "text-sm", etc. here if you want to allow override
            variant_map={},        # no built-in variants
            # default_variant={}
        ),
    }
        