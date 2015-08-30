from flask import Flask, render_template, redirect, request
from data import get_url, add_url
app = Flask(__name__)

@app.route('/')
def start():
    return render_template('home.html')

@app.route('/new_url', methods=["POST"])
def new_url():
	long_url = request.form['long_url'];
	short_url = request.form['short_url']
	add_url(
		{
		'Long': long_url,
		'Short': short_url
		}
		)
	return render_template('new_url.html', url=short_url)

@app.route('/<short_url>')
def go(short_url):
	url = get_url(short_url)
	return redirect(url)

if __name__ == '__main__':
    app.run(debug=True)