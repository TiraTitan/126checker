from flask import Flask, render_template_string, redirect

app = Flask(__name__)

@app.route('/')
def main_route():
    return redirect('/panel')

@app.route('/panel')
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>126Checker</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #121212;
                color: white;
                text-align: center;
                margin: 0;
                height: 100vh;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
            }
            h1 {
                font-size: 3rem;
                margin-bottom: 10px;
            }
            p {
                font-size: 1.5rem;
                margin-top: 0;
            }
            .container {
                padding: 20px;
                background-color: #1e1e1e;
                border-radius: 10px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.6);
            }
            .footer {
                position: absolute;
                bottom: 20px;
                font-size: 1rem;
                color: #aaa;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>126Checker'a Hoş Geldiniz</h1>
            <p>Şu anlık kapalıyız</p>
        </div>
        <div class="footer">
            <p>© 2025 126Checker. Tüm hakları saklıdır.</p>
        </div>
    </body>
    </html>
    """)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
