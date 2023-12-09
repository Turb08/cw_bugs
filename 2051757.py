# output out of range if value is invalid
# output total incorrect if value is >120
# output integer required if value is str or float

# assigning values to credits
def credit_pass():
    p = int(input("Enter credits at pass: "))
    return p
def credit_defer():
    d = int(input("Enter credits at defer: "))
    return d
def credit_fail():
    f = int(input("Enter credits at fail: "))
    return f

# evaluating is values are assigned to respective outcome
def vol_of_credits():
    c_pass = credit_pass()
    c_defer = credit_defer()
    c_fail = credit_fail()
    if c_pass == 120:
        print("Progress")
    elif c_pass == 100:
        print("Trailer")
    elif c_fail >= 80:
        print("Exclude")
    else:
        print("Retriever")


# main code that runs when executed
def main():
    done = False
    while not done: # while loop to keep asking to enter values
        ques = input("Would you like to enter results or quit?(y/q): ")
        if ques == "y":
            vol_of_credits()
        elif ques == "q":
            print("Thanks for using our Program")
            done = True


main()

