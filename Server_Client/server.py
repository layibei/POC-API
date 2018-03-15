#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6
from flask import Flask, jsonify, abort, request, url_for, make_response , render_template
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS



auth = HTTPBasicAuth()

#@auth.get_password
#def get_password(username):
#    if username == 'Dicky':
#        return 'Wong'
#    return None

# @auth.error_handler
# def unauthorized():
#     return make_response(jsonify({'error': 'Unauthorized access'}), 401)


app = Flask(__name__)
CORS (app)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'I am dying when I am learning Python', 
        'done': False, 
	'type': u'testing'
    }
]

def make_public_task(task):
    new_task = {}

    for field in task:
        new_task[field] = task[field]

    new_task['uri'] = url_for('get_task', task_id=task['id'], _external=True)

#    for field in task:
#        if field == 'id':
#            new_task['uri'] = url_for('get_task', task_id=task['id'], _external=True)
#        else:
#            new_task[field] = task[field]

    return new_task

# list all (GET method)
@app.route('/todo/api/v1.0/tasks', methods=['GET'])
# @auth.login_required		# disable authentication
def get_tasks():
    return jsonify({'tasks': [make_public_task(task) for task in tasks]})

# list a particular task (GET method)
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task_temp = [task for task in tasks if task['id'] == task_id]
    if len(task_temp) == 0:
        #abort(404)
        return make_response(jsonify({'error': 'Not found'}), 401)
    return jsonify({'task': task_temp[0]})

    #if len(task_temp) == 0: 
	# abort(404)

# create a task (POST method)
@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

# update a task (PUT method)
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})

# delete a task (DELETE method)
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})


@app.route('/')
def index():
    return "Dicky testing project!"


@app.route('/client/')
def static_page(name=None):
    return render_template('client.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
