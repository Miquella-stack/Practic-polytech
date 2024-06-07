from flask import Flask, render_template

app = Flask(__name__)
#функция @app.route('/') создает путь для вкладки

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/warrior')
def warrior():
    return render_template('warrior.html')

@app.route('/mag')
def mag():
    return render_template('mag.html')

@app.route('/ranger')
def ranger():
    return render_template('ranger.html')

@app.route('/summoner')
def summoner():
    return render_template('summoner.html')

if __name__ == '__main__':
    app.run(host = '127.0.0.1' ,port = 3000 ,debug=True)