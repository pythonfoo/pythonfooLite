def fizz_buzz(number: int) -> str:
    output = ""
    if number % 3 == 0:
        output += "fizz"
    if number % 5 == 0:
        output += "buzz"
    return output or str(number)

for val in map(fizz_buzz, range(1, 16)):
    print(val)
