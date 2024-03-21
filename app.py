import string

from flask import Flask, render_template, request
import random

app = Flask(__name__)


def random_password(length):
    char = string.ascii_letters + string.digits + string.ascii_letters + string.ascii_uppercase + string.punctuation
    password = " ".join(random.choice(char) for _ in range(length))
    return password


@app.route('/', methods=['GET','POST'])
def index():
    senha = None
    show_password = False


    if request.method == 'POST':
        size = max(int(request.form.get('size', 12)), 12)
        show_password = True
        senha = random_password(size)


    return render_template('index.html', senha=senha, show_password=show_password)


if __name__ == '__main__':
    app.run(debug=True)
