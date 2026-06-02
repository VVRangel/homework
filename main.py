
from flask import Flask, render_template, request, redirect


app = Flask(__name__)

tasks = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task = request.form.get("task")

        if task and task.strip():
            tasks.append(task.strip())

        return redirect("/")

    return render_template("index.html", tasks=tasks)


@app.route("/delete/<int:task_id>")
def delete(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect("/")


@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit(task_id):
    if task_id < 0 or task_id >= len(tasks):
        return redirect("/")

    if request.method == "POST":
        new_task = request.form.get("task")

        if new_task and new_task.strip():
            tasks[task_id] = new_task.strip()

        return redirect("/")

    return render_template("edit.html", task=tasks[task_id], task_id=task_id)


if __name__ == "__main__":
    app.run(debug=True)
else:
    pass