from flask import Flask, request, render_template, request, redirect, url_for, send_from_directory,jsonify
from comparison_model import similarity
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins="http://localhost:8080")

@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))

@app.route('/compare', methods=["POST"])
def compare_handler():
    try: 
        data = request.get_json()
    except:
        raise ValueError
    
    if data is None:
        raise ValueError

    result = similarity(data["sentences1"],data["sentences2"])

    dict = list_to_dict(result)

    return jsonify(dict)

def list_to_dict(result):
    list = []
    for sentence1, sentence2, score in result:
        entry = {
            "sentence1": sentence1,
            "sentence2": sentence2,
            "score": score
        }
        
        list.append(entry)
    
    return list

if __name__ == '__main__':
   app.run()