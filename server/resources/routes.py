from .note import NoteListApi, NoteApi

def initialize_routes(api):
    api.add_resource(NoteListApi, '/api/notes')
    api.add_resource(NoteApi, '/api/notes/<id>')