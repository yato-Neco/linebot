from flask import Flask, request, abort
import datetime
import datetime as dt
import json
import time
import asyncio

 
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import os
 
app = Flask(__name__)
 
#環境変数取得

YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]
line_bot_api=LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler=WebhookHandler(YOUR_CHANNEL_SECRET)
 
 
## 1 ##
#Webhookからのリクエストをチェックします。
@app.route("/callback", methods=['POST'])
def callback():
    # リクエストヘッダーから署名検証のための値を取得します。
    signature = request.headers['X-Line-Signature']
 
    # リクエストボディを取得します。
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
 
    # handle webhook body
    # 署名を検証し、問題なければhandleに定義されている関数を呼び出す。
    try:
        handler.handle(body, signature)
    # 署名検証で失敗した場合、例外を出す。
    except InvalidSignatureError:
        abort(400)
    #handleの処理を終えればOK
    return 'OK'
 

 
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    if "授業" in event.message.text:
        content = "明日の授業は..."

        json_open = open('week2.json', 'r',encoding="utf-8")
        json_load = json.load(json_open)
        week = dt.datetime.now().strftime("%A")
        indx = len(json_load[week]["class"])
        if indx == 1:
            buffa = json_load[week]["week"] +  json_load[week]["class"][indx - 1]

            content = buffa

        if week == "Monday":
            buffa = json_load[week]["class"][indx - 2] + json_load[week]["time"][indx - 2] + json_load[week]["class"][indx - 1] + json_load[week]["time"][indx - 1]

            content - buffa

        if week == "Wednesday":
            buffa = json_load[week]["class"][indx - 3] + json_load[week]["time"][indx - 3] + json_load[week]["class"][indx - 2] + json_load[week]["time"][indx - 2] + json_load[week]["class"][indx - 1] + json_load[week]["time"][indx - 1]

            content = buffa

        if week == "Thursday":
            buffa = json_load[week]["class"][indx - 4]
            + json_load[week]["time"][indx - 4]
            + json_load[week]["class"][indx - 3]
            + json_load[week]["time"][indx - 3]
            + json_load[week]["class"][indx - 2]
            + json_load[week]["time"][indx - 2]
            + json_load[week]["class"][indx - 1]
            + json_load[week]["time"][indx - 1]

            content = buffa

        if week == "Tuesday":
            buffa = json_load[week]["class"][indx - 5]
            + json_load[week]["time"][indx - 5]
            + json_load[week]["class"][indx - 4]
            + json_load[week]["time"][indx - 4]
            + json_load[week]["class"][indx - 3]
            + json_load[week]["time"][indx - 3]
            + json_load[week]["class"][indx - 2]
            + json_load[week]["time"][indx - 2]
            + json_load[week]["class"][indx - 1]
            + json_load[week]["time"][indx - 1]

            content = buffa

        if week == "Friday":
            buffa = json_load[week]["class"][indx - 2] + json_load[week]["time"][indx - 2] + json_load[week]["class"][indx - 1] + json_load[week]["time"][indx - 1]

            content = buffa


    line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))




# ポート番号の設定
if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)