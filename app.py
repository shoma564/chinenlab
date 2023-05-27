#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, flash, render_template, request, session
import mysql.connector, re
from datetime import timedelta



app = Flask(__name__, static_folder='./templates/images/')


@app.route("/")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
