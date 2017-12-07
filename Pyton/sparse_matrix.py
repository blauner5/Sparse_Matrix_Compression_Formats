def CSR():
    b = 0
    f = open ('A.txt', 'r')
    a = [line.split() for line in f]
    for i in range (0,4):
        for j in range (0,5):
            if a[i][j] == 0:
                b = b+1
            else:
                print (a[i][j])
    print "Gli elementi nulli sono:", b
    print "-------------------------------------------"

def COO():
    b = 0
    f = open ('A.txt', 'r')
    a = [line.split() for line in f]
    ele = []
    cols = []
    rows = []
    for i in range (0,4):
        for j in range (0,5):
            if a[i][j] == '0':
                b = b+1
            else:
                ele.append(a[i][j])
                cols.append(j)
                rows.append(i)
    print "-------------------------------------------"
    print "Gli elementi nulli sono:", b
    print "-------------------------------------------\n"
    print "Elementi: "
    for k in ele:
        print k,
    print "\n-------------------------------------------"
    for o in rows:
        print o,
    print "\n-------------------------------------------"
    for m in cols:
        print m,
    print "\n-------------------------------------------"

#---------------------------------------------------------------------------------#
a = 10
while a !=0:
    print "-------------------------------------------"
    print("1)COO \n2)CSR \n0)Exit")
    a = input("Scelta: ")
    print "-------------------------------------------"
    if a == 1:
        print(COO())
    elif a == 2:
        print(CSR())
    else:
        print "Programma terminato."
print "-------------------------------------------"
