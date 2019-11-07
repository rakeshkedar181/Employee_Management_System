'''
Created on Oct 22, 2019

@author: rakesh13575
'''
import sys

def example_datatypes():
    num_example = 20
    list_example = [12,'Name',434,'Developer']
    tuple_example = (23,44,66,900,23,944,['abc',45,98.87])
    emp_dict_example = {'empno':13575 , 'name':'rakesh','salary':246588,32:'aaaaa'}    
    list_example.append('india')
    
    print("Size is " ,num_example)
    print(list_example)
    print(tuple_example)
    print(tuple_example[3])
    print(tuple_example[-2])
    print(tuple_example[1:4:2]) #skip the element at last index
    print(tuple_example[1:])
    print(emp_dict_example)
    print('check presence of value using in', 23 in tuple_example)
    
    for key in emp_dict_example.keys():
        print(key ,'=' ,emp_dict_example[key])
        
    for key,value in emp_dict_example.items():
        print(key,'=',value)

    pass

def compute_division():
    try:
        num1 = int(input("Enter Number 1:"))
        num2 = int(input("Enter Number 2:"))
        result = num1/num2
    except ValueError:
        print("Invalid Number Entered")
    except ZeroDivisionError:
        print("Zero division error occurred")
    except:
        print("Exception Occured",sys.exc_info())
    else:
        print("Result of",num1, "/",num2," is ",result )
    finally:
        print("Division completed")
    
if __name__ == '__main__':
        #example_datatypes()
        compute_division()
        pass