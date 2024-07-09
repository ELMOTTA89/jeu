row=6
cell=7
i=0
j=0
k=0
index=1
while index<=cell:
    print(" ",index,end=" ")
    index+=1
print("")
while i<row:
    print("+",end='')
    while j<cell:
        print("---+",end='')
        j+=1
    print("")
    while k<cell:
        print("|",end='   ')
        k+=1
    print("|")
    k=0
    j=0
    i+=1
print("+",end="")
while j<cell:
    print("---+",end='')
    j+=1
