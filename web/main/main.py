# -*- coding: utf-8 -*-
import os
from flask import Flask, request, url_for, send_from_directory
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['mp3', 'mp4', 'wav'])

app = Flask(__name__)
#文件上传路径
app.config['UPLOAD_FOLDER'] = os.getcwd()
#上传文件大小 200M
app.config['MAX_CONTENT_LENGTH'] = 200 * 1024 * 1024


#html
html = '''
    <!DOCTYPE html>
    <title>Upload File</title>
    <h1>音视频上传</h1>
    <form method=post enctype=multipart/form-data>
         <input type=file name=file>
         <input type=submit value=上传>
    </form>
    '''


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file_url = url_for('uploaded_file', filename=filename)
            return html + '<br><audio controls src=' + file_url + '> <a href=" + file_url "> Download audio </a></audio>'
    return html


if __name__ == '__main__':
    app.run()