from http.server import BaseHTTPRequestHandler, HTTPServer
import views


class RequestHandler(BaseHTTPRequestHandler):
    """Custom RequestHandler to handle HTTP requests and routing"""

    def do_GET(self):
        """Handles GET requests"""
        if self.path == '/':
            views.display_home_page(self)
        elif self.path == '/add_note':
            views.display_add_note_form(self)
        elif self.path == '/view_notes':
            views.display_notes(self)
        else:
            self.send_error(404, "Page not found")

    def do_POST(self):
        """Handles POST requests"""
        if self.path == '/add_note':
            views.handle_add_note(self)


def run_server():
    """start the HTTP server on localhost and port 8080"""
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    print("Server running on http://localhost:8080")
    httpd.serve_forever()
