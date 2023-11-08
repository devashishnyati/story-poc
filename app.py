from flask import Flask, send_from_directory, render_template

app = Flask(__name__)


@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/testing/<string:file_name>')
def stream(file_name):
    print("Inside video API")
    video_dir = './video-folder'
    return send_from_directory(directory=video_dir, path=file_name)


if __name__ == '__main__':
    app.run()