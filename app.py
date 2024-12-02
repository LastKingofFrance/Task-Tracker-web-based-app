from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initialize a dictionary to store tasks
tasks = {}

@app.route("/")
def home():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    coworker = request.form["coworker"]
    said_hi = request.form["said_hi"]  # Yes/No for saying hi
    task_given = request.form["task_given"]  # Yes/No for receiving a task
    task_desc = request.form["task"]  # Description of the task
    deadline = request.form["deadline"]  # Deadline for the task

    # Store the task data, including the interaction details
    tasks[task_desc] = {
        "coworker": coworker,
        "said_hi": said_hi,
        "task_given": task_given,
        "deadline": deadline
    }
    
    return redirect(url_for("home"))

@app.route("/complete/<task>")
def complete_task(task):
    if task in tasks:
        del tasks[task]
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
