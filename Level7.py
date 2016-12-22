# format
"Das folgende Wort wird ersetzt: '{}' Der Rest nicht.".format("blargh")

# String
>> > s = "a;b;cd"
>> > s.split(";")
['a', 'b', 'cd']
>> > l = s.split(";")
>> > ";".join(l)
'a;b;cd'

# Generatoren und yield
>> > def gen(s):
... for char in s:
... yield char
...
...
>> > for x in gen("abcdef"):
... print(x)

# Dekoratoren
>> > def f(x):
... return x**2
...
>> > f(2)
4
>> > f(3)
9

>> > def dec(func):
... def inner_func(*args):
... print(args)
...         r = func(*args)
... print("Return: {}".format(r))
... return r
... return inner_func
...
>> > @dec
... def f(x):
... return x**2
...
>> > f(2)
(2,)
Return:
    4
4

# Exceptions
>> > try:
...     1 / 0
...
... except ZeroDivisionError as exc:
... print(exc)
...
... finally:
... print("Fertig.")
...
division by zero
Fertig.

# Nett ist auch "raise" innerhalb eines except-Blocks.
