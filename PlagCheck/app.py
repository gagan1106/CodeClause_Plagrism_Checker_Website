from flask import Flask, render_template, request
from plagiarism_detection import plagiarism_check

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', plagiarism_result=None)

@app.route('/check', methods=['POST'])
def check_plagiarism():
    document = request.files['document']
    plagiarism_result = plagiarism_check(document)
    return render_template('index.html', plagiarism_result=plagiarism_result)

if __name__ == '__main__':
    app.run()
