from flask import Blueprint, url_for, render_template, redirect, request

login = Blueprint('login', __name__, template_folder='../frontend')


@login.route('/login', methods=['GET', 'POST'])
def show():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # TODO Check if username and password pair exist in DB
        return redirect(url_for('home.show'))
    else:
        return render_template('login.html')
