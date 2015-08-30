from flask import Flask, render_template, redirect, request
app = Flask(__name__)

urls = []

@app.route('/')
def start():
    return render_template('home.html')

@app.route('/new_url', methods=["POST"])
def new_url():
	long_url = request.form['long_url'];
	short_url = request.form['short_url']
	urls.append(
		{
		'Long': long_url,
		'Short': short_url
		}
		)
	return render_template('new_url.html', url=short_url)

@app.route('/<short_url>')
def go(short_url):
	for url in urls:
		if url.get('Short') == short_url:
			return redirect(str(url.get('Long')))

if __name__ == '__main__':
    app.run(debug=True)