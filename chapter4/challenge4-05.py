try:
    a=input("数を入力")
    b=input("数を入力")
    a=int(a)
    b=int(b)
    print(float(a/b))
except(ZeroDivisionError,ValueError):
    print("Invalid input")

