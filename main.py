from bs4 import BeautifulSoup, Tag, Doctype
from components import Component, Variant, ComponentAdapter
from typing import Dict, Tuple, Optional
from registry import COMPONENTS
from converter import JSXConverter

converter = JSXConverter(COMPONENTS)

html_input="""
<button class="inline-flex items-center justify-center gap-2 whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 [&amp;_svg]:pointer-events-none [&amp;_svg]:size-4 [&amp;_svg]:shrink-0 hover:bg-accent hover:text-accent-foreground h-10 px-4 py-2 custom-class">Login</button>"""
print(converter.convert(html_input))