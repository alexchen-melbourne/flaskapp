from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from data import Articles

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/alex/Desktop/flaskapp/flask.db'
db = SQLAlchemy(app)


Articles = Articles()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def articles():
    return render_template('articles.html', articles = Articles)

@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        age = request.form['age']

        return render_template('age.html', age=age)
    
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)

