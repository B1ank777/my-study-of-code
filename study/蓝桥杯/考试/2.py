from operator import index

n=int(input())
b_num_list=[]

def get_b(x):
    b_num=""

    while x>0:
        temp=str(x%2)
        x=x//2
        b_num=temp+b_num
    return b_num

def is_all_1(s):
    for i in range(len(s)):
        if s[i]=='0':
            return False
    return True

def cnt_1(s):
    cnt=0
    for x in s:
        if x=='0':
            return cnt
        else:
            cnt+=1

def all_0(l):
    for i in l:
        if i ==1:
            return False
    return True

def get_d(s):
    node =len(s)-1
    value=0
    while node>-1:
        value+=int(s[len(s)-node-1])*(2**node)
        node-=1
    return value

for i in range(1,n+1):
    b_num_list.append(get_b(i))

result=""

for i in range(n):
    if is_all_1(b_num_list[i]):
        result=result+b_num_list[i]
        b_num_list[i]='0'

cnt_first_1s=[]

for i in range(len(b_num_list)):
    cnt_first_1s.append(cnt_1(b_num_list[i]))

while True:
    max_cnt = 0
    index = 0
    for i in range(n):
        if cnt_first_1s[i]>max_cnt:
            max_cnt=cnt_first_1s[i]
            index=i

    result += b_num_list[index]
    cnt_first_1s[index] = 0
    b_num_list[index] = '0'

    if all_0(cnt_first_1s):
        break

print(get_d(result))