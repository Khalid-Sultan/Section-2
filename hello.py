def sayHi():
    c=0
    print("hello")
    if c==10:
        return
    else:
        sayHi()
        c=c+1
sayHi()
