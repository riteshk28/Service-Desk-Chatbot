from flask import Flask, render_template, request
from flask import jsonify

from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import time

bot = ChatBot('Test')

conv = open('servicedesk.txt', 'r').readlines()

bot.set_trainer(ListTrainer)

bot.train(conv)
'''
while True:
	request = raw_input('You: ')
	
	response = bot.get_response(request)
'''
app = Flask(__name__,static_url_path="/static") 

#############
# Routing
#
@app.route('/message', methods=['POST'])
def reply():
    message = request.form['msg']
    reply=str(bot.get_response(message))
    print(reply)
    
    return jsonify({'text':reply})

@app.route("/")
def index(): 
    return render_template("index.html")
#############

'''
Init seq2seq model

    1. Call main from execute.py
    2. Create decode_line function that takes message as input
'''
#_________________________________________________________________
'''import tensorflow as tf
import execute

sess = tf.Session()
sess, model, enc_vocab, rev_dec_vocab = execute.init_session(sess, conf='seq2seq_serve.ini')'''
#_________________________________________________________________

# start app
if (__name__ == "__main__"): 
    app.run(port = 5000) 
