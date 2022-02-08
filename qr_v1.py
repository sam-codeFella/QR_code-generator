from flask import Flask, request, render_template
import requests
import os
import asyncio

RESULT_IMAGES = os.path.join('static', 'results')
app = Flask(__name__)


async def getImage(input):
    response = requests.get("https://api.qrserver.com/v1/create-qr-code/?&data=" + input)
    return response


async def syncGetImage(input):
    response = requests.get("https://api.qrserver.com/v1/create-qr-code/?&data=" + input)
    file = open(RESULT_IMAGES + "/sample_image.png", "wb")
    file.write(response.content)
    file.close()
    filename = RESULT_IMAGES + '/sample_image.png'
    return filename


async def getImage2(input):
    task = asyncio.ensure_future(getImage(input))# this is the async call.  One can continue execution from here.
    response = await asyncio.gather(task)
    return response[0]


@app.route('/', methods=['GET'])
def welcome():
    print("Showing the home page....")
    return render_template("index.html")


@app.route('/generate', methods=['GET'])
def returnForm():
    return render_template("input.html")


@app.route('/qrcode', methods=['POST'])
async def returnQr():
    input = request.form['input_text']
    response = await getImage2(input)
    file = open(RESULT_IMAGES + "/sample_image.png", "wb")
    file.write(response.content)
    file.close()
    filename = RESULT_IMAGES + '/sample_image.png'
    return render_template("code.html", qr_image=filename)# okay so this works.


if __name__ == '__main__':
    print("Starting application.")
    app.run(port=8888, host='0.0.0.0', debug=True)