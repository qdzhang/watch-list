from flask import render_template

from watchlist import app
from watchlist.models import User


@app.errorhandler(404)
def page_not_found(e):  # 接受异常对象作为参数
    user = User.query.first()
    return render_template('404.html'), 404