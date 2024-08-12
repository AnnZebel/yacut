import re
from http import HTTPStatus

from flask import request, jsonify

from . import app, db
from .error_handlers import APIErrors
from .models import URLMap
from .constants import LINK_REG
from .views import get_unique_short_id


@app.route('/api/id/', methods=['POST'])
def create_short_link():
    data = request.get_json(silent=True)
    if not data:
        raise APIErrors('Отсутствует тело запроса', HTTPStatus.BAD_REQUEST)
    if 'url' not in data:
        raise APIErrors('\"url\" является обязательным полем!',
                        HTTPStatus.BAD_REQUEST)

    custom_id = data.get('custom_id')
    if custom_id:
        if URLMap.query.filter_by(short=custom_id).first() is not None:
            raise APIErrors('Предложенный вариант короткой ссылки '
                            'уже существует.')
        if custom_id == '' or custom_id is None:
            custom_id = get_unique_short_id()
        elif not re.match(LINK_REG, custom_id):
            raise APIErrors('Указано недопустимое имя для короткой ссылки')
    else:
        custom_id = get_unique_short_id()

    new_url = URLMap(original=data['url'], short=custom_id)
    db.session.add(new_url)
    db.session.commit()
    return jsonify(new_url.to_dict()), HTTPStatus.CREATED


@app.route('/api/id/<short_id>/', methods=['GET'])
def get_original_url(short_id):
    db_object = URLMap.query.filter_by(short=short_id).first()
    if not db_object:
        raise APIErrors('Указанный id не найден', HTTPStatus.NOT_FOUND)
    original_url = db_object.original
    return jsonify({'url': original_url}), HTTPStatus.OK
