from components import Component, Variant, ComponentAdapter
from typing import Dict, Tuple, Optional

COMPONENTS = {
        "Button": ComponentAdapter.from_cva(
            name="Button",
            tag="button",
            cva_config={
                "base_classes": """
                    inline-flex items-center justify-center gap-2 whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0
                """,
                "variants": {
                    "variant": {
                        "default": "bg-primary text-primary-foreground hover:bg-primary/90",
                        "destructive": "bg-destructive text-destructive-foreground hover:bg-destructive/90",
                        "outline": "border border-input bg-background hover:bg-accent hover:text-accent-foreground",
                        "secondary": "bg-secondary text-secondary-foreground hover:bg-secondary/80",
                        "ghost": "hover:bg-accent hover:text-accent-foreground",
                        "link": "text-primary underline-offset-4 hover:underline"
                    },
                    "size": {
                        "default": "h-10 px-4 py-2 rounded-md",
                        "sm": "h-9 px-3 rounded-md",
                        "lg": "h-11 px-8 rounded-md",
                        "icon": "h-10 w-10 rounded-md"
                    }
                },
                "default_variant": "default"
            }
        ),
        "Badge": ComponentAdapter.from_cva(
            name="Badge",
            tag="span",
            cva_config={
                "base_classes": """
                    inline-flex items-center justify-center rounded-md border px-2 py-0.5 text-xs font-medium w-fit whitespace-nowrap shrink-0 [&>svg]:size-3 gap-1 [&>svg]:pointer-events-none focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px] aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive transition-[color,box-shadow] overflow-hidden
                """,
                "variants": {
                    "variant": {
                        "default": "border-transparent bg-primary text-primary-foreground [a&]:hover:bg-primary/90",
                        "secondary": "border-transparent bg-secondary text-secondary-foreground [a&]:hover:bg-secondary/90",
                        "destructive": "border-transparent bg-destructive text-white [a&]:hover:bg-destructive/90 focus-visible:ring-destructive/20 dark:focus-visible:ring-destructive/40 dark:bg-destructive/60",
                        "outline": "text-foreground [a&]:hover:bg-accent [a&]:hover:text-accent-foreground"
                    }
                },
                "default_variant": "default"
            },
            ignore_attrs={"data-slot"}
        ),
        "Card": ComponentAdapter.from_base(
            name="Card",
            tag="div",
            base_classes="rounded-xl border bg-card text-card-foreground shadow"
        ),
        "CardHeader": ComponentAdapter.from_base(
            name="CardHeader",
            tag="div",
            base_classes="flex flex-col space-y-1.5 p-6"
        ),
        "CardTitle": ComponentAdapter.from_base(
            name="CardTitle",
            tag="div",
            base_classes="font-semibold leading-none tracking-tight"
        ),
        "CardDescription": ComponentAdapter.from_base(
            name="CardDescription",
            tag="div",
            base_classes="text-sm text-muted-foreground"
        ),
        "CardContent": ComponentAdapter.from_base(
            name="CardContent",
            tag="div",
            base_classes="p-6 pt-0"
        ),
        "CardFooter": ComponentAdapter.from_base(
            name="CardFooter",
            tag="div",
            base_classes="flex items-center p-6 pt-0"
        ),
        "Input": ComponentAdapter.from_base(
            name="Input",
            tag="input",
            base_classes="file:text-foreground placeholder:text-muted-foreground selection:bg-primary selection:text-primary-foreground dark:bg-input/30 border-input flex h-9 w-full min-w-0 rounded-md border bg-transparent px-3 py-1 text-base shadow-xs transition-[color,box-shadow] outline-none file:inline-flex file:h-7 file:border-0 file:bg-transparent file:text-sm file:font-medium disabled:pointer-events-none disabled:cursor-not-allowed disabled:opacity-50 md:text-sm focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px] aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive",
            ignore_attrs={"data-slot"}
        ),
        "Label": ComponentAdapter.from_base(
            name="Label",
            tag="label",
            base_classes="flex items-center gap-2 text-sm leading-none font-medium select-none group-data-[disabled=true]:pointer-events-none group-data-[disabled=true]:opacity-50 peer-disabled:cursor-not-allowed peer-disabled:opacity-50"
        ),
        "Separator": ComponentAdapter.from_base(
            name="Separator",
            tag="div",
            base_classes="bg-border shrink-0 data-[orientation=horizontal]:h-px data-[orientation=horizontal]:w-full data-[orientation=vertical]:h-full data-[orientation=vertical]:w-px",
            ignore_attrs={"role", "data-orientation", "data-slot"}
        ),
        "LucideIcon": ComponentAdapter.from_base(
            name="LucideIcon",
            tag="svg",
            base_classes="lucide",
            ignore_attrs={"xmlns", "stroke", "fill", "viewbox", "aria-hidden", "focusable", "width", "height", "stroke-width", "color", "xmlns:xlink", "xlink:href", "xmlns:xlink", "xlink:show", "xlink:title", "xlink:role", "viewbox", "stroke-linecap", "stroke-linejoin"},
            self_closing=True  
        )
    }
        