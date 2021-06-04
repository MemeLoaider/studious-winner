def Settings(**kwargs):
    return {
        'interpeter_path': './env/bin/python',
        'sys_path' : [
            './env/lib/python3.9/site-packages/flask',
            './env/lib/python3.9/site-packages/flask_sqlalchemy',
            './env/lib/python3.9/site-packages/SQLAlchemy-1.4.17.dist-info'
        ]
    }
