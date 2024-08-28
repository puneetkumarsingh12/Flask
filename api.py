# from flask import Flask
# from flask_restful import Api,Resource 
# app=Flask(__name__)
# api=Api(app)
# Product_Infor={
#     1:{"Pid":1001,"Pname":"Mobile_1","Price":25000,"Company":"Samsung"},
#     2:{"Pid":1002,"Pname":"Mobile_2","Price":27000,"Company":"Samsung"},
#     3:{"Pid":1003,"Pname":"Mobile_3","Price":21000,"Company":"Samsung"},
#     4:{"Pid":1004,"Pname":"Mobile_3","Price":9000,"Company":"Samsung"},
#     5:{"Pid":1005,"Pname":"Mobile_3","Price":7000,"Company":"Samsung"},

# }
# class Test_Case1(Resource):
#     def get(self):
#         return Product_Infor 
# api.add_resource(Test_Case1,"/IHUB")
# if(__name__=="__main__"):
#     app.run(debug=True)


from flask import Flask
from flask_restful import Api,Resource 
app=Flask(__name__)
api=Api(app)
Product_Infor={
    1:{"Pid":1001,"Pname":"Mobile_1","Price":25000,"Company":"Samsung"},
    2:{"Pid":1002,"Pname":"Mobile_2","Price":27000,"Company":"Samsung"},
    3:{"Pid":1003,"Pname":"Mobile_3","Price":21000,"Company":"Samsung"},
    4:{"Pid":1004,"Pname":"Mobile_3","Price":9000,"Company":"Samsung"},
    5:{"Pid":1005,"Pname":"Mobile_3","Price":7000,"Company":"Samsung"},

}
class Test_Case1(Resource):
    def get(self,id):
        return Product_Infor[id]
api.add_resource(Test_Case1,"/IHUB/<int:id>")
if(__name__=="__main__"):
    app.run(debug=True)
