'''
Created on Oct 23, 2019

@author: rakesh13575
'''
import unittest
from basics.CompanyExample import Employee


class Test(unittest.TestCase):


    def setUp(self):
        print('Initializing Test')
        self.sample_emp = Employee({"empno":222,"name":"sameer","daily_salary":444})
        pass


    def tearDown(self):
        print('Finalizing Test')
        del self.sample_emp
        pass

    def testOne(self):
        print('Executing test one')
        emp = self.sample_emp
        print(emp._calculate_salary())
        self.assertGreater(emp._calculate_salary(),1000,"Salary not matching")
        pass
    
    def test_get_employees_from_db(self):
        emps = Employee.get_all_employees_from_db()
        print(len(emps),"Employees Found")
        for i in range(len(emps)):
            print(emps[i])
        self.assertGreater(len(emps), 0, "No Employees Found")
        pass
    
    def test_add_employee_to_db(self):
        current_count = len(Employee.get_all_employees_from_db())
        new_emp = Employee({"empno":input("Number:"),"name":input("Name:"),"daily_salary":input("salary")})
        new_emp = Employee.add_employee_to_db(new_emp)
        self.assertIsNotNone(new_emp, "No employee added")
        self.assertGreater(len(Employee.get_all_employees_from_db()),current_count,"One New Record added of Employee")
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()