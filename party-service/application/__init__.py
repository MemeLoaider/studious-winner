from flask import Flask
from flask_sqlalchemy import SQLAlchemy


#global variables
db = SQLAlchemy()


def init_app():
    """Initializing core Flask application"""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.LocalConfig')


    #Init plugins
    db.init_app(app)


    with app.app_context():
        from . import party


        #Registering blueprints
        app.register_blueprint(party.party_bp)


        #Running init_db.sql script
        with app.open_resource('init_db.sql') as sql_file:
            list_of_commands = sql_file.read().decode('utf8').strip().split(";")
            for command in list_of_commands[:-1]:
                db.engine.execute(command)


        return app

