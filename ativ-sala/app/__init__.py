from flask import Flask, request
import logging


logging.basicConfig(level=logging.INFO)


app = Flask(__name__)
app.config['SECRET_KEY'] = 'sao-paulo-futebol-clube'


@app.before_request
def log_request_info():
   app.logger.info('Requesição Recebida: %s %s', request.method, request.path)


from app import routes
