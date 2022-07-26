import sys

n = int(sys.stdin.readline().rstrip())
n_list = list(map(int, sys.stdin.readline().rstrip().split()))

score=0
count=0
 
for i in range(n):
    if n_list[i]==1:
        if count>=1:
            count+=1
            score+=count
        else:
            count+=1
            score+=1 
    else:
        count=0
        score+=0
 
 
print(score)