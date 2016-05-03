a = 1
def foo():
        #OK in the foo, just use the var out of the function
        print a

def foo1():
        #this will cause the error because the interpreter
        #find we change the a in foo1. so a is local var
        print a
        a = 1


if __name__ == "__main__":
    foo()
   # foo1()
