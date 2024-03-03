from flask import Blueprint, url_for, redirect

logout = Blueprint('logout', __name__, template_folder='../frontend')


@logout.route('/logout')
def show():
    return redirect(url_for('login.show'))
