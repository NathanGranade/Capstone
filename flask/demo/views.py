from flask import Blueprint, render_template, request, jsonify, redirect, url_for 

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html", name = "Thomas")

@views.route("/app")
def app():
    return render_template("app.html", name = "Thomas")

@views.route("/register")
def register():
    return render_template("login.html")

@views.route("/tuner")
def tuner():
    return render_template("tuner.html")

