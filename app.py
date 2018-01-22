from flask import Flask, render_template, send_from_directory
import os
import glob

app = Flask(__name__)
app.config['RESULT_STATIC_PATH'] = "posts/"

@app.route('/')
def index():
    posts = []
    for root, dirs, files in os.walk('posts'):
        posts += glob.glob(os.path.join(root, '*.html'))

    titles = []
    for post in posts:
        tmp = post.split('/')[1]
        tmp2 = tmp.split('.')[0]
        titles.append(tmp2)

    result_dict = dict(zip(titles, posts))

    return render_template('index.html', result=result_dict)

@app.route('/posts/<path:file>', defaults={'file': 'index.html'})
def serve_results(file):
    # Haven't used the secure way to send files yet
    return send_from_directory(app.config['RESULT_STATIC_PATH'], file)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
