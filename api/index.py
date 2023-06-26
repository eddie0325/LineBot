from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageMessage, ImageSendMessage

import os

line_bot_api = LineBotApi(os.getenv("LINE_CHANNEL_ACCESS_TOKEN"))
line_handler = WebhookHandler(os.getenv("LINE_CHANNEL_SECRET"))

app = Flask(__name__)

# domain root
@app.route('/')
def home():
    return 'Hello, World!'

@app.route("/webhook", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        line_handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


@line_handler.add(MessageEvent, message=TextMessage)
def handle_message(event):


    sendText0 = event.message.text + " ??? 蛤竟然敢講這種話，我看是欠星爆哦"

    sendText1 = "星爆...氣流斬..."

    img_url = "https://media.tenor.com/4Wmrjus9r0MAAAAC/%E6%98%9F%E7%88%86%E6%B0%A3%E6%B5%81%E6%96%AC.gif"
    
    
    line_bot_api.reply_message(event.reply_token, [
        TextSendMessage(text=sendText0),
        TextSendMessage(text=sendText1),
        ImageSendMessage(original_content_url=img_url, preview_image_url=img_url)
    ])
    
    return


if __name__ == "__main__":
    app.run()
