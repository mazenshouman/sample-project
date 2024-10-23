from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    operation = data.get('operation')
    num1 = data.get('num1')
    num2 = data.get('num2')

    if operation not in ['add', 'subtract', 'multiply', 'divide']:
        return jsonify({'error': 'Invalid operation'}), 400

    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return jsonify({'error': 'Cannot divide by zero'}), 400
        result = num1 / num2

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
