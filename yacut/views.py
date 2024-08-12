import random

from flask import flash, redirect, render_template

from . import app, db
from .constants import SHORT_ID_LENGTH, SYMBOLS
from .forms import URLMapForm
from .models import URLMap


def get_unique_short_id():
    while True:
        short_id = ''.join(random.choice(SYMBOLS) for _ in range(
            SHORT_ID_LENGTH))
        if URLMap.query.filter_by(short=short_id).first() is None:
            return short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    if not form.validate_on_submit():
        return render_template('index.html', form=form)
    custom_id = form.custom_id.data
    if not custom_id:
        custom_id = get_unique_short_id()
    elif URLMap.query.filter_by(short=custom_id).first() is not None:
        flash('Предложенный вариант короткой ссылки уже существует.',
              'link-taken')
        return render_template('index.html', form=form)
    new_url = URLMap(
        original=form.original_link.data,
        short=custom_id
    )
    db.session.add(new_url)
    db.session.commit()
    return render_template('index.html', url=new_url, form=form)


@app.route('/<short_id>')
def redirect_link(short_id):
    db_object = URLMap.query.filter_by(short=short_id).first_or_404()
    original_link = db_object.original
    return redirect(original_link)
