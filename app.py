from flask import Flask,request
from main import query

app = Flask(__name__)

@app.route('/api/query', methods=['POST'])
def respond_to_query():
    data = request.get_json()
    prompt = data.get('prompt','')
    return {
        'response' : query(prompt)
    }

if __name__ == '__main__':
    app.run(debug = True)