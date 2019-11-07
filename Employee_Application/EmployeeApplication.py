'''
Created on Oct 23, 2019

@author: rakesh13575
'''
from flask.app import Flask
from flask.globals import request
from basics.CompanyExample import Employee
import jsonpickle
from flask.templating import render_template
from werkzeug.utils import redirect
from pip._vendor import requests

# initialize Flask Environment for current application
emp_app=Flask(__name__)

@emp_app.route("/")
def welcome():
    #request.
    print("Welcome screen shown")
    return "Welcome to Employee Application"

@emp_app.route("/web/emp")
def display_all_employees():
    emps = Employee.get_all_employees_from_db()
    return render_template("employees.html",result=emps,content_type="application/json")

@emp_app.route("/web/emp/register",methods=["POST"])
def register_new_emp():
    f_empno = int(request.form.get("empno"))
    f_name = request.form.get("name")
    f_day_salary = float(request.form.get("salary"))
    
    new_emp=Employee({"empno":f_empno,"name":f_name,"daily_salary":f_day_salary})
    Employee.add_employee_to_db(new_emp)
    
    return redirect("/web/emp")

@emp_app.route("/web/emp/delete",methods=["POST"])
def delete_emp():
    f_empno = request.form.get("id")
    print(f_empno)
    Employee.delete_employee_from_db(f_empno)
    
    return redirect("/web/emp")
    
@emp_app.route("/api/emp/list")
def get_all_emps():
    return jsonpickle.encode(Employee.get_all_employees_from_db())
    
@emp_app.route("/api/emp/register",methods=["POST"])
def add_new_emp():
    f_empno = int(request.form.get("empno"))
    f_name = request.form.get("name")
    f_day_salary = float(request.form.get("salary"))
    
    new_emp=Employee({"empno":f_empno,"name":f_name,"daily_salary":f_day_salary})
    return jsonpickle.encode(Employee.add_employee_to_db(new_emp))

if __name__ == '__main__':
    print("Flask app started")
    # start the http request listener on provided port
    emp_app.run(port=7799)
    pass