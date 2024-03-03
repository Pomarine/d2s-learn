from flask import Flask

from index import index
from login import login
from logout import logout
from home import home
from ball import ball


app = Flask(__name__, static_folder='../frontend/static')

app.app_context().push()

app.register_blueprint(index)
app.register_blueprint(login)
app.register_blueprint(logout)
app.register_blueprint(home)
app.register_blueprint(ball)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
