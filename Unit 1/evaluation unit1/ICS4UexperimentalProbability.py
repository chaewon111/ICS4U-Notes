# 1. coin head, dice even/// 2. dice odd ///3. dice 2~4 경험적인거라 먼저 실행하고 확률계산이래

import random
n= random.randint(100,1000)

def find_probablity(n):
    if n==0:
        return 0
   
    c= random.randint(0,1)
    d1=random.randint(1,6)
    d2=random.randint(1,6) 
    d3=random.randint(1,6)
    if c==0 and d1%2==0 and d2%2==1 and d3>5 or d3<3:
        return 1+ find_probablity(n-1)
    else:
        return find_probablity(n-1)


print('probablity of your wins ',find_probablity(n)/n, '%')

