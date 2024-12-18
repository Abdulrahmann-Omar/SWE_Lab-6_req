from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    name = request.form.get('name')
    age = request.form.get('age')
   
    return render_template('result.html', name=name, age=age)

if __name__ == '__main__':
    app.run(debug=True)
