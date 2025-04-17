l=list((input()))
after_sort_list=[]

while l!=[]:
    index=0
    ch=l[index]
    for i in range(len(l)):
        if ch > l[i]:
            index=i
            ch=l[i]
    after_sort_list.append(ch)
    del l[index]

print(''.join(after_sort_list))