from flask import Flask, request
from caesar import encrypt

app = Flask(__name__)
app.config['DEBUG'] = True


form = '''
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
     <form action="/" method="POST">
        <label for="rot" name="rotlabel">Rotate by: </label>
        <input id="rot" type="text" name="rot" value="0"/>
        <br>
        <br>
        <label for="text" name="encryptlabel">Text to encrypt:</label>
        <br>
        <textarea id="text" name="text">{0}</textarea>
        <br>
        <br>
        <input type="submit" name="encryptsubmit" value="Encrypt">
     </form>
    </body>
    
</html>
'''

@app.route("/", methods=['GET'])
def index():
    return form.format('Type text to encrypt')

@app.route("/", methods=['POST'])
def encrypt_text():
    encrypttext = request.form.get('text')
    rot = int(request.form['rot'])
    encrypted = encrypt(encrypttext, rot)
    return form.format(encrypted)
app.run()