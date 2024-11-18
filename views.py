from urllib.parse import parse_qs
import db


def display_home_page(handler):
    """Renders the home page"""
    handler.send_response(200)
    handler.send_header("Content-type", "text/html")
    handler.end_headers()
    with open("templates/home.html", "r") as file:
        handler.wfile.write(file.read().encode())


def display_add_note_form(handler):
    """Renders the form page for adding a new note."""
    handler.send_response(200)
    handler.send_header("Content-type", "text/html")
    handler.end_headers()
    with open("templates/add_note.html", "r") as file:
        handler.wfile.write(file.read().encode())


def handle_add_note(handler):
    """Handles the POST form submission for adding a note """
    content_length = int(handler.headers['Content-Length'])
    post_data = handler.rfile.read(content_length)
    data = parse_qs(post_data.decode())
    title = data['title'][0]
    content = data['content'][0]

    db.add_note_to_db(title, content)

    handler.send_response(302)
    # Redirect to view all notes after adding.
    handler.send_header("Location", "/view_notes")
    handler.end_headers()


def display_notes(handler):
    """Renders all the saved notes"""
    handler.send_response(200)
    handler.send_header("Content-type", "text/html")
    handler.end_headers()

    notes = db.get_all_notes()
    notes_html = "".join(
        [f"<h3>{title}</h3><p>{content}</p><hr>" for title, content in notes]
    )

    with open("templates/view_notes.html", "r") as file:
        html_content = file.read()

    # Inject the notes_html into the template for dynamic content display.
    html_content = html_content.replace("{{notes_content}}", notes_html)

    handler.wfile.write(html_content.encode())
