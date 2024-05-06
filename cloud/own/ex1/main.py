from flask import Flask

# Create Flask app instance
app = Flask(__name__)

# Define endpoint
@app.route('/hello')
def hello():
    return {"message": "Hello, World!"}

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
