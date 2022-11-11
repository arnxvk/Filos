from flask import Flask,render_template
from flask import request,send_file
import pyttsx3
from werkzeug.utils import secure_filename
from PyPDF2 import PdfFileReader


import os

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/home")
def home():
	return render_template("home.html")

@app.route("/uploader" , methods=['GET', 'POST'])
def uploader():
        global path_file
        if request.method=='POST':
            f = request.files['file1']
            path_file=f.filename
            f.save(secure_filename(f.filename))
            audio(path_file)
            return "Uploaded successfully!"

#print(path_file)

def speak(txt):
    talker = pyttsx3.init()
    #talker.say(txt)
    talker.save_to_file(txt,"filename.mp3")
    talker.runAndWait()


def audio(filename):
        book=open(filename , "rb")
        reader=PdfFileReader(book)
        pages=reader.numPages
        print(pages)
        page =reader.getPage(3)
        text=page.extractText()
        speak(text)


@app.route('/download')
def download_file():
        p='filename.mp3'
        return send_file(p,as_attachment=True)

@app.route("/audiobook")
def audiobook():
	return render_template("audiobook.html")

@app.route("/health")
def health():
	return render_template("site.html")


if __name__ == "__main__":
	app.run()
