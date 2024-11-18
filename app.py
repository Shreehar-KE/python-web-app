from db import init_db
from server import run_server

# Entry point for the application. Initializes the database and starts the server.
if __name__ == "__main__":
    init_db()
    print("Starting the Note-Taking App.")
    run_server()
