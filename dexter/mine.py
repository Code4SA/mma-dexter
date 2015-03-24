from dexter.app import app

from flask import request, url_for, flash, redirect, make_response, jsonify, abort
from flask.ext.mako import render_template
from flask.ext.login import login_required, current_user

@app.route('/mine/')
@login_required
def mine_home():
    return render_template('mine/index.haml')
