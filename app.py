from flask import Flask, json, render_template,request, jsonify
from flask.helpers import make_response
from model.chatbot import main,user_input

app = Flask(__name__)
df,Topics,all_words,model = 0,0,0,0

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ask', methods = ['POST'])
def aks_me():
    query = request.get_json(force=True)
    message = query['message']
    res = user_input(df,Topics,all_words,message,model)
    return make_response(jsonify({'res':res}),200)

if __name__ == '__main__':
    #train the modle first! the start the app
    df,Topics,all_words,model = main()
    app.run(debug=True)