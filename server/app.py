# -*- coding: utf-8 -*-

from flask import Flask
from database.db import initialize_db
from flask_restful import Api
from resources.routes import initialize_routes

app = Flask(__name__)
api = Api(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/notes'
}

initialize_db(app)
initialize_routes(api)

if __name__ == "__main__":
    app.run()