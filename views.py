from utils import load_data, load_template, build_response, add_note, remove_note
from urllib.parse import unquote_plus
from database import Database

def index(request: str, database: Database):
    response = build_response()

    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST'):
        response = build_response(code=303, reason='See Other', headers='Location: /')
        
        request = request.replace('\r', '') 

        partes = request.split('\n\n')
        corpo = partes[1]

        if "delete" in request:
            note_id = int(corpo[7:])

            remove_note(database, note_id)
        else:
            params = {}

            for chave_valor in corpo.split('&'):
                chave = unquote_plus(chave_valor.split('=')[0])
                valor =  unquote_plus(chave_valor.split('=')[1])
                params[chave] = valor

            add_note(database, params["title"], params["content"])
        
    note_template = load_template('components/note.html')
    notes = [
        note_template.format(title=dados.title, content=dados.content, id=dados.id)
        for dados in load_data(database)
    ]
    notes = '\n'.join(notes)


    return response + load_template('index.html').format(notes=notes).encode()
