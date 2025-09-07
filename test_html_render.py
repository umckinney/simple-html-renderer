"""
test code for html_render.py
"""

import io

# import * is often bad form, but makes it easier to test everything in a module.
from html_render import *


def render_result(element, ind=""):
    """
    calls the element's render method, and returns what got rendered as a
    string
    """
    outfile = io.StringIO()
    if ind:
        element.render(outfile, ind)
    else:
        element.render(outfile)
    print(f"render_result from test = {outfile.getvalue()}")
    return outfile.getvalue()


########
# Step 1
########


def test_init():
    """
    This only tests that it can be initialized with and without
    some content -- but it's a start
    """
    e = Element()

    e = Element("this is some text")


def test_append():
    """
    This tests that you can append text

    It doesn't test if it works --
    that will be covered by the render test later
    """
    e = Element("this is some text")
    e.append("some more text")


def test_render_element():
    """
    Tests whether the Element can render two pieces of text
    So it is also testing that the append method works correctly.

    It is not testing whether indentation or line feeds are correct.
    """
    e = Html("this is some text")
    e.append("and this is some more text")

    # This uses the render_results utility above
    file_contents = render_result(e).strip()
    print(f"file_contents in test_render_element is {file_contents}")

    # making sure the content got in there.
    assert ("this is some text") in file_contents
    assert ("and this is some more text") in file_contents

    # make sure it's in the right order
    assert file_contents.index("this is") < file_contents.index("and this")

    # making sure the opening and closing tags are right.
    assert file_contents.startswith("<!DOCTYPE html>")
    assert file_contents.endswith("</html>")


def test_render_element2():
    """
    Tests whether the Element can render two pieces of text
    So it is also testing that the append method works correctly.

    It is not testing whether indentation or line feeds are correct.
    """
    e = Html()
    e.append("this is some text")
    e.append("and this is some more text")

    file_contents = render_result(e).strip()
    print(f"file_contents in test_render_element2 is {file_contents}")

    assert ("this is some text") in file_contents
    assert ("and this is some more text") in file_contents

    assert file_contents.index("this is") < file_contents.index("and this")

    assert file_contents.startswith("<!DOCTYPE html>")
    assert file_contents.endswith("</html>")


# ########
# # Step 2
# ########


def test_html():
    e = Html("this is some text")
    e.append("and this is some more text")

    file_contents = render_result(e).strip()

    assert ("this is some text") in file_contents
    assert ("and this is some more text") in file_contents
    print(file_contents)
    assert file_contents.endswith("</html>")


def test_body():
    e = Body("this is some text")
    e.append("and this is some more text")

    file_contents = render_result(e).strip()

    assert ("this is some text") in file_contents
    assert ("and this is some more text") in file_contents

    assert file_contents.startswith("<body>")
    assert file_contents.endswith("</body>")


def test_p():
    e = P("this is some text")
    e.append("and this is some more text")

    file_contents = render_result(e).strip()

    assert ("this is some text") in file_contents
    assert ("and this is some more text") in file_contents

    assert file_contents.startswith("<p>")
    assert file_contents.endswith("</p>")


def test_sub_element():
    """
    tests that you can add another element and still render properly
    """
    page = Html()
    page.append("some plain text.")
    page.append(P("A simple paragraph of text"))
    page.append("Some more plain text.")

    file_contents = render_result(page)
    print(file_contents)

    assert "some plain text" in file_contents
    assert "A simple paragraph of text" in file_contents
    assert "Some more plain text." in file_contents
    assert "some plain text" in file_contents
    assert "<p>" in file_contents
    assert "</p>" in file_contents


########
# Step 3
########


def test_head():
    e = Head("this is the head")
    e.append(Title("this is the title"))

    file_contents = render_result(e).strip()

    assert ("this is the head") in file_contents
    assert ("this is the title") in file_contents

    assert file_contents.startswith("<head>")
    assert file_contents.endswith("</head>")

    assert file_contents.index("head") < file_contents.index("title")
    assert file_contents.index("title") < file_contents.index("/title")
    assert file_contents.index("/title") < file_contents.index("/head")


########
# Step 4
########
def test_attributes():
    test_attributes = {
        "id": "1",
        "size": 400,
        "color": "orange",
    }
    e = P("This is a paragraph", **test_attributes)

    file_contents = render_result(e).strip()

    assert ('id="1"') in file_contents
    assert ('size="400"') in file_contents
    assert ('color="orange"') in file_contents


