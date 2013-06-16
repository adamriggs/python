from bottle import route, run, template

@route('/hello/:name')
def index(name='World'):
    return template('<b>Hello {{name}}</b>!', name=name)

@route('/')
def index(name='World'):
    return '<b>Hello</b>!'

run(host='ubuntu.vm', port=8080)
