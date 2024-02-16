from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Utilisation d'un dictionnaire pour stocker les informations de connexion.
users = {'username': 'password'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username in users and users[username] == password:
        return redirect(url_for('success'))
    else:
        return redirect(url_for('index'))

@app.route('/success')
def success():
    return "Connexion réussie !"

if __name__ == '__main__':
    app.run(debug=True)

