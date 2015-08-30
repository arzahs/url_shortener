from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def start():
    return render_template('home.html')

@app.route('/new_url', methods=["POST"])
def new_url():
	url = request.form['url'];
	return render_template('new_url.html', url=url)


if __name__ == '__main__':
    app.run(debug=True)