from dexter.app import app
from flask import request, url_for, flash, redirect
from flask.ext.mako import render_template
from flask.ext.login import login_required, current_user
from sqlalchemy.sql import func

from dexter.models import db, Document, Entity, Medium

import dexter.articles
import dexter.entities
import dexter.api
import dexter.users
import dexter.dashboard

@app.route('/')
@login_required
def home():
    if current_user.admin:
        return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('monitor_dashboard'))
