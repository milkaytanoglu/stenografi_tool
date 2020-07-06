from flask import Flask, render_template, request, send_from_directory, send_file
from flask_uploads import UploadSet, configure_uploads, IMAGES
from stego_web_new import stego_encode, stego_decode
app = Flask(__name__, static_folder='images')

photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'images/old'
configure_uploads(app, photos)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encode', methods=['GET', 'POST'])
def encode():
    if request.method == 'POST' and 'photo' in request.files and 'plaintext' in request.form and 'password' in request.form:
        filename = photos.save(request.files['photo'])
        plaintext = request.form['plaintext']
        passw = request.form['password']
        stego_encode.encode(plaintext, passw, filename)
        print(filename)
        return render_template("encode_download.html",f_=filename)
    return render_template('encode.html')

@app.route('/decode', methods=['GET', 'POST'])
def decode():
    if request.method == 'POST' and 'photo' in request.files and 'password' in request.form:
        file = request.files['photo']
        filename = file.filename
        print(filename)
        #filename = photos.save(request.files['photo'])
        passw = request.form['password']
        text = stego_decode.decode(passw, filename)
        if str(text) != 'None':
            return render_template("decode_done.html",value = text, f_name = filename+".png")
        else:
            return render_template("decode_error.html")

    return render_template('decode.html')

@app.route('/decode_done')
def decode_done():
    return render_template('decode_done.html')

@app.route('/decode_error')
def decode_error():
    return render_template('decode_error.html')

@app.route('/encode_download')
def encode_download():
    return render_template("encode_download.html")


if __name__ == '__main__':
    app.run(host= '0.0.0.0')
