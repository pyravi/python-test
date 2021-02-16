import os

from app import create_app

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)


if __name__ == '__main__':
    '''
    https://www.digitalocean.com/community/tutorials/build-a-crud-web-app-with-python-and-flask-part-one

    https://www.nintyzeros.com/2019/11/flask-mysql-crud-restful-api.html
    '''
    app.run()