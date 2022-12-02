from server_folder import app, db

from flask import Flask, redirect, render_template, request, url_for, session, flash


@app.route('/')
def homepage():
    return render_template('homepage.html')






if __name__ == '__main__':
    app.run(debug=True)