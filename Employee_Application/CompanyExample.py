'''
Created on Oct 22, 2019

@author: rakesh13575
'''
#class declaration
import sys
from mysql.connector import Connect
class Employee(object):
    
    # constructor
    def __init__(self,params):  #builtin method
        if int(params["empno"])<0:
            raise Exception("Invalid Employee Number Entered" + str(params["empno"]))
        self.empno = int(params["empno"])
        self.name = str(params["name"])
        self.salary_per_day = float(params["daily_salary"])
        
    def print_information(self):  
        print("Employee Number ", self.empno,"Name ",self.name,"salary ",self._calculate_salary(tax=800))

    def _calculate_salary(self,days=30,tax=100):
        return (self.salary_per_day*days) - tax
        
    def apply_leaves(self,days=1):
        self.current_leaves = 20
        self.MAX_LEAVES = 5
        
        if(self.current_leaves>days):
            self.current_leaves -= days
            print("Leave auto- approved")
        else:
            print("Not enough leaves")
            
    max_leaves = 10
    
    @classmethod        
    def update_max_leaves(cls,days):
        cls.max_leaves = days
        pass
    
    @staticmethod
    def get_Employee_by_empno(empno):
        return Employee({})
    
    @staticmethod
    def get_all_employees_from_db():
        emps = []
        
        try:
            #connect to db
            db_connection = Connect(user='root',password='root',database='training',port=3306)
            #get the db cursor
            db_cursor = db_connection.cursor()
            #identify the query and execute using cursor
            db_cursor.execute("select * from emp_data")
            #process data received from cursor
            for(empno,name,salary) in db_cursor:
                emps.append(Employee({"empno":empno,"name":name,"daily_salary":salary}))
            #close the cursor and connection
            db_connection.close()
            db_cursor.close()
        except:
            print("exception occurred",sys.exc_info())
            
        return emps
    
    @staticmethod
    def add_employee_to_db(new_emp):
        try:
            #connect to db
            db_connection = Connect(user='root',password='root',database='training',port=3306)
            #get the db cursor
            db_cursor = db_connection.cursor()
            #identify the query and execute using cursor
            db_cursor.execute("insert into emp_data values(%s,%s,%s)",(new_emp.empno,new_emp.name,new_emp.salary_per_day))
            db_connection.commit()
            db_connection.close()
            db_cursor.close()
        except:
            new_emp = None
            print("Exception Occured",sys.exc_info())
        return new_emp
    
    @staticmethod
    def delete_employee_from_db(empno):
        try:
            #connect to db
            db_connection = Connect(user='root',password='root',database='training',port=3306)
            #get the db cursor
            db_cursor = db_connection.cursor()
            #identify the query and execute using cursor
            db_cursor.execute("delete from emp_data where empno = %s",(empno,))
            db_connection.commit()
            db_connection.close()
            db_cursor.close()
        except:
            print("Excepion Occurred",sys.exc_info())
        return 
            
    # overriding the __str__ internal object method
    def __str__(self, *args, **kwargs):
        return "Empno:" + str(self.empno) + ", Name: "+ self.name
    
# derive class from base class - inheritance    
class SalesEmployee(Employee):    
    
    def __init__(self,params):
        Employee.__init__(self, params)
        self.commission = float(params["commission"])
        self.target = int(params["target"])
        
    def _calculate_salary(self, days=30, tax=100):
        base_salary = Employee._calculate_salary(self, days=days, tax=tax)
        return (base_salary*self.commission) + base_salary
    
    
if __name__ == '__main__':
    emp = Employee({"empno":13575,"name":"rakesh","daily_salary":122456})
    emp.print_information()
    emp.apply_leaves(5)
    
    emp1 = Employee({"empno":13575,"name":"rakesh","daily_salary":122456})
    Employee.update_max_leaves(15)
    print("max leaves:" , Employee.max_leaves)
    
    emp1.print_information()
    
    print(emp1)
    
    semp = SalesEmployee({"empno":233,"name":"sameer","daily_salary":44.044,"commission":3.5,"target":165})
    semp.print_information()
    pass