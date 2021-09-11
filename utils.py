from pathlib import Path
from database import Database, Note
from typing import List


def load_database() -> Database:
    return Database("banco")

def extract_route(request: str) -> str:
    route = request.split("\n")[0].split()[1]

    return route[1:]

def read_file(path: Path) -> str:
    for suffix in ["*.txt", "*.html", "*.css", "*.js"]:
        if path.match(suffix): return path.read_text().encode("utf-8")
    
    return path.read_bytes()

def build_response(body: str = '', code: int = 200, reason: str = 'OK', headers: str = ''):
    if headers != '': return f"HTTP/1.1 {code} {reason}\n{headers}\n\n{body}".encode()
    
    return f"HTTP/1.1 {code} {reason}\n\n{body}".encode()

def load_data(database: Database) -> List[Note]:
    return database.get_all()

def add_note(database: Database, title: str, content: str) -> None:
    new_note = Note(0, title, content)
    database.add(new_note)

def remove_note(database: Database, note_id: int) -> None:
    database.delete(note_id)

def load_template(file_name: str) -> str:
    file = Path(f"client/{file_name}")
    return file.read_text()

