def hiii(niii):
    print("Hello my first function", niii)


try :
    x = float(input("Enter your first number"))
    y = float(input("Enter your secound number"))

    print(f"So Total of the nnumber is {x + y}")
    hii = input("your name ")
    hiii(hii)

except ValueError :
    print("Invalid innput plz enter only number")
