import logging
from flask import Flask
import os

app = Flask(__name__)

if not os.path.exists('logs'):
    os.makedirs('logs')

handler = logging.FileHandler('./logs/flask-app.log')
handler.setLevel(logging.DEBUG)
app.logger.addHandler(handler)
app.logger.setLevel(logging.DEBUG)

@app.route('/')
def hello_world():
    app.logger.info('Witaj na stronie głownej!')
    return 'Hello, World!'

@app.route('/status')
def status():
    app.logger.info('Witaj na stronie status!')
    return {
        'status': 'ok',
        'message': os.getenv('STATUS_MESSAGE', '')
    }
    
@app.route('/version')
def version():
    app.logger.info('Witaj na stronie version!')
    
    return_dict = {
        'version': '1.0.0'
    }
    
    if os.getenv('SHOW_BUILD_INFO', None):
        return_dict['build_time'] = os.getenv('BUILD_TIME', 'brak informacji o czasie budowania')
    
    return return_dict

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('APP_PORT', 5000))
