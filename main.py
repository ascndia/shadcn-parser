from bs4 import BeautifulSoup, Tag, Doctype
from components import Component, Variant, ComponentAdapter
from typing import Dict, Tuple, Optional
from registry import COMPONENTS
from converter import JSXConverter

converter = JSXConverter(COMPONENTS)

def main():
    html_input = """
    <div>
        <h1>Welcome</h1>
        <img src='images/input_image.png' alt='Example Image'>
    </div>
    """
    jsx_output = converter.convert(html_input)
    print(jsx_output)

if __name__ == "__main__":
    main()