from flask_restful import Resource
from flask import render_template, make_response, request

class show_num(Resource):
    def get(self):
        x = request.args.get("x")

        y = request.args.get("y")

        method = request.args.get("method")

        totals = request.args.get("results")

        if not x and not y:
            x = "20"
            y = "20"
        
        if not x:
            x = "20"
        
        if not y:
            y = "20"

        datax = int(x)
        datay = int(y)

        if not method:
            method = "sum"

        # Penjumlahan
        if method == "sum":
            totals = calculation.sum(datax,datay)

        # Pembagian
        elif method == "divide":
            totals = calculation.divide(datax, datay)

        # Pengurangan
        elif method == "sub":
            totals = calculation.sub(datax, datay)

        # Perkalian
        elif method == "multiply":
            totals = calculation.multiply(datax, datay)

        else:
            totals = "cant get the current calculation result"

        results = str(totals)
            
        view = render_template("show_num.html", x=x, y=y, method=method, results=results)
        return make_response(view)

class calculation():    
    def sum(x,y):
        return x + y

    def divide(x,y):
        return x / y
    
    def sub(x,y):
        return x - y
    
    def multiply(x,y):
        return x * y