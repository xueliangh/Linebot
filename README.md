# Linebot
用python撰寫的Linebot

首先必須申請你的Linebot Developers
然後將token與secret貼到到Linebot_Reply_Wiki.py中
記得將後台的webhook打開
在電腦端用cmd 執行Linebot_Reply_Wiki.py port預設80

需要再下載ngrok 
在ngrok.exe的目錄下啟動cmd
輸入 ngrok http 80

這樣就可以讓Linebot自動接收內容 並搜尋維基百科回覆
