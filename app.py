from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from image_flipper import convert_image

app = Flask(__name__)

@app.route('/')
def home():  # put application's code here
    return render_template('index.html')

# print variables from image flipper.html
@app.route('/imageflipper', methods=['GET','POST'])
def image_flipper():
    if request.method == 'POST':
        url = request.form['url']
        filename = request.form['filename']
        status = convert_image(url, filename)
        return render_template('imageflipper.html', status=status)
    else:
        return render_template('imageflipper.html')

if __name__ == '__main__':
    app.run(debug=True)
