# 1 Ошибка в коде:
# В строке @app.route('') должно быть указано, какой маршрут будет обрабатываться.
# Пустая строка недопустима, должен быть /!
# Исправленный код:
# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def home():
#     return 'Hello, World!'
# if __name__ == '__main__':
#     app.run()

# 2

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Flask!'

@app.route('/user/<name>')
def user(name):
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run(debug = True)