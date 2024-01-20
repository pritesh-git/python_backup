num = 9
# while num < 5:
#     num = int(input("ENTER ODD NUMBER(n<5): "))
#     if num % 2 == 0:
#         num += 1

"""
    1 
    2 2 
    3 3 3 
    4 4 4 4 
    5 5 5 5 5 
"""
for i in range(num):
    for j in range(num):
        if i >= j:
            print(i+1, end=" ")
    print()

print('\n\n','=-' * 30,'\n\n')  # this is just a division code 


"""
    1 
    1 2 
    1 2 3 
    1 2 3 4 
    1 2 3 4 5 
"""
for i in range(num):
    for j in range(num):
        if i >= j:
            print(j+1, end=" ")
    print()

print('\n\n','=-' * 30,'\n\n')  # this is just a division code 


"""
    1 
    2 3 
    4 5 6 
    7 8 9 10 
    11 12 13 14 15 
"""
x = 1
for i in range(num):
    for j in range(num):
        if i >= j:
            print(x, end=" ")
            x += 1
    print()

print('\n\n','=-' * 30,'\n\n')  # this is just a division code 


"""
    1 2 3 4 5 
    1 2 3 4 
    1 2 3 
    1 2 
    1 
"""
for i in range(num):
    for j in range(num):
        if i + j <= num-1:
            print(j+1, end=" ")
    print()

print('\n\n','=-' * 30,'\n\n')  # this is just a division code 


"""
    1 
    2 2 
    3 3 3 
    4 4 4 4 
    5 5 5 5 5 
"""
for i in range(num):
    for j in range(num):
        if i >= j:
            print(j+1, end=" ")
    print()

print('\n\n','=-' * 30,'\n\n')  # this is just a division code 


"""
               1
             1   1
           1   2   1
         1   3   3   1
       1   4   6   4   1
     1   5   10   10   5   1
   1   6   15   20   15   6   1
"""
for i in range(num):
    c = 1
    for j in range(1, num - i):
        print(end=" ")

    for k in range(0, i + 1):
        print(c, end=" ")
        c = int(c * (i - k) / (k + 1))
    print()

print('\n\n','=-' * 30,'\n\n')  # this is just a division code 


"""
        1 
       2 2 
      3 3 3 
     4 4 4 4 
    5 5 5 5 5 
     4 4 4 4 
      3 3 3 
       2 2 
        1 
"""
for i in range(num):
    for j in range(num):
        if (i < num / 2 and (i + j) >= num - 1) or (num / 2 <= i <= j):
            print(i + 1 if i < num / 2 else num - i, end=" ")
        else:
            print(end=" ")
    print()

print('\n\n','=-' * 30,'\n\n')  # this is just a division code 


"""
        10
       1010
      101010
     10101010
    1010101010
"""
for i in range(num):
    for j in range(num):
        if i + j >= num-1:
            print("10", end="")
        else:
            print(end=" ")
    print()
