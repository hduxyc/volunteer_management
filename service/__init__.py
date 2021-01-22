from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__,
            template_folder='./templates',
            static_folder='./templates/static')

bootstrap = Bootstrap(app)

from service.apis import *
from service.views import *
