from flask import Flask, request, render_template
import requests
import os
import asyncio

RESULT_IMAGES = os.path.join('static', 'results')

qr_app = Flask(__name__)
# qr_app.config['RESULT_IMAGES'] = RESULT_IMAGES

async def getImage(url):
    response = requests.get("https://api.qrserver.com/v1/create-qr-code/?&data=" + input)
    file = open(RESULT_IMAGES + "/sample_image.png", "wb")
    file.write(response.content)
    file.close()

@qr_app.route('/', methods=['GET'])
def welcome():
    print("Showing the home page....")
    return render_template("index.html")


@qr_app.route('/qr', methods=['POST'])
def returnqr():
    input = request.form['input_text']
    response = requests.get("https://api.qrserver.com/v1/create-qr-code/?&data=" + input)
    # now this qr_image variable needs to be an actual image.
    file = open(RESULT_IMAGES + "/sample_image.png", "wb")
    file.write(response.content)
    file.close()
    filename = RESULT_IMAGES + '/sample_image.png'
    return render_template("code.html", qr_image=filename)# okay so this works.


@qr_app.route('/generate', methods=['GET'])
def returnform():
    return render_template("input.html")


if __name__ == '__main__':
    print("Starting application.")
    qr_app.run(port=8888, host='0.0.0.0', debug=True)