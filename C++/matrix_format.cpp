#include <iostream>
#include <fstream>

using namespace std;


void test() {
	int val = 0, rows = 0, cols = 0, numItems = 0;
	string line;
	ifstream file("C:\\Users\\ricca\\Desktop\\Sparse_Matrix_Compression_Formats\\C++\\A.txt");
	while (file.peek() != '\n' && file >> val)
	{
		cout << val << ' ';
		++numItems;
	}
	cols = numItems;// # of columns found

	cout << '\n';
	while (file >> val)
	{
		++numItems;
		cout << val << ' ';
		if (numItems%cols == 0) cout << '\n';
	}
	file.close();
	rows = numItems / cols;
	cout << "rows = " << rows << ", cols = " << cols << '\n';
	//creo la nuova matrice
	int** matrix = new int*[rows];
	for (int i = 0; i < rows; ++i)
	{
		matrix[i] = new int[cols];
	}
}
//COO
void COO() {
	int val=0, rows=0, cols=0, numItems=0;
	string line;
	ifstream file("C:\\Users\\ricca\\Desktop\\Sparse_Matrix_Compression_Formats\\C++\\A.txt");
	while(file.peek() != '\n' && file >> val )
    {
        cout << val << ' ';
        ++numItems;
    }
    cols = numItems;// # of columns found

    cout << '\n';
    while(file >> val )
    {
        ++numItems;
        cout << val << ' ';
        if( numItems%cols == 0 ) cout << '\n';
    }
	file.close();
    rows = numItems/cols;
    cout << "rows = " << rows << ", cols = " << cols << '\n';
	//creo la nuova matrice
	int** matrix = new int*[rows];
	for (int i = 0; i < rows; ++i)
	{
		matrix[i] = new int[cols];
	}

	int b = rows + cols;
	int cooValA[10]; //elementi della matrice non zero
	int cooColIndA[10]; //Salvo gli indici
	int cooRowIndA[10]; //Salvo gli row offsets
	int f = 0;
	int i, j;
	int elezero = 0;
	for (i = 0; i < rows; i++) {
		for (j = 0; j < cols; j++) {
			if (matrix[i][j] == 0) { //controllo gli elementi nulli
				elezero = elezero + 1;
			}
			else {
				cooValA[f] = matrix[i][j];
				cooColIndA[f] = j;
				cooRowIndA[f] = i;
				f++;
			}
		}
	}
	cout << "-------------------------------------------------------" << endl;
	cout << "COO: " << endl;
	cout << "La matrice e grande: " << rows << "x" << cols << endl;
	cout << "Gli elementi nulli sono: " << elezero << endl;
	cout << "cooValA: ";
	for (f = 0; f < b; f++) {
		cout << cooValA[f] << " ";

	}
	cout << endl;
	cout << "cooRowIndA: ";
	for (f = 0; f < b; f++) {
		cout << cooRowIndA[f] << " ";

	}
	cout << endl;
	cout << "cooColIndA: ";
	for (f = 0; f < b; f++) {
		cout << cooColIndA[f] << " ";

	}
	cout << endl;
}

//CSR

void CSR() {
	int a[4][5] = {
		{ 1,4,0,0,0 },
		{ 0,2,3,0,0 },
		{ 5,0,0,7,8 },
		{ 0,0,9,0,6 }
	}; //La mia matrice A con elementi nulli
	int rows = sizeof(a) / sizeof(a[0]);  //Controllo la dimensione della matrice righe
	int cols = sizeof(a[0]) / sizeof(a[0][0]); //Controllo la dimensione della matrice colonne
	int b = rows + cols;
	//-----------------ARRAY---------------------//
	int csrValA[10]; //elementi della matrice non zero
	int csrColIndA[10]; //Salvo gli indici
	int csrRowPtrA[10]; //Salvo gli row offsets
	//---------------ARRAY----------------------//
	int f = 0;
	int i, j;
	int elezero = 0;
	for (i = 0; i < rows; i++) {
		csrRowPtrA[i] = f;
		for (j = 0; j < cols; j++) {
			if (a[i][j] == 0) { //controllo gli elementi nulli
				elezero++;
			}
			else {
				csrValA[f] = a[i][j]; //ci salvo gli elementi
				csrColIndA[f] = j;
				f++;
			}
		}
	}
	csrRowPtrA[i] = f;
	cout << "-------------------------------------------------------" << endl;
	cout << "CSR: " << endl;
	cout << "La matrice e grande: " << rows << "x" << cols << endl;
	cout << "Gli elementi nulli sono: " << elezero << endl;
	cout << "csrValA: ";
	for (f = 0; f < b; f++) {
		cout << csrValA[f] << " ";

	}
	cout << endl;
	cout << "csrRowPtrA: ";
	for (f = 0; f < cols; f++) {
		cout << csrRowPtrA[f] << " ";

	}
	cout << endl;
	cout << "csrColIndA: ";
	for (f = 0; f < b; f++) {
		cout << csrColIndA[f] << " ";

	}
	cout << endl;
}

//CSC

void CSC() {
	int a[4][5] = {
		{ 1,4,0,0,0 },
		{ 0,2,3,0,0 },
		{ 5,0,0,7,8 },
		{ 0,0,9,0,6 }
	}; //La mia matrice A con elementi nulli
	int rows = sizeof(a) / sizeof(a[0]);  //Controllo la dimensione della matrice righe
	int cols = sizeof(a[0]) / sizeof(a[0][0]); //Controllo la dimensione della matrice colonne
	int b = rows + cols;
	//-----------------ARRAY---------------------//
	int cscValA[10]; //elementi della matrice non zero
	int cscColPtrA[10]; //Salvo gli indici
	int cscRowIndA[10]; //Salvo gli row offsets
	//---------------ARRAY----------------------//
	int f = 0;
	int i, j = 0;
	int elezero = 0;
	for (i = 0; i < cols; i++) {
		cscColPtrA[i] = f;
		for (j = 0; j < rows; j++) {
			if (a[j][i] == 0) { //controllo gli elementi nulli
				elezero++;
			}
			else {
				cscValA[f] = a[j][i]; //ci salvo gli elementi
				cscRowIndA[f] = j;
				f++;
			}
		}
	}
	cscColPtrA[i] = f;
	cout << "-------------------------------------------------------" << endl;
	cout << "CSC: " << endl;
	cout << "La matrice e grande: " << rows << "x" << cols << endl;
	cout << "Gli elementi nulli sono: " << elezero << endl;
	cout << "cscValA: ";
	for (f = 0; f < b; f++) {
		cout << cscValA[f] << " ";

	}
	cout << endl;
	cout << "cscRowIndA: ";
	for (f = 0; f < b; f++) {
		cout << cscRowIndA[f] << " ";

	}
	cout << endl;
	cout << "cscColPtrA: ";
	for (f = 0; f <= cols; f++) {
		cout << cscColPtrA[f] << " ";

	}
	cout << endl;
}


int main()
{
	int a = 10;
	while (a != 0) {
		cout << "-------------------------------------------------------" << endl;
		cout << "Cosa desideri stampare: " << endl;
		cout << "1) COO" << endl << "2) CSR" << endl << "3) CSC" << endl << "4) TEST" << endl << "0) Exit" << endl;
		cout << "Scelta: ";
		cin >> a;
		if (a == 1) {
			COO();
		}
		else if (a == 2) {
			CSR();
		}
		else if (a == 3) {
			CSC();
		}
		else if (a == 4) {
			test();
		}
		else {
			a == 0;
		}
	}
}
