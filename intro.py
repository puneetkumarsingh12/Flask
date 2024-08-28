from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/home",methods=["POST"])
def Test_Case1():
    user_1=request.form["username"]
    pass_1=request.form["password"]
    if(user_1=="Rahul_12345" and pass_1=="R_12345"):
        return "<h1><tt>Valid user ....</tt></h1>"
    else:
        return "<h1><tt>In_Valid user ....</tt></h1>"
if(__name__=="__main__"):
    app.run(debug=True)
