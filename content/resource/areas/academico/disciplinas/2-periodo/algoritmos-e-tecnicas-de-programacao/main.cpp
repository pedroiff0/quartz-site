#include <iostream>

using namespace std;

void pedro () {
	cout << "menu começando agora: \n1 gays\n2heteros";
}

int main() {
	int escolha;
	
	pedro();
	cin >> escolha;
	
	/**
	do{
		cout <<"vc conseguiu viu seu coco";
		cout << "0 para, continuar?";
		cin >> escolha;
	} while(escolha!=0);
	**/
	
	switch (escolha) {
		case 1:
			cout << "vc eh gay";
			break;
		case 2: 
			cout << "vc eh hetero";
			break;
		case 0: 
			cout << "vc parou";
			break;			
	}
	
	
};
