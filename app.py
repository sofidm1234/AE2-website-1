from flask import Flask, render_template 
#imported flask
app = Flask(__name__)
#created flask app 
#register route to application
@app.route("/")
def hello_world():
  return render_template('home.html')
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
  #if it is running app.py
  