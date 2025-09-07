# Simple HTML Renderer

![Python](https://img.shields.io/badge/python-3.12%2B-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Last Commit](https://img.shields.io/github/last-commit/umckinney/simple-html-renderer)
![Repo Size](https://img.shields.io/github/repo-size/umckinney/simple-html-renderer)

This project provides a class-based system for rendering HTML programmatically using Python.  
It supports element nesting, attributes, self-closing tags, and inline vs. block-level elements.

## Features

- HTML tag rendering with indentation
- Element content and attribute handling
- Support for self-closing tags (e.g., `br`, `hr`, `meta`)
- Specialized subclasses for common HTML tags (`Html`, `Body`, `P`, `Title`, etc.)
- Link and header tag rendering
- Readable, testable architecture with class-based design

## Getting Started

To render an HTML structure, create instances of HTML elements and nest them using `.append()`.

Example:
```python
from html_render import Html, Body, P

page = Html()
body = Body()
body.append(P("Hello, world!"))
page.append(body)

with open("output.html", "w") as f:
    page.render(f)
```

## Running Tests

Run the included tests with:
```bash
pytest test_html_render.py
```

## License

This project is licensed under the MIT License.
