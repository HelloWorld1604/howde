from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def about():
    return render_template('homepage.html')

@app.route('/app')
def chat_app():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug=True)