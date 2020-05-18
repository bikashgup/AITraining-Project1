from ...ISEAR_app import ISEAR_app
from ..experiments import experiment1

@ISEAR_app.route('/')
@ISEAR_app.route('/index')
def index():
    experiment1.experiment1()
    return "Hello, World!"