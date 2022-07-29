from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/summer')
def summer():
   print('Request for index page received')
   return  '<h1>Hello Summer Day!</h1>'

def autumn():
   return '<h1>Hello Autumn ::) </h1>'
app.add_url_rule('/autumn','autumn',autumn)

@app.route("/my_pubkey", methods=["GET"])
def my_pubkey():
   pubkey0 = "ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBBk65s7ZJhsTrR55if8XofyvA/E5Ta0enBxaoF5ugTPnf5iDgN3A3QXBSyY+Yah2p0ehAKftRUf3GaTL0BXSi5g= root@huygens"
   rt_msg = "<h1>" + pubkey0 + "</h1>"
   return rt_msg, 200

@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
   time0 = datetime.now() 
   rt_string = {'remote_ip': request.remote_addr , 'TimeStamp': time0.strftime("%m/%d/%Y, %H:%M:%S") , 'ip3': request.remote_addr}
   #return jsonify({'ip': request.remote_addr }), 200
   return jsonify( rt_string ), 200

@app.route("/where_am_j", methods=["GET"])
def where_am_j():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
      time0 = datetime.now() 
      azBudge = '<div data-iframe-width="150" data-iframe-height="270" data-share-badge-id="961cdefc-2d50-40f8-a60e-5887e7c0f1f0" data-share-badge-host="https://www.credly.com"></div><script type="text/javascript" async src="//cdn.credly.com/assets/utilities/embed.js"></script>'
      rt_string = "<h1>" + request.environ['REMOTE_ADDR'] +  '   TimeStamp   '+  time0.strftime("%m/%d/%Y, %H:%M:%S") + "</h1>" + azBudge
      return rt_string, 200
    else:
      time0 = datetime.now() 
      rt_string = "<h1>" + request.environ['HTTP_X_FORWARDED_FOR'] +  '   TimeStamp   '+  time0.strftime("%m/%d/%Y, %H:%M:%S") + "</h1>"
      return rt_string, 200
#         return "<h1>" + request.environ['HTTP_X_FORWARDED_FOR'] + "</h1>" , 200

@app.route("/where_am_k", methods=["GET"])
def where_am_k():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
         return jsonify({'ip': request.environ['REMOTE_ADDR']}), 200
    else:
         return jsonify({'ip': request.environ['HTTP_X_FORWARDED_FOR']}), 200

@app.route('/dashboard/<name>')
def dashboard(name):
   return 'welcome %s' % name

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


if __name__ == '__main__':
   app.run()
