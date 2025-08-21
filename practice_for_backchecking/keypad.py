keypad =((1,2,3),
         (4,5,6),
         (7,8,9),
         ("*",0,'#') )
for key in keypad:
    for numbers in key:
        print(numbers, end=" ")
    print()