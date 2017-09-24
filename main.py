from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <!-- create your form here -->
        <form method="post">
            <input type="text" name="rot"/>
            <input type="textarea" name="text"/>
            <input type="submit"/>
        </form>
    </body>
</html>
"""

@app.route("/", methods=['post'])
def encrypt():
    text_to_encrypt = request.form['text']
    num_rotate = int(request.form['rot'])

    new_text = rotate_string(text_to_encrypt, num_rotate)
    
    return '<h1>' + new_text + '</h1>'

@app.route("/")
def index():
    return form

app.run()