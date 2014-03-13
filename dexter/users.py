from dexter.app import app

from flask import request, url_for, flash, redirect
from flask.ext.mako import render_template
from flask.ext.login import login_required, login_user, logout_user, current_user

from dexter.models import User
from dexter.models.user import LoginForm


@app.route('/login', methods=['GET', 'POST'])
def user_login():
    if current_user.is_authenticated():
        return redirect(request.args.get("next") or url_for("home"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.get_and_authenticate(form.email.data, form.password.data)
        if user:
            login_user(user, remember=True)
            flash("Logged in successfully.")
            return redirect(request.args.get("next") or url_for("home"))
        else:
            flash("Incorrect email or password.", 'error')

    return render_template("users/login.haml", form=form)

@app.route('/logout', methods=['POST'])
@login_required
def user_logout():
    logout_user()
    return redirect(url_for('home'))
