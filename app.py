from flask import Flask, render_template, request, redirect
import joblib

app = Flask(__name__)

#loading model
def getPredictions(eText):
     model=joblib.load('model.pkl')
     arr=model.predict(eText)
     for x in arr :
          if(x==1) :
              res="Spam"
          else:
              res="Not Spam" 
     return res

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method=="POST":
        # rollno = request.form['rollno']
        eText=request.form['emailText']
        eText=[eText]
        result=getPredictions(eText)
        return render_template('result.html', result=result)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, port=8000)