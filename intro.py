from flask import Flask,render_template
app=Flask(__name__)
@app.route("/about")
def Test_Case1():
  return render_template("about.html")

@app.route("/contact")
def Test_Case2():
  return render_template("contact.html")

@app.route("/home")
def Test_Case3():
  return render_template("home.html")

@app.route("/about")
def Test_Case4():
  return render_template("about.html")

if(__name__=="__main__"):
  app.run(debug=True)