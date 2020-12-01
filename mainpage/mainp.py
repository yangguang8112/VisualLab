from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

#from mainpage.db import get_db
from mainpage.database import db_session
from mainpage.models import User, RawData

bp = Blueprint('mainp', __name__)


@bp.route('/')
def index():
    '''
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    '''
    posts=None
    return render_template('index.html', posts=posts)

@bp.route('/ztron_upload', methods=['POST'])
def ztron_upload():
    data = request.json
    print(data)
    return "hahhh"
