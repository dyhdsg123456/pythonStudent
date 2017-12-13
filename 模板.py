from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username_ = request.form['username']
    password_ = request.form['password']
    if 'admin'==username_ and "123"==password_:
        return render_template('signin-ok.html', username=username_)
    return render_template('form.html', message='Bad username or password', username=username_)

if __name__ == '__main__':
    app.run()
