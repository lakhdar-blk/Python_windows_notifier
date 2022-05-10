from threading import Timer


def function1():
    print("lakhdar")
    
def function2():
    print("khadero")

if __name__=="__main__":

    t1 = Timer(0, function1)
    t2 = Timer(5, function1)
    t1.start()
    t2.start()

    while(True):
        v = input()
        print(v)