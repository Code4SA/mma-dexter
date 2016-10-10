from dexter.app import app
from flask import request, url_for, flash, redirect
from flask.ext.mako import render_template
from flask.ext.security import current_user
from sqlalchemy.sql import func

from dexter.models import db, Document, Entity, Medium

import dexter.articles
import dexter.entities
import dexter.api
import dexter.dashboard
import dexter.mine
import dexter.search
import dexter.fdi

@app.route('/')
def home():
    if current_user.is_authenticated():
        if current_user.admin:
            return redirect(url_for('dashboard'))

        if current_user.has_role('monitor'):
            return redirect(url_for('monitor_dashboard'))

        if current_user.has_role('miner'):
            return redirect(url_for('mine_home'))

        if current_user.has_role('fdi'):
            return redirect(url_for('fdi_home'))

        return render_template('noperms.haml')
    else:
        return redirect(url_for('security.login'))

