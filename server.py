from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')  # Serves index.html

@app.route('/features')
def features():
    return send_from_directory('.', 'features.html')  # Serves features.html

if __name__ == '__main__':
    app.run(debug=True)