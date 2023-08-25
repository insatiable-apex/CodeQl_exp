def perform_op(a,b):
    if type(a) is int and type(b) is int:
        return a+b
    elif type(a) is str and type(b) is str:
        return a+b
    else:
        print("Ivalid Input")


a = 12
b = 1
print(perform_op(a,b))