########
# Step 5
########
def test_hr():
    e = Hr()

    file_contents = render_result(e).strip()

    assert ("<hr />") in file_contents


def test_br():
    test_attributes = {
        "id": "5",
        "happy": "go lucky",
    }
    e = Br(**test_attributes)

    file_contents = render_result(e).strip()
    print(f"br test file contents = {file_contents}")

    assert ('<br id="5" happy="go lucky" />') in file_contents


########
# Step 6
########
def test_a():
    e = A("www.google.com", "Google Away!")

    file_contents = render_result(e).strip()
    print(f"file_contents for test_a = {file_contents}")
    assert ('<a href="www.google.com">Google Away!</a>') in file_contents


########
# Step 7
########
def test_ul_li():
    e = Ul()
    e.append(Li("first"))
    e.append(Li("second"))

    file_contents = render_result(e).strip()

    assert ("<ul>") in file_contents
    assert ("</ul") in file_contents
    assert ("<li>") in file_contents
    assert ("</li>") in file_contents
    assert file_contents.index("ul") < file_contents.index("li")
    assert file_contents.index("ul") < file_contents.index("/li")
    assert file_contents.index("ul") < file_contents.index("/ul")
    assert file_contents.index("li") < file_contents.index("first")
    assert file_contents.index("li") < file_contents.index("second")
    assert file_contents.index("li") < file_contents.index("/li")
    assert file_contents.index("li") < file_contents.index("/ul")
    assert file_contents.index("first") < file_contents.index("/li")
    assert file_contents.index("first") < file_contents.index("second")
    assert file_contents.index("first") < file_contents.index("/ul")
    assert file_contents.index("second") < file_contents.index("/ul")


########
# Step 8
########
def test_h():
    e = Body()
    e.append(H(1, "this is an H1"))
    e.append(H(2, "this is an H2"))

    file_contents = render_result(e).strip()
    assert ("<h1>") in file_contents
    assert ("<h2>") in file_contents
    assert file_contents.index("<h1>") < file_contents.index("<h2>")


def test_meta():
    e = Meta(**{"charset": "UTF-8"})

    file_contents = render_result(e).strip()
    print(f"test_meta file_contents = {file_contents}")

    assert ('<meta charset="UTF-8" />') in file_contents


#####################
# indentation testing
#####################


def test_indent():
    """
    Tests that the indentation gets passed through to the renderer
    """
    html = P("some content")
    file_contents = render_result(html, ind=3).rstrip()  # remove the end newline

    print("********")
    print("********")
    print(f"test_indent file_content = \n{file_contents}")
    lines = file_contents.split("\n")
    print("********")
    print("********")
    print(f"lines[0] = \n{lines[0]}")
    assert lines[0].startswith("   <")
    print("********")
    print("********")
    print(f"lines[-1] = \n{lines[-1]}")
    print("********")
    print("********")
    assert lines[-1].startswith("   <")


def test_indent_contents():
    """
    The contents in a element should be indented more than the tag
    by the amount in the indent class attribute
    """
    html = Html("some content")
    file_contents = render_result(html, ind=0)

    print(f"file_contents from test_indent_contents = \n{file_contents}")
    print(f"indent value from Element class = \n{Element().indent}")
    lines = file_contents.split("\n")
    print(f"lines[1] is {lines[1]}")
    print(f"lines[2] is {lines[2]}")
    assert lines[2].startswith(Element().indent * " ")


def test_multiple_indent():
    """
    make sure multiple levels get indented fully
    """
    body = Body()
    body.append(P("some text"))
    html = Html(body)

    file_contents = render_result(html)

    print(f"file_contents from test_multiple_indent = \n{file_contents}")
    lines = file_contents.split("\n")
    for i in range(3):  # this needed to be adapted to the <DOCTYPE> tag
        assert lines[i + 1].startswith(i * (Element().indent * " ") + "<")

    assert lines[4].startswith(3 * (Element().indent * " ") + "some")


def test_element_indent1():
    """
    Tests whether the Element indents at least simple content

    we are expecting to to look like this:

    <html>
        this is some text
    </html>

    More complex indentation should be tested later.
    """
    e = Element("this is some text")
    file_contents = render_result(e).strip()
    assert ("this is some text") in file_contents

    lines = file_contents.split("\n")
    assert lines[0] == "<element>"
    assert lines[1].startswith((Element().indent * " ") + "thi")
    assert lines[2] == "</element>"
    assert file_contents.endswith("</element>")
