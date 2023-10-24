
from flask import Flask, flash, render_template, jsonify, request, redirect, session, url_for, send_from_directory
import mysql.connector
from google.oauth2 import id_token
from google.auth.transport import requests
from pydub import AudioSegment


app = Flask(__name__)
app.secret_key = 'asdfk2dkwhdsfg'
# app.config['PREFERRED_URL_SCHEME'] = 'https'


def login_check():
    if 'user' not in session:
        session['pre_url'] = request.url
        return redirect(url_for('login'))

@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/api/data', methods=['GET'])
def get_data():
    data = {'message': 'Hello from Flask!'}
    return jsonify(data)



if __name__ == '__main__':
    app.run(debug=True)
    # context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    # context.load_cert_chain('/etc/letsencrypt/live/notepal.ai/fullchain.pem', '/etc/letsencrypt/live/notepal.ai/privkey.pem')

    # app.run(host='31.220.108.185', port=443, ssl_context=context)



