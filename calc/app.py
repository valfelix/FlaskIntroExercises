# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

# @app.route('/add')
# def do_add():
#     """Adds a and b and returns result as the body."""
#     a = int(request.args.get('a'))
#     b = int(request.args.get('b'))
#     result = add(a, b)
#     return str(result)

# @app.route('/sub')
# def do_sub():
#     """Subtracts a and b and returns result as the body."""
#     a = int(request.args.get('a'))
#     b = int(request.args.get('b'))
#     result = sub(a, b)
#     return str(result)

# @app.route('/mult')
# def do_mult():
#     """Multiplies a and b and returns result as the body."""
#     a = int(request.args.get('a'))
#     b = int(request.args.get('b'))
#     result = mult(a, b)
#     return str(result)

# @app.route('/div')
# def do_div():
#     """Divides a and b and returns result as the body."""
#     a = int(request.args.get('a'))
#     b = int(request.args.get('b'))
#     result = div(a, b)
#     return str(result)

OPERATIONS = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div,
}

@app.route('/math/<op>')
def do_math(op):
    """Does given math operation on a and b and returns result as the body."""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    task = OPERATIONS[op](a,b)
    return str(task)
