"""
    Reference
    A-Z - [65-90]
    a-z - [97-122]
    0-9 - [48-57]
    Special symbols - [0-47,58-64,91-96,123-127]
"""

num = 9
x = 64
# while num < 5:
#     num = int(input("ENTER ODD NUMBER(n<5): "))
#     if num % 2 == 0:
#         num += 1

"""
    A 
    B B 
    C C C 
    D D D D 
    E E E E E 
"""
for i in range(num):
    x += 1
    for j in range(num):
        if i >= j:
            print(chr(x), end=" ")
    print()


print('\n\n','=-' * 30,'\n\n')  # this is just a division code 


"""
        A 
       B C 
      D E F 
     G H I J 
    K L M N O 
"""
x = 64
for i in range(num):
    for j in range(num):
        if i+j >= num-1:
            x += 1
            print(chr(x), end=" ")
        else:
            print(end=" ")
    print()


print('\n\n','=-' * 30,'\n\n')  # this is just a division code 


"""
        A 
       B B 
      C C C 
     D D D D 
    E E E E E 
"""
x = 64
for i in range(num):
    x += 1
    for j in range(num):
        if i + j >= num - 1:
            print(chr(x), end=" ")
        else:
            print(end=" ")
    print()


print('\n\n','=-' * 30,'\n\n')  # this is just a division code 


"""
        A 
       A B 
      A B C 
     A B C D 
    A B C D E 
     F G H I 
      J K L 
       M N 
        O 
"""
for i in range(num):
    x = 65 if i <= num/2 else x
    for j in range(num):
        if (i < num / 2 and (i + j) >= num - 1) or (num / 2 <= i <= j):
            print(chr(x), end=" ")
            x += 1
        else:
            print(end=" ")
    print()
