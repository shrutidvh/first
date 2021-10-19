def div1(a,b):
    try:
        d=a/b
    except ZeroDivisionError:
        print("not divi by 0")
    else:
        print(d)
    finally:
        print("hello world")
div1(2,0)