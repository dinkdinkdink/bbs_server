from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
)
from routes import *

main = Blueprint('setting', __name__)


@main.route("/")
def index():
    u = current_user()
    return render_template("setting.html", user=u)

