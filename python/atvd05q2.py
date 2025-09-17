import math
a = int(input("digite um numero"))
b=0
if a == 1:
    print("1 não é primo")
else:
    for i in range (1, a + 1):
        if a % i == 0:
            b+=1
            
        
    if b > 2:
      print("o numero não é primo")          

    else:
        print("é primo")