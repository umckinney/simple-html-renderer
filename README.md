# simple-html-renderer

A Python-based HTML rendering engine built from scratch using object-oriented principles.

This educational project demonstrates how to construct a tree-like DOM structure and serialize it to HTML. It supports tags, attributes, inline text, indentation, and even self-closing tags.

## Features

- 🏗️ Compose HTML using Python classes like `Html`, `Body`, `P`, `Head`, etc.
- 🧱 Nest elements with parent-child relationships
- 📝 Add attributes and text content dynamically
- 📄 Render well-structured and indented HTML
- 🚫 Handle self-closing tags like `<br />` and `<hr />`
- 💡 Demonstrates use of `__str__`, `__repr__`, and `__call__` methods

## Example Usage

```python
html = Html()
body = Body()
body.append(P("This is a paragraph."))
html.append(body)

render(html, output_file)
```

This would produce:

```html
<html>
    <body>
        <p>This is a paragraph.</p>
    </body>
</html>
```

## Educational Objectives

- Understand and implement magic methods like `__init__`, `__str__`, `__repr__`, and `__call__`
- Practice clean OOP design with base and subclass structures
- Reinforce the concept of recursive rendering and indentation
- Prepare for more complex HTML templating and rendering patterns

## How to Run

1. Clone the repo or download the folder.
2. Run any of the included test scripts (`test_render.py`) to validate functionality.
3. Edit or extend the class hierarchy to experiment with your own tags.

## File Structure

- `html_render.py` — main rendering engine
- `test_render.py` — unit tests
- `README.md` — this file

## License

MIT License.
