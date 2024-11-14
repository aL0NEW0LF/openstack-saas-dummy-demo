from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        num1 = float(data['num1'])
        num2 = float(data['num2'])
        operation = data['operation']

        result = None
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return jsonify({'error': 'Division by zero'}), 400
            result = num1 / num2
        else:
            return jsonify({'error': 'Invalid operation'}), 400

        return jsonify({
            'result': result,
            'operation': operation,
            'num1': num1,
            'num2': num2
        })
    except KeyError:
        return jsonify({'error': 'Missing parameters'}), 400
    except ValueError:
        return jsonify({'error': 'Invalid numbers'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
