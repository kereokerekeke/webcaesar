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
     <form action="http://localhost:5000/" method="POST">
        <label for="rot" name="rotlabel">Rotate by: </label>
        <input id="rot" type="text" name="rot" value="0"/>
        <br>
        <br>
        <label for="encrypt" name="encryptlabel">Text to encrypt:</label>
        <br>
        <textarea id="encrypt" name="encrypt">{0}</textarea>
        <br>
        <br>
        <input type="submit" name="encryptsubmit" value="Encrypt">
     </form>
    </body>
    
</html>
'''

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        encrypttext = request.form.get('encrypt')
        encrypted = encrypt(encrypttext, int(request.form['rot']))
    return form.format(encrypted)

app.run()