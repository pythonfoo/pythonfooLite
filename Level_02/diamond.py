max_width = int(input("Maximale Breite: "))
min_width = 0
zeichen = input("Zeichen: ")
assert len(zeichen) == 1

cur_width = 1
while cur_width * 2 <= max_width:
    print(" " * (max_width - cur_width) + zeichen*(cur_width * 2 - 1))
    cur_width += 1

while cur_width * 2 >= min_width:
    print(" " * (max_width - cur_width) + zeichen*(cur_width * 2 - 1))
    cur_width -= 1
