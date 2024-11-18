# 📝 Note-Taking App

A lightweight, minimalistic note-taking web application built from scratch using only Python’s built-in modules. This project emphasizes understanding **core web development concepts** without relying on frameworks.

## 🚀 Features
- **Add Notes**: Create and save notes with a title and content.
- **View Notes**: Display all saved notes in a readable format.
- **Database**: Persistent storage using SQLite3 for easy data management.
- **Core Concepts**: Manages HTTP requests, routing, and database operations without any frameworks.

## 📂 Project Structure
```plaintext
.
├── app.py                # Entry point of the application
├── server.py             # Handles HTTP server and request routing
├── views.py              # Renders pages and processes requests
├── db.py                 # Database connection and queries
├── templates/            # HTML templates for rendering pages
│   ├── home.html         # Home page with navigation links
│   ├── add_note.html     # Form to add a new note
│   └── view_notes.html   # Displays all saved notes
├── notes.sqlite3         # SQLite3 database file (auto-created)
└── README.md             # Project documentation
```
## 💡 Key Concepts
- **Core HTTP Handling**: Used Python’s http.server module for handling requests and serving pages.
- **Dynamic Content Rendering**: Injected dynamic content (notes) into HTML templates using Python.
- **Manual Routing**: Implemented custom request routing logic to handle different endpoints.
- **SQLite3 Integration**: Handled database connections, table creation, and Create, Read operations manually.

## 🛠️ Technologies Used
- **Python Modules:**
  - http.server - For handling HTTP requests.
  - sqlite3 - For database operations.
  - os - For file existence checks.
  - urllib.parse - For parsing POST data.
- **SQLite3** - Lightweight database for persistent storage.

## 📋 Instructions to run the project locally.
1. Clone the Repository
```bash
git clone https://github.com/Shreehar-KE/python-web-app.git
cd note-taking-app
```
2. Run the Application
```bash
python3 app.py
```
The app will start running at:
http://localhost:8080

## 🧠 Why Build This?
Frameworks like Django and Flask are powerful but often abstract away core concepts. This project is an effort to:
- Strengthen the understanding of HTTP servers, manual routing, and database integration.
- Appreciate the foundational principles that frameworks are built upon.
- Encourage learning why things work instead of just focusing on how to use a framework.