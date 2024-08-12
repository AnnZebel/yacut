from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, URL


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле'),
                    URL(message='Введите корректный URL адрес'),
                    Length(1, 256)]
    )
    custom_id = StringField(
        'Короткая ссылка',
        validators=[Length(max=16),
                    Optional()]
    )
    submit = SubmitField('Создать')
