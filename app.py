from flask import Flask, render_template, request, redirect, url_for


app = Flask(
 __name__,
 template_folder="./templates",
 static_folder="./static",
)

@app.route("/")
def index():
    return render_template('index.html')

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