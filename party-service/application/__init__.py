from flask import Flask, Response, jsonify
from flask_sqlalchemy import SQLAlchemy
from logging.config import dictConfig


#global variables
db = SQLAlchemy()


#Configuring logging
dictConfig({
    'version': 1,
    'root': {
        'level': 'INFO'
    }
})


def prepare_json_response(json_body:dict, status_code:int) -> Response:
    """Prepares a json flask response with given <json_body> as dictionary and <status_code>"""
    response_to_return = jsonify(json_body)
    response_to_return.status_code = status_code
    return response_to_return


def init_app():
    """Initializing core Flask application"""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.LocalConfig')

    #Init plugins
    db.init_app(app)

    with app.app_context():
        from .party import routes

        #Registering blueprints
        app.register_blueprint(routes.party_bp)

        #Running init_db.sql script
        with app.open_resource('init_db.sql') as sql_file:
            list_of_commands = sql_file.read().decode('utf8').strip().split(";")
            #Making a slice of commands because the last command is empty
            for command in list_of_commands[:-1]:
                db.engine.execute(command)

        return app

