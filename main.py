

from flask import Flask, request, abort
import datetime
import datetime as dt
import json
import time
 
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
 
## 2 ##
###############################################
#LINEのメッセージの取得と返信内容の設定(オウム返し)
###############################################
 
#LINEでMessageEvent（普通のメッセージを送信された場合）が起こった場合に、
#def以下の関数を実行します。
#reply_messageの第一引数のevent.reply_tokenは、イベントの応答に用いるトークンです。 
#第二引数には、linebot.modelsに定義されている返信用のTextSendMessageオブジェクトを渡しています。
 
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    if "授業" in event.message.text:
        content = "明日の授業は..."

        content = schedule_week2(week)

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=content)) #ここでオウム返しのメッセージを返します。

def schedule_week2(week):
    json_open = open('week2.json', 'r',encoding="utf-8")
    json_load = json.load(json_open)
    idx = len(json_load[week]["class"])
    indx = idx
    weeks = week
    if weeks == 1:
        embed = discord.Embed(title=json_load[week]["week"],color=0x00FF00)
        embed.add_field(name=json_load[week]["class"][indx - 1], value=json_load[week]["time"][indx - 1], inline=False)
        return embed
    if weeks == "Monday":
        embed = discord.Embed(title=json_load[week]["week"],color=0x00ff00,url="https://sites.google.com/g.neec.ac.jp/hac-it-ai02-all/2%E7%B5%84%E6%8E%88%E6%A5%AD%E3%83%AA%E3%83%B3%E3%82%AF#h.64dgy083n7j1")
        embed.add_field(name=json_load[week]["class"][indx - 2], value=json_load[week]["time"][indx - 2], inline=False)
        embed.add_field(name=json_load[week]["class"][indx - 1], value=json_load[week]["time"][indx - 1], inline=False)
        print("M")
        return embed
    if weeks == "Wednesday":
        embed = discord.Embed(title=json_load[week]["week"],color=0x00ff00,url="https://sites.google.com/g.neec.ac.jp/hac-it-ai02-all/2%E7%B5%84%E6%8E%88%E6%A5%AD%E3%83%AA%E3%83%B3%E3%82%AF#h.enh563r3am7t")
        embed.add_field(name=json_load[week]["class"][indx - 3], value=json_load[week]["time"][indx - 3], inline=False)
        embed.add_field(name=json_load[week]["class"][indx - 2], value=json_load[week]["time"][indx - 2], inline=False)
        embed.add_field(name=json_load[week]["class"][indx - 1], value=json_load[week]["time"][indx - 1], inline=False)
        print("W")
        return embed
    if weeks == "Thursday":
        embed = discord.Embed(title=json_load[week]["week"],color=0x00ff00,url="https://sites.google.com/g.neec.ac.jp/hac-it-ai02-all/2%E7%B5%84%E6%8E%88%E6%A5%AD%E3%83%AA%E3%83%B3%E3%82%AF#h.mustv3jw6wer")
        embed.add_field(name=json_load[week]["class"][indx - 4],value=json_load[week]["time"][indx - 4], inline=False)
        embed.add_field(name=json_load[week]["class"][indx - 3], value=json_load[week]["time"][indx - 3], inline=False)
        embed.add_field(name=json_load[week]["class"][indx - 2], value=json_load[week]["time"][indx - 2], inline=False)
        embed.add_field(name=json_load[week]["class"][indx - 1], value=json_load[week]["time"][indx - 1], inline=False)
        print("T")
        return embed
    if weeks == "Tuesday":
        embed = discord.Embed(title=json_load[week]["week"],color=0x00ff00,url="https://sites.google.com/g.neec.ac.jp/hac-it-ai02-all/2%E7%B5%84%E6%8E%88%E6%A5%AD%E3%83%AA%E3%83%B3%E3%82%AF#h.xu0w5gswu0lz")
        embed.add_field(name=json_load[week]["class"][indx - 5], value=json_load[week]["time"][indx - 5], inline=False)
        embed.add_field(name=json_load[week]["class"][indx - 4], value=json_load[week]["time"][indx - 4], inline=False)
        embed.add_field(name=json_load[week]["class"][indx - 3], value=json_load[week]["time"][indx - 3], inline=False)
        embed.add_field(name=json_load[week]["class"][indx - 2], value=json_load[week]["time"][indx - 2], inline=False)
        embed.add_field(name=json_load[week]["class"][indx - 1], value=json_load[week]["time"][indx - 1], inline=False)
        print("Tu")
        return embed
    if weeks == "Friday":
        embed = discord.Embed(title=json_load[week]["week"],color=0x00ff00,url="https://sites.google.com/g.neec.ac.jp/hac-it-ai02-all/2%E7%B5%84%E6%8E%88%E6%A5%AD%E3%83%AA%E3%83%B3%E3%82%AF#h.hzk0p75dg3mh")
        embed.add_field(name=json_load[week]["class"][indx - 2], value=json_load[week]["time"][indx - 2], inline=False)
        embed.add_field(name=json_load[week]["class"][indx - 1], value=json_load[week]["time"][indx - 1], inline=False)
        print("F")

        return embed
# ポート番号の設定
if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)