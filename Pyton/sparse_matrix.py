from random import randint

def COO():
    num_ele_null = 0
    f = open ('b.txt', 'r') #Apro il file contenente la matrice
    a = [map(int,line.split(' ')) for line in f] #Leggo la matrice e la salvo su 'a'
    cooValA = [] #Salvo i valori della matrice non nulli
    cooColIndA = [] #Salvo gli indici di colonna
    cooRowIndA = [] #Salvo gli indici di riga
    numrows = len(a) #Salvo la dimensione della matrice (riga)
    numcols = len(a[0]) #Salvo la dimensione della matrice (colonna)
    for i in range (0,numrows):
        for j in range (0,numcols):
            if a[i][j] == 0: #Controllo se i valori della matrice sono nulli
                num_ele_null = num_ele_null+1
            else:
                cooValA.append(a[i][j])
                cooColIndA.append(j)
                cooRowIndA.append(i)
    print "-------------------------------------------"
    print "La dimensione della matrice e':  %dx%d" % (numrows, numcols)
    print "Gli elementi nulli sono:", num_ele_null
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
    print "La dimensione della matrice e':  %dx%d" % (numrows, numcols)
#-----------------------------------------------------------------------------------------#
def CSR():
    num_ele_null = 0
    f = open ('b.txt', 'r') #Apro il file contenente la matrice
    a = [map(int,line.split(' ')) for line in f] #Leggo la matrice e la salvo su 'a'
    csrValA = [] #Salvo i valori della matrice non nulli
    csrColIndA = [] #Salvo gli indici di colonna
    csrRowPtrA = [] #Salvo dove inizia la riga
    numrows = len(a) #Salvo la dimensione della matrice (riga)
    numcols = len(a[0]) #Salvo la dimensione della matrice (colonna)
    csrRowPtrA.append(len(csrColIndA)) #Leggo il numero dell'indice di csrColIndA
    for i in range (0,numrows):
        for j in range (0,numcols):
            if a[i][j] == 0:
                num_ele_null = num_ele_null+1
            else:
                csrValA.append(a[i][j])
                csrColIndA.append(j)
        csrRowPtrA.append(len(csrColIndA))
    print "-------------------------------------------"
    print "La dimensione della matrice e':  %dx%d" % (numrows, numcols)
    print "Gli elementi nulli sono:", num_ele_null
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
    print "La dimensione della matrice e':  %dx%d" % (numrows, numcols)
#-----------------------------------------------------------------------------------------#
def CSC():
    num_ele_null = 0
    f = open ('b.txt', 'r') #Apro il file contenente la matrice
    a = [map(int,line.split(' ')) for line in f] #Leggo la matrice e la salvo su 'a'
    cscValA = [] #Salvo i valori della matrice non nulli
    cscColPtrA = [] #Salvo dove inizia la colonna
    cscRowIndA = [] #Salvo gli indici di riga
    numrows = len(a) #Salvo la dimensione della matrice (riga)
    numcols = len(a[0]) #Salvo la dimensione della matrice (colonna)
    cscColPtrA.append(len(cscRowIndA)) #Leggo il numero dell'indice di cscRowIndA
    for i in range(0,numcols):
        for j in range(0,numrows):
            if a[j][i] == 0:
                num_ele_null = num_ele_null+1
            else:
                cscValA.append(a[j][i])
                cscRowIndA.append(j)
        cscColPtrA.append(len(cscRowIndA))
    print "-------------------------------------------"
    print "La dimensione della matrice e':  %dx%d" % (numrows, numcols)
    print "Gli elementi nulli sono:", num_ele_null
    print "-------------------------------------------\n"
    print "cscValA: "
    for k in cscValA:
        print k,
    print "\n-------------------------------------------"
    print "cscRowIndA: "
    for o in cscRowIndA:
        print o,
    print "\n-------------------------------------------"
    print "cscColPtrA: "
    for m in cscColPtrA:
        print m,
    print "\n-------------------------------------------"
    print "La dimensione della matrice e':  %dx%d" % (numrows, numcols)
#-----------------------------------------------------------------------------------------#
def Converti_menu():
    z = 10
    while z != 0:
        print "Converti"
        print "-------------------------------------------"
        print ("1)COO2CSR \n2)COO2CSC \n---------------------------- \n3)Torna al menu principale \n0)Exit")
        z = input("Scelta: ")
        print "-------------------------------------------"
        if z == 1:
            print "Sto convertendo da COO a CSR..."
        elif z == 2:
            print "Sto convertendo da COO a CSC..."
        elif z == 3:
            print(main())
        elif z == 0:
            print "Programma terminato."
            exit()
        else:
            print "Scelta non valida."
    print "-------------------------------------------"
#-----------------------------------------------------------------------------------------#
#Genero una matrice

def genera(righe, colonne):
    fil = open("b.txt", "w")
    for i in range(0, righe):
        print ("\n"),
        fil.write("\n")
        for j in range(0,colonne):
            a = randint(0, 9)
            print(a),
            fil.write("%d " %a)
#-----------------------------------------------------------------------------------------#
def main():
    a = 10
    while a != 0:
        print "\n-------------------------------------------"
        print("1)COO \n2)CSR \n3)CSC \n4)Genera Matrice \n------------- \n0)Exit")
        a = input("Scelta: ")
        print "-------------------------------------------"
        if a == 1:
            print(COO())
        elif a == 2:
            print(CSR())
        elif a == 3:
            print(CSC())
        elif a == 4:
            z = input ("Righe: ")
            x = input ("Colonne: ")
            genera(z,x)
        #elif a == 4:   nenu converti disabilitato
        #    print(Converti_menu())
        elif a == 0:
            print "Programma terminato."
            exit()
        else:
            print "Scelta non valida."
    print "-------------------------------------------"

if __name__ == "__main__":
    main()
