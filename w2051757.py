# I declare that my work contains no examples of misconduct, such as plagiarism or collusion.

# Any code taken from other sources will be referenced within my code solution.

# Student ID: IIT- 20230747  UoW- 20517577

# Date: 2023/11/29
from graphics import*
total = 120
credit_pass = int(input("Enter credits at pass: "))
credit_defer = int(input("Enter credits at defer: "))
credit_fail = int(input("Enter credits at defer: "))
def vol_of_credit():
    credit_pass = int(input("Enter credits at pass: "))
    credit_defer = int(input("Enter credits at defer: "))
    credit_fail = int(input("Enter credits at defer: "))
def list_range():
    value = [0, 20, 40, 60, 80, 100, 120]
    try:
        if value in vol_of_credit():
            print(vol_of_credit())
    except:
        print("Value is out of range")
def integer_req():
    try:
        vol_of_credit()
    except ValueError:
        print("Integer required.")
def total_inc():
    if total != vol_of_credit():
        print("Total is incorrect. Please enter again.")

def module_progress():
    pass
def module_trailer():
    pass
def module_retriever():
    pass
def module_exclude():
    pass

def main():
    vol_of_credit()
    if credit_pass in module_progress() == 120: print("Progress.")
    if credit_pass in module_trailer() == 100: print("Module trailer.")
    if credit_pass in module_retriever() == 80 or 60 or 40 or 20 or 0: print("Module retriever.")
    if credit_pass in module_exclude() == 40 or 20 or 0: print("Excluded.")

main()
