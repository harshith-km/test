from flask import Flask, request, render_template

app = Flask(__name__)

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/track_time', methods=['POST'])
def track_time():
    print('this page is called')
    try:
        data = request.get_json()
        time_spent = data.get("time_spent")
    except Exception as e:
        print('Error: ' + str(e))
        return 'Error processing request', 400

    if not time_spent:
        print('no time provided')
        return 'Error no time provided', 400

    print(f'Time provided, Tital time spend is {time_spent}')
    return f'Time spent on page: {time_spent} seconds'


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cursor')
def cursor():
    return render_template('cursor.html')

if __name__ == '__main__':
    app.run(debug=True)