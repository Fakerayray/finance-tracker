from flask import Flask\napp = Flask(__name__)\n@app.route('/')\ndef hello(): return 'Vault Online'\nif __name__ == '__main__': app.run(host='0.0.0.0', port=8080)
