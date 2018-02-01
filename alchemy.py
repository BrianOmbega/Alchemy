from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///home/ombega/Projects/Alchemy/databasedir/alchemy.db'
db = SQLAlchemy(app)

class Dog(db.Model):
    __tablename__ = 'dogs'
    id = db.Column('id', db.Integer, primary_key=True)
    data = db.Column('data', db.Unicode)
    text = db.Column('jina', db.String(50))
#Create the index route
@app.route('/')
def index():
    return render_template('index.html')

#Create the add route. Only rendered with POST request.
@app.route('/add', methods=['POST'])
def add():
    #Create instance dog of class Dog passing in text and data
    dog = Dog(text=request.form['dog'], data =("You are my "))
    #Concatenate dog.text and dog.data
    dog.data += dog.text
    return '<h1>{}<h1>'.format(dog.data)

if __name__ == "__main__":
    app.run(debug=True)
