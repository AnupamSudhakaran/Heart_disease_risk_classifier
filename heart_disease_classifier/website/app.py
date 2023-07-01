from flask import Flask, render_template, request
import pickle
import pandas as pd
import sklearn


app = Flask(__name__)


def response(ans):
    res1= """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .alert {
  position: relative;
  top: 10;
  left: 0;
  width: auto;
  height: auto;
  padding: 10px;
  margin: 10px;
  line-height: 1.8;
  border-radius: 5px;
  cursor: hand;
  cursor: pointer;
  font-family: sans-serif;
  font-weight: 400;
}

.alertCheckbox {
  display: none;
}

:checked + .alert {
  display: none;
}

.alertText {
  display: table;
  margin: 0 auto;
  text-align: center;
  font-size: 16px;
}

.alertClose {
  float: right;
  padding-top: 5px;
  font-size: 10px;
}

.clear {
  clear: both;
}

.info {
  background-color: #EEE;
  border: 1px solid #DDD;
  color: #999;
}

.success {
  background-color: #EFE;
  border: 1px solid #DED;
  color: #9A9;
}

.notice {
  background-color: #EFF;
  border: 1px solid #DEE;
  color: #9AA;
}

.warning {
  background-color: #FDF7DF;
  border: 1px solid #FEEC6F;
  color: #C9971C;
}

.error {
  background-color: #FEE;
  border: 1px solid #EDD;
  color: #A66;
}
    </style>
</head>
<body>
    <label>
        <input type="checkbox" class="alertCheckbox" autocomplete="off" />
        <div class="alert info">
          <span class="alertClose">X</span>
          <span class="alertText">You might have some  heart disease.
              <br class="clear"/></span>
        </div>
      </label>
      
</body>
</html>
    """

    res2= """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .alert {
  position: relative;
  top: 10;
  left: 0;
  width: auto;
  height: auto;
  padding: 10px;
  margin: 10px;
  line-height: 1.8;
  border-radius: 5px;
  cursor: hand;
  cursor: pointer;
  font-family: sans-serif;
  font-weight: 400;
}

.alertCheckbox {
  display: none;
}

:checked + .alert {
  display: none;
}

.alertText {
  display: table;
  margin: 0 auto;
  text-align: center;
  font-size: 16px;
}

.alertClose {
  float: right;
  padding-top: 5px;
  font-size: 10px;
}

.clear {
  clear: both;
}

.info {
  background-color: #EEE;
  border: 1px solid #DDD;
  color: #999;
}

.success {
  background-color: #EFE;
  border: 1px solid #DED;
  color: #9A9;
}

.notice {
  background-color: #EFF;
  border: 1px solid #DEE;
  color: #9AA;
}

.warning {
  background-color: #FDF7DF;
  border: 1px solid #FEEC6F;
  color: #C9971C;
}

.error {
  background-color: #FEE;
  border: 1px solid #EDD;
  color: #A66;
}
    </style>
</head>
<body>
    <label>
        <input type="checkbox" class="alertCheckbox" autocomplete="off" />
        <div class="alert info">
          <span class="alertClose">X</span>
          <span class="alertText">You Probably do not have any disease.
              <br class="clear"/></span>
        </div>
      </label>
      
</body>
</html>
    """
    return(res1 if ans==1 else res2)




#************************CODE**************************************************#

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/validate-user", methods=["POST"])
def validate_user():
    lst=[]
    # print(request.form,request.method)
    if request.method == "POST":
        # print(request.form)
        # print(request.form['age'])
        lst.append(request.form['age'])
        lst.append(1 if request.form['gender']=="Male" else 0)
        lst.append(request.form['chestpain'])
        lst.append(request.form['bp'])
        lst.append(request.form['cholestrol'])
        lst.append(request.form['sugar'])
        lst.append(request.form['ecg'])
        lst.append(request.form['heart_rate'])
        lst.append(request.form['angina'])
        lst.append(request.form['oldpeak'])
        lst.append(request.form['exc_st'])
        lst.append(request.form['blood_vessels'])
        lst.append(request.form['thal'])
        f=open(r"C:\Users\Anupam\Desktop\Projects\website\intial_model","rb")
        model=pickle.load(f)
        # lst=[38,1,2,138,175,0,1,173,0,0.0,2,4,2]
        lst=pd.DataFrame(lst).T
        res=model.predict(lst)
        # 0 is no disease and 1 is diesease
        # ans=""
        # if res==0:
        #     ans="You might have a disease Please get Checked"
        # else:
        #     ans="You are safe you might not a have a disease"
        return response(res)
        # print(lst)
        
    
    # print(lst)
    # return 'Hello ' + request.form['userid']

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)