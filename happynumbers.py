from random import randint
def happynumber(n):
    a =n;
    visited = set()
    while 1:
        if a == 1:
            '''print "Number is happy!"
            break'''
            return True
        a = sum(int(c) ** 2 for c in str(a))
        if a in visited:
            '''print "Number is sad!"
            break'''
            return False
        visited.add(a)

lis=[]
for num in range(1,1001):
# prime numbers are greater than 1
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
            elif str(num) not in lis:
                lis.append(str(num))
fr=open("prime.txt","w")

for i in lis:
    fr.write(i)
    fr.write("\n")
fr.close()
fw=open("rand.txt","a+")
for i in range(1,1001):
    while(1):
        tem=str(randint(1,1000))
        check=happynumber(tem)
        if check==True:
            fw.write(tem)
            fw.write("\n")
            break
fw.close()

fr=open("prime.txt","r")
fw=open("rand.txt","r")

common=[]
for i in fr.readlines():
    fw.seek(0)
    for j in fw.readlines():
        if int(i)==int(j) and int(i) not in common:
            common.append(int(i))
print(common)
