from ...ISEAR_app import ISEAR_app
from ..experiments.experiment2 import experiment2

@ISEAR_app.route('/')
@ISEAR_app.route('/index')
def index():
    experiment2.experiment2()
    return "Hello, World!"