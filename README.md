# Yacut

## Описание

**Yacut** - это сервис укорачивания ссылок, который создает из длинной ссылки короткую. Короткую ссылку может предложить сам пользователь, или же сервис самостоятельно её сгенерирует.

## Технологии
- Python
- Flask
- SQLAlchemy

## Установка
1. Склонируйте репозиторий:
```
git clone git@github.com:AnnZebel/yacut.git
```
2. Активируйте venv и установите зависимости:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
3. Создайте в корневой директории файл .env со следующим наполнением:
```
FLASK_APP=yacut
FLASK_ENV=development
DATABASE_URI=sqlite:///db.sqlite3
SECRET_KEY=<ваш_секретный_ключ>
```
4. Запустить:
```
flask run
```

## Работа с API

Доступные эндпоинты:
```
"/api/id/"
"/api/id/{short_id}/"
```

Получение полного URL по короткой ссылке:
```
Method: GET
Endpoint: "/api/id/{short_id}/"
```

### Автор проекта
Анна Зыбель
