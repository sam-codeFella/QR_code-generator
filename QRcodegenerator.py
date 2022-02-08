from flask import Flask, request, render_template
import os
import asyncio
from aiohttp import ClientSession, ClientResponseError

RESULT_IMAGES = os.path.join('static', 'results')

qr_app = Flask(__name__)
# qr_app.config['RESULT_IMAGES'] = RESULT_IMAGES


async def fetch_url_data(session, url):
    try:
        async with session.get(url, timeout=60, ssl=False) as response:
            resp = await response.read()
            await asyncio.sleep(1)
            file = open(RESULT_IMAGES + "/sample_image.png", "wb")
            file.write(response.content)
            file.close()
            return resp()
    except Exception as e:
        print(e)
    return

'''
async def getImage(input):
    response = requests.get("https://api.qrserver.com/v1/create-qr-code/?&data=" + input)
    file = open(RESULT_IMAGES + "/sample_image.png", "wb")
    file.write(response.content)
    file.close()
'''


async def getFile(input):
    filename = RESULT_IMAGES + '/sample_image.png'
    async with ClientSession() as session:
        task = asyncio.ensure_future(fetch_url_data(session, 'https://api.qrserver.com/v1/create-qr-code/?&data=' + input))
        print("yo")
        responses = await asyncio.gather(task)
        print(responses)
    return filename


@qr_app.route('/', methods=['GET'])
def welcome():
    print("Showing the home page....")
    return render_template("index.html")


@qr_app.route('/qr', methods=['POST'])
async def returnqr():
    input = request.form['input_text']
    filename = await getFile(input)
    return render_template("code.html", qr_image=filename)# okay so this works.


@qr_app.route('/generate', methods=['GET'])
def returnform():
    return render_template("input.html")


if __name__ == '__main__':
    print("Starting application.")
    qr_app.run(port=8888, host='0.0.0.0', debug=True)