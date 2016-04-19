def foo1():
    a = 1
    def foo2():
        print a
        #this will cause the fault
        #because it find the change the a
        #if your use the python3 you can add
        #nonlocal
        a = a + 1
    return foo2

if __name__ == "__main__":
    temp = foo12()
    temp()
    

