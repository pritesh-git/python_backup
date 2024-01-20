num = 9
# while num < 5:
#     num = int(input("ENTER ODD NUMBER(n<5): "))
#     if num % 2 == 0:
#         num += 1

"""
        *
       * *
      * * *
     * * * *
    * * * * *
"""
for i in range(num):
    for j in range(num):
        if i + j >= num-1:
            print("*", end=" ")
        else:
            print(end=" ")
    print()


print('\n\n','=-' * 30,'\n\n')  # this is just a division code 
"""
    * * * * * 
     * * * * 
      * * * 
       * * 
        * 
"""
for i in range(num):
   for j in range(num):
       if i <= j:
           print("*", end=" ")
       else:
           print(end=" ")
   print()


print('\n\n','=-' * 30,'\n\n')  # this is just a division code 

"""
    * 
    * * 
    * * * 
    * * * * 
    * * *
    * *  
    *  
"""
for i in range(num):
    for j in range(num):
        if i >= j and i + j < num:
            print("*", end=" ")
    print()


print('\n\n','=-' * 30,'\n\n')  # this is just a division code 

"""
        * 
      * * 
    * * * 
  * * * * 
    * * *
      * *
        * 
"""
for i in range(num):
    for j in range(num):
        if i <= j and i + j >= num - 1:
            print("*", end=" ")
        else:
            print(end="  ")
    print()


print('\n\n','=-' * 30,'\n\n')  # this is just a division code 

"""
    * * * * * 
     * * * * 
      * * * 
       * * 
        * 
        * 
       * * 
      * * * 
     * * * * 
    * * * * * 
"""
for i in range(num * 2):
    for j in range(num):
        if (i < num and i <= j) or (i >= num and (i + j) >= (num*2)-1):
            print("*", end=" ")
        else:
            print(end=" ")
    print()


print('\n\n','=-' * 30,'\n\n')  # this is just a division code 

"""
    *     
    * *    
    * * *   
    * * * *  
    * * * * * 
"""
for i in range(num):
    for j in range(num):
        if i >= j:
            print("*", end=" ")
        else:
            print(end=" ")
    print()


print('\n\n','=-' * 30,'\n\n')  # this is just a division code 

"""
            * 
          * * 
        * * * 
      * * * * 
    * * * * * 
"""
for i in range(num):
    for j in range(num):
        if i + j >= num-1:
            print("*", end=" ")
        else:
            print(end="  ")
    print()


print('\n\n','=-' * 30,'\n\n')  # this is just a division code 

"""
    * * * * * 
    * * * *   
    * * *     
    * *       
    *     
"""
for i in range(num):
    for j in range(num):
        if i + j <= num-1:
            print("*", end=" ")
    print()


print('\n\n','=-' * 30,'\n\n')  # this is just a division code 

"""
    * * * * * 
      * * * * 
        * * * 
          * * 
            * 
"""
for i in range(num):
    for j in range(num):
        if i <= j:
            print("*", end=" ")
        else:
            print(end="  ")
    print()


print('\n\n','=-' * 30,'\n\n')  # this is just a division code 

"""
      * 
     * * 
    * * * 
   * * * * 
    * * * 
     * * 
      * 
"""
for i in range(num):
    for j in range(num):
        if (i < num/2 and (i+j)>=num-1) or (num / 2 <= i <= j):
            print("*", end=" ")
        else:
            print(end=" ")
    print()


print('\n\n','=-' * 30,'\n\n')  # this is just a division code 

"""
       *   
      * *  
     *   * 
    *     *
     *   * 
      * *  
       *   
"""
for i in range(num*2+1):
    for j in range(num*2+1):
        if i+j == num or i+j == (num+(num/2))*2 or j-i == num or i-j == num:
            print("*", end="")
        else:
            print(end=" ")
    print()


print('\n\n','=-' * 30,'\n\n')  # this is just a division code 

"""
    *       * 
    *     *   
    *   *     
    * *       
    *         
    * *       
    *   *     
    *     *   
    *       * 
"""
for i in range(num*2-1):
    for j in range(num):
        if j == 0 or i+j == num-1 or i-j == num-1:
            print("*", end=" ")
        else:
            print(end="  ")
    print()


print('\n\n','=-' * 30,'\n\n')  # this is just a division code 

"""
     * * * * * *
    *           * 
    *           * 
    * * * * * * *
    *           * 
    *           * 
    *           * 
"""
for i in range(num):
    for j in range(num):
        if (j == 0 and i != 0) or (i == 0 and j != num - 1 and j != 0) or (j == num - 1 and i != 0) or i == (num-1)/2:
            print("*", end=" ")
        else:
            print(end="  ")
    print()
