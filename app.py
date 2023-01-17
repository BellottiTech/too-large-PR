from flask import Flask, render_template, request, redirect, url_for

import random
import json

app = Flask(
 __name__,
 template_folder="./templates",
 static_folder="./static",
)

@app.route("/")
def index():
    item = []
    key = 0
    with open("data.json") as f:
        data = json.loads(f.read())
        key = random.randrange(0, len(data["todo"])+1, 1)
        item = data["todo"][key]

    return render_template('index.html',item=item, key=key)

@app.route("/submit", methods=['POST'])
def update():
    if request.method == "POST":
        key = request.form.get('key')
        k = int(key)
        name = request.form.get('name')
        desc = request.form.get('description')
    
        with open("data.json") as f:
            data = json.loads(f.read())
            item = data["todo"][k]
            if name.lower() != "skip":
                data["done"].append({"pattern":item, "name":name, "description":desc})
            data["todo"] = data["todo"][0:k] + data["todo"][k+1:]
    
        with open("data.json", "w") as f:
            f.write(json.dumps(data))