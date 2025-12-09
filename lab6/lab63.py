from flask import Flask, render_template

app = Flask(__name__)

data = [
  {"id": 1, "name": "Настя", "age": 30, "city": "Москва"},
  {"id": 2, "name": "Иван", "age": 24, "city": "Тула"},
  {"id": 3, "name": "Артём", "age": 35, "city": "Санкт-Петербург"},
  {"id": 4, "name": "Мария", "age": 28, "city": "Казань"},
]

@app.route('/')
def index():
  return render_template('index3.html', data=data, title="Данные пользователей")

if __name__ == '__main__':
  app.run(debug=True)