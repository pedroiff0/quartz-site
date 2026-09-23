#include <iostream>
using namespace std;

int main () {
	//Conversão de Duração em Segundos
	
	int d = 0, h = 0, m = 0, s = 0, calc = 0;
	
	
	cout << "Insira o numero de dias: ";
	cin >> d;

	cout << "Insira o numero de hroas: ";
	cin >> h;
	
	cout << "Insira o numero de minutos: ";
	cin >> m;
	
	cout << "Insira o numero de segundos: ";
	cin >> s;	
	
	if (d > 0 && h > 0 && m > 0 && s >0) {
		calc = ((d*86400) + (h*3600) + (m*60) + s);		
		cout << "Resultado em segundos: " << calc;		
	} else {
		cout << "Valor nao permitido";
	}
}
