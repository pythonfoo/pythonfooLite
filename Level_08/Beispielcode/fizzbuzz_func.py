# funktionales FizzBuzz

# entweder:
list(map(
    print,
    map(
        lambda t: (
                          (not t % 3)*"fizz" + (not t % 5) * "buzz"
                  ) or str(t),
        range(1, 101)
    )
))


# oder:
[
    print(
        (
            (not t % 3)*"fizz" + (not t % 5) * "buzz"
        ) or str(t)
    )
    for t in range(1, 101)
]
