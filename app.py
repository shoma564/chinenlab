#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, flash, render_template, request, session
import mysql.connector, re
from datetime import timedelta



app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/event")
def event():
    return render_template('index.html')

@app.route("/event/01")
def event01():
    return render_template('event01.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
