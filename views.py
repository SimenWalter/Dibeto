from flask import Blueprint, redirect
from flask import render_template

views = Blueprint('views', __name__)

@views.route('/')
def homepage():
    return redirect('/index')

@views.route('/signup')
def signup():
    return render_template("signup.html")

@views.route('/the_claims')
def the_claims():
    return redirect('/claims')

@views.route('/the_replies')
def the_replies():
    return redirect('/replies')