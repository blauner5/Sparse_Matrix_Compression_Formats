from random import randint
import sys

def COO():
    num_ele_null = 0
    num_ele = 0
    ele_non_null = 0
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
                num_ele = num_ele+1
            else:
                cooValA.append(a[i][j])
                cooColIndA.append(j)
                cooRowIndA.append(i)
                num_ele = num_ele+1
                ele_non_null = ele_non_null+1
    doc = open("out.txt", "w")
    print "-------------------------------------------"
    print "La dimensione della matrice e':  %dx%d" % (numrows, numcols)
    print "Gli elementi sono: ", num_ele
    print "Gli elementi nulli sono:", num_ele_null
    print "Gli elementi non nulli sono: ", ele_non_null
    print "Grandezza degli array in byte: \n"
    grandezza_cooValA = sys.getsizeof(cooValA)
    grandezza_cooColIndA = sys.getsizeof(cooColIndA)
    grandezza_cooRowIndA = sys.getsizeof(cooRowIndA)
    print "Grandezza cooValA: ", grandezza_cooValA
    print "Grandezza cooRowIndA: ", grandezza_cooRowIndA
    print "Grandezza cooColIndA: ", grandezza_cooColIndA
    print "-------------------------------------------\n"
    doc.write("Come leggere il file: \ncooValA cooRowIndA cooColIndA\n")
    print "cooValA: "
    for k in cooValA:
        doc.write("%d " %k),
        #print k,
    print "\n-------------------------------------------"
    doc.write("\n")
    print "cooRowIndA: "
    for o in cooRowIndA:
        doc.write("%d " %o),
        #print o,
    print "\n-------------------------------------------"
    print "cooColIndA: "
    doc.write("\n")
    for m in cooColIndA:
        doc.write("%d " %m),
        #print m,
    print "\n-------------------------------------------"
#-----------------------------------------------------------------------------------------#
def CSR():
    num_ele_null = 0
    num_ele = 0
    ele_non_null = 0
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
                num_ele = num_ele+1
            else:
                csrValA.append(a[i][j])
                csrColIndA.append(j)
                num_ele = num_ele+1
                ele_non_null = ele_non_null+1
        csrRowPtrA.append(len(csrColIndA))
    doc = open("out.txt", "w")
    print "-------------------------------------------"
    print "La dimensione della matrice e':  %dx%d" % (numrows, numcols)
    print "Gli elementi sono: ", num_ele
    print "Gli elementi nulli sono:", num_ele_null
    print "Gli elementi non nulli sono: ", ele_non_null
    grandezza_csrValA = sys.getsizeof(csrValA)
    grandezza_csrRowPtrA = sys.getsizeof(csrRowPtrA)
    grandezza_csrColIndA = sys.getsizeof(csrColIndA)
    print "Grandezza csrValA: ", grandezza_csrValA
    print "Grandezza csrRowPtrA: ", grandezza_csrRowPtrA
    print "Grandezza csrColIndA: ", grandezza_csrColIndA
    print "-------------------------------------------\n"
    doc.write("Come leggere il file: \ncsrValA csrRowPtrA csrColIndA\n")
    print "csrValA: "
    for k in csrValA:
        doc.write("%d " %k)
        #print k,
    print "\n-------------------------------------------"
    doc.write("\n")
    print "csrRowPtrA: "
    for o in csrRowPtrA:
        doc.write("%d " %o)
        #print o,
    print "\n-------------------------------------------"
    doc.write("\n")
    print "csrColIndA: "
    for m in csrColIndA:
        doc.write("%d " %m)
        #print m,
    print "\n-------------------------------------------"
#-----------------------------------------------------------------------------------------#
def CSC():
    num_ele_null = 0
    num_ele = 0
    ele_non_null = 0
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
                num_ele = num_ele+1
            else:
                cscValA.append(a[j][i])
                cscRowIndA.append(j)
                num_ele = num_ele+1
                ele_non_null = ele_non_null+1
        cscColPtrA.append(len(cscRowIndA))
    doc = open("out.txt", "w")
    print "-------------------------------------------"
    print "La dimensione della matrice e':  %dx%d" % (numrows, numcols)
    print "Gli elementi sono: ", num_ele
    print "Gli elementi nulli sono:", num_ele_null
    print "Gli elementi non nulli sono: ", ele_non_null
    grandezza_cscValA = sys.getsizeof(cscValA)
    grandezza_csrRowIndA = sys.getsizeof(cscRowIndA)
    grandezza_csrColPtrA = sys.getsizeof(cscColPtrA)
    print "Grandezza cscValA: ", grandezza_cscValA
    print "Grandezza csrRowIndA: ", grandezza_csrRowIndA
    print "Grandezza csrColPtrA: ", grandezza_csrColPtrA
    print "-------------------------------------------\n"
    doc.write("Come leggere il file: \ncscValA cscRowIndA cscColPtrA\n")
    print "cscValA: "
    for k in cscValA:
        doc.write("%d " %k)
        #print k,
    print "\n-------------------------------------------"
    doc.write("\n")
    print "cscRowIndA: "
    for o in cscRowIndA:
        doc.write("%d " %o)
        #print o,
    print "\n-------------------------------------------"
    print "cscColPtrA: "
    doc.write("\n")
    for m in cscColPtrA:
        doc.write("%d " %m)
        #print m,
    print "\n-------------------------------------------"
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
