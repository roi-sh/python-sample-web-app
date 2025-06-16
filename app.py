from flask import Flask, render_template, request, redirect, url_for, flash
import os
import secrets

app = Flask(__name__)
secret_key = os.environ.get('SECRET_KEY')
if not secret_key:
    print("WARNING: No SECRET_KEY provided, generating random key")
    secret_key = secrets.token_urlsafe(32)

app.secret_key = secret_key

tasks = []

@app.route('/')
def home():
    """Home page route"""
    return render_template('index.html', tasks=tasks)

@app.route('/about')
def about():
    """About page route"""
    return render_template('about.html')

@app.route('/add_task', methods=['POST'])
def add_task():
    """Add a new task"""
    task = request.form.get('task')
    if task:
        tasks.append({'id': len(tasks) + 1, 'text': task, 'completed': False})
        flash('Task added successfully!', 'success')
    else:
        flash('Please enter a task!', 'error')
    return redirect(url_for('home'))

@app.route('/complete_task/<int:task_id>')
def complete_task(task_id):
    """Mark a task as completed"""
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            flash('Task completed!', 'success')
            break
    return redirect(url_for('home'))

@app.route('/delete_task/<int:task_id>')
def delete_task(task_id):
    """Delete a task"""
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    flash('Task deleted!', 'info')
    return redirect(url_for('home'))

@app.route('/api/tasks')
def api_tasks():
    """API endpoint to get all tasks as JSON"""
    return {'tasks': tasks}

if __name__ == '__main__':
    if not os.path.exists('templates'):
        os.makedirs('templates')
    
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    
    app.run(debug=debug, host='0.0.0.0', port=port)
