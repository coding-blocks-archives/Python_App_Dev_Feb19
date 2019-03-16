from flask import (
  Flask, 
  render_template
)
app = Flask(
  __name__, 
  static_folder='static',
  static_url_path='/static')
# name
# roll number
# 5 subject marks
@app.route('/')
def index():
  name = "Jatin Katyal"
  languages = [
    "python", "go", "javascript"
  ]
  context = {
    "name": name,
    "languages": languages
  }
  return render_template(
    'index.html', **context)

# /add/5/6
# /square/7
@app.route('/<string>')
def blank(string):
  return "hello, {}".format(string)

@app.route('/add/<int:a>/<int:b>')
def add(a, b):
  return "sum: {}".format(a+b)

@app.route('/person/<int:id>')
def person(id):
  name, lang = users[id]

  return "{} likes {}".format(name, lang)

def main():
  app.run(port = 8000, debug = True)

if __name__ == "__main__":
  main()
