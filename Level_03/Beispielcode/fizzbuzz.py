for i in range(1, 16):
    output = ""
    if i % 3 == 0:
        output += "fizz"
    if i % 5 == 0:
        output += "buzz"
    print(output or i)
