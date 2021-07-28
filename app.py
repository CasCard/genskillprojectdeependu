import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
DATABASE = os.path.join(PROJECT_ROOT, 'todo.db')

work = Flask(__name__)
work.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////" + DATABASE
work.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(work)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    complete = db.Column(db.Boolean)


@work.route("/")
def index():
    todolist = Todo.query.all()
    return render_template("index.html", todolist = todolist)


@work.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    newtask = Todo(title=title, complete=False)
    db.session.add(newtask)
    db.session.commit()
    return redirect(url_for("index"))


@work.route("/complete/<string:todo_id>")
def complete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("index"))


@work.route("/delete/<string:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    db.create_all()
    work.run(debug=True)

