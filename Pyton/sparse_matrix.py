def CSR():
    b = 0
    f = open ('A.txt', 'r') #Apro il file contenente la matrice
    a = [line.split() for line in f] #Leggo la matrice e la salvo su 'a'
    f = 0
    csrValA = []
    csrColIndA = []
    csrRowPtrA = []
    csrRowPtrA.append(len(csrColIndA))
    for i in range (0,4):
        for j in range (0,5):
            if a[i][j] == '0':
                b = b+1
            else:
                csrValA.append(a[i][j])
                csrColIndA.append(j)
        csrRowPtrA.append(len(csrColIndA))
    print "-------------------------------------------"
    print "Gli elementi nulli sono:", b
    print "-------------------------------------------\n"
    print "csrValA: "
    for k in csrValA:
        print k,
    print "\n-------------------------------------------"
    print "csrRowPtrA: "
    for o in csrRowPtrA:
        print o,
    print "\n-------------------------------------------"
    print "csrColIndA: "
    for m in csrColIndA:
        print m,
    print "\n-------------------------------------------"

def COO():
    b = 0
    f = open ('A.txt', 'r') #Apro il file contenente la matrice
    a = [line.split() for line in f] #Leggo la matrice e la salvo su 'a'
    cooValA = [] #Salvo i valori della matrice non nulli
    cooColIndA = [] #Salvo gli indici di colonna
    cooRowIndA = [] #Salvo gli indici di riga
    for i in range (0,4):
        for j in range (0,5):
            if a[i][j] == '0': #Controllo se i valori della matrice sono nulli
                b = b+1
            else:
                cooValA.append(a[i][j])
                cooColIndA.append(j)
                cooRowIndA.append(i)
    print "-------------------------------------------"
    print "Gli elementi nulli sono:", b
    print "-------------------------------------------\n"
    print "cooValA: "
    for k in cooValA:
        print k,
    print "\n-------------------------------------------"
    print "cooRowIndA: "
    for o in cooRowIndA:
        print o,
    print "\n-------------------------------------------"
    print "cooColIndA: "
    for m in cooColIndA:
        print m,
    print "\n-------------------------------------------"

#---------------------------------------------------------------------------------#
a = 10
while a != 0:
    print "-------------------------------------------"
    print("1)COO \n2)CSR \n0)Exit")
    a = input("Scelta: ")
    print "-------------------------------------------"
    if a == 1:
        print(COO())
    elif a == 2:
        print(CSR())
    elif a == 0:
        print "Programma terminato."
    else:
        print "Scelta non valida."
print "-------------------------------------------"
