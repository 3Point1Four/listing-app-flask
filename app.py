from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder = "templates")

tasks = [{"dopoint": "Sample", "done": False}]

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)
@app.route("/add", methods=["POST"])

def add():
    task = request.form['task']
    tasks.append({"dopoint": task, "done": False})
    return redirect(url_for("index"))
@app.route("/edit/<int:index>", methods=["GET", "POST"])
  
def edit(index):
    task = tasks[index]
    if request.method == "POST":
        task['dopoint'] = request.form["task"]
        return redirect(url_for("index"))
    else:
        return render_template("edit.html", task=task, index=index)

@app.route("/check/<int:index>")    
def check(index):
    tasks[index]['done'] = not tasks[index]['done']
    return redirect(url_for("index"))
    
@app.route("/delete/<int:index>")
def delete(index):
    del tasks[index]
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)