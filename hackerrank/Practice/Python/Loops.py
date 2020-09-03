if __name__ == '__main__':
    n = int(input())

i = 0
list1 = [ ]
list2 = list(range(i,n))
for i in list2:
    j = i*i
    list1.append(j)
print(*list1, sep = '\n')




