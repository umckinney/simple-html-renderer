#!/usr/bin/env python3

"""
A class-based system for rendering HTML documents.
Each class represents an HTML element or tag with support for nested structure,
attributes, self-closing tags, and one-line content.
"""


class Element:
    """Base class for all HTML elements."""

    tag = "element"
    indent = 2

    def __init__(self, content=None, **attributes):
        """
        Initialize an HTML element.

        Args:
            content (str or Element, optional): Initial content of the tag.
            **attributes: Arbitrary keyword attributes for the tag.
        """
        self.content = [content] if content else []
        self.attributes = attributes
        self.attributes_string = " ".join(
            [f'{key}="{value}"' for key, value in attributes.items()]
        )

    def __str__(self):
        """Return a string representation of the tag and attributes."""
        string = f"{self.tag} {self.attributes_string}" if self.attributes else self.tag
        return string

    def append(self, new_content):
        """Append new content to the element."""
        self.content.append(new_content)

    def render(self, out_file, cur_indent=0):
        """
        Render the element and its content to the output file.

        Args:
            out_file (file-like): A writable file-like object.
            cur_indent (int): Current indentation level.
        """
        next_indent = cur_indent + self.indent
        out_file.write(" " * cur_indent)
        if self.attributes:
            out_file.write(f"<{self.tag} {self.attributes_string}>")
        else:
            out_file.write(f"<{self.tag}>")
        if self.content:
            out_file.write("\n")
        for i in self.content:
            try:
                i.render(out_file, next_indent)
                out_file.write("\n")
            except AttributeError:
                out_file.write(" " * next_indent)
                out_file.write(i)
                out_file.write("\n")
        if self.content:
            out_file.write(" " * cur_indent)
        out_file.write(f"</{self.tag}>")


class Html(Element):
    """HTML root element with <!DOCTYPE html> declaration."""

    tag = "html"
    doctype = "<!DOCTYPE html>"

    def render(self, out_file, cur_indent=0):
        out_file.write(" " * cur_indent)
        out_file.write(f"{self.doctype}")
        out_file.write("\n")
        super().render(out_file, cur_indent)


class Body(Element):
    """HTML <body> element."""

    tag = "body"


class P(Element):
    """HTML <p> (paragraph) element."""

    tag = "p"


class Head(Element):
    """HTML <head> element."""

    tag = "head"


class OneLineTag(Element):
    """Represents tags that should render content on a single line."""

    tag = "oneline"

    def render(self, out_file, cur_indent=0):
        next_indent = cur_indent + self.indent
        out_file.write(" " * cur_indent)
        if self.attributes:
            out_file.write(f"<{self.tag} {self.attributes_string}>")
        else:
            out_file.write(f"<{self.tag}>")
        for i in self.content:
            try:
                i.render(out_file, next_indent)
            except AttributeError:
                out_file.write(i)
        out_file.write(f"</{self.tag}>")


class Title(OneLineTag):
    """HTML <title> tag (single-line)."""

    tag = "title"


class SelfClosingTag(Element):
    """Represents self-closing tags like <hr /> or <br />."""

    tag = "selfclosing"

    def __init__(self, content=None, **attributes):
        if content:
            raise TypeError("You cannot pass in content for self closing tags.")
        super().__init__(None, **attributes)

    def render(self, out_file, cur_indent=0):
        out_file.write(" " * cur_indent)
        if self.attributes:
            out_file.write(f"<{self.tag} {self.attributes_string} />")
        else:
            out_file.write(f"<{self.tag} />")


class Hr(SelfClosingTag):
    """HTML <hr /> horizontal rule."""

    tag = "hr"


class Br(SelfClosingTag):
    """HTML <br /> line break."""

    tag = "br"


class A(Element):
    """HTML <a> (anchor) tag with href link."""

    tag = "a"

    def __init__(self, link, content=None, **attributes):
        """
        Initialize a hyperlink element.

        Args:
            link (str): The URL for the href attribute.
            content (str or Element): The visible text or nested element.
            **attributes: Additional HTML attributes.
        """
        self.link = link
        super().__init__(content, **attributes)

    def render(self, out_file, cur_indent=0):
        next_indent = cur_indent + self.indent
        out_file.write(" " * cur_indent)
        if self.attributes:
            out_file.write(f'<{self.tag} href="{self.link}" {self.attributes_string}>')
        else:
            out_file.write(f'<{self.tag} href="{self.link}">')
        for i in self.content:
            try:
                i.render(out_file, next_indent)
            except AttributeError:
                out_file.write(i)
        out_file.write(f"</{self.tag}>")


class Ul(Element):
    """HTML <ul> unordered list."""

    tag = "ul"


class Li(Element):
    """HTML <li> list item."""

    tag = "li"


class H(Element):
    """HTML <h1> to <h6> heading element."""

    tag = "h"

    def __init__(self, level, content=None, **attributes):
        """
        Initialize a heading tag (e.g., <h1>).

        Args:
            level (int): Heading level (1 to 6).
            content (str or Element): Heading content.
            **attributes: Additional HTML attributes.
        """
        self.tag = f"{self.tag}{level}"
        super().__init__(content=None, **attributes)


class Meta(SelfClosingTag):
    """HTML <meta /> tag for metadata."""

    tag = "meta"
