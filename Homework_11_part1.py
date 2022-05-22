from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template('Homework_11_part1.html')

if __name__ == '__main__':
    app.run()