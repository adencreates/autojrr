from flask import Flask, render_template
import image_flipper

app = Flask(__name__)

@app.route('/')
def home():  # put application's code here
    return render_template('index.html')

@app.route('/image_flipper/')
def image_flipper():
    return render_template('image_flipper.html')

if __name__ == '__main__':
    app.run()
