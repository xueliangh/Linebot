import requests
from bs4 import BeautifulSoup
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

#Linebot Token
line_bot_api = LineBotApi('Your Linebot Token')
#Linebot Secret
handler = WebhookHandler('Your Linebot Secret')

def getWiki(term):
    res = requests.get('https://zh.wikipedia.org/wiki/{}'.format(term))
    soup = BeautifulSoup(res.text, 'lxml')
    article = soup.select_one('.mw-parser-output p').text
    return article
    print(article)

@app.route("/", methods=['GET'])
def hello():
    return "Hello World!"

@app.route("/", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    print("Request body: " + body, "Signature: " + signature)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
       abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    replay = getWiki(event.message.text)
    print(msg)
    msg = msg.encode('utf-8')
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=replay))

if __name__ == "__main__":
    app.run(debug=True,port=80)


