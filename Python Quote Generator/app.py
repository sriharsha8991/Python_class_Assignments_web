from flask import Flask, render_template
import random
from quotes import QUOTES
# pip install flask

app = Flask(__name__)

@app.route('/')
def index():
    daily_quote = random.choice(QUOTES)
    return render_template('index.html', quote=daily_quote)


if __name__ == '__main__':
    app.run(debug=True)

