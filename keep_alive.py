from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return '<h1 style="bold">The web server is running for the stfu discord bot.</h1><br><img src=https://i.makeagif.com/media/3-20-2015/9ttdrX.gif>'

def run():
	app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()