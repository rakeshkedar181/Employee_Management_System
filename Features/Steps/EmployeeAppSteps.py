from nose.tools.trivial import ok_
from selenium import webdriver

@given("User wants to browse list of employees")
def emp_web_browse_employees(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://localhost:7799/web/emp")
    context.count = int(context.driver.find_element_by_id("emp_count").text)
    print(context.count)
    context.driver.save_screenshot("list.png")
    ok_(context.count>0,"Employees not found")
    pass

@then("he should see the list with count")
def emp_web_browse_display_count(context):
    ok_(context.count>0,"Employees Count failed")
    pass

@given("set of employees")
def add_set_of_emps(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://localhost:7799/web/emp")
    context.prev_count = int(context.driver.find_element_by_id("emp_count").text)
     
    for row in context.table:
        context.driver.find_element_by_id("f-empno").send_keys(row["empno"])
        context.driver.find_element_by_id("f-name").send_keys(row["name"])
        context.driver.find_element_by_id("f-salary").send_keys(row["salary"])
        context.driver.save_screenshot("pre-add"+row["empno"]+".png")
        context.driver.find_element_by_id("btn-register").click()
        context.driver.save_screenshot("post-add"+row["empno"]+".png")
     
@then("Employee details will be added and count will increase")
def validate_count_increase_after_add(context):
    context.current_count = int(context.driver.find_element_by_id("emp_count").text)
    ok_(context.prev_count<context.current_count,"Could not changed, Employee not added")
    
@given("User wants to delete an employee")
def del_emp(context):
    context.driver =webdriver.Chrome()
    context.driver.get("http://localhost:7799/web/emp")
    context.prev_count = int(context.driver.find_element_by_id("emp_count").text)
    
    for row in context.table:
        context.driver.find_element_by_id("f-empno").send_keys(row["empno"])
        context.driver.save_screenshot("pre-delete"+row["empno"]+".png")
        context.driver.find_element_by_id("btn-delete").click()
        context.driver.save_screenshot("post-delete"+row["empno"]+".png")
    
    
@then("Employee details will be deleted and count will decrease")
def validate_count_decrease_after_delete(context):
    context.current_count = int(context.driver.find_element_by_id("emp_count").text)
    ok_(context.current_count<context.prev_count,"Could not changed, Employee not deleted")
    