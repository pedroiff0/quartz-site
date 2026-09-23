//PEDRO
#include <iostream>
#include <string>
#include <iomanip>
using namespace std;



//JOGO DA VELHA
/*
int main () {
	char tabuleiro[3][3] = {{'1', '2', '3'},
                            {'4', '5', '6'},
                            {'7', '8', '9'}};
	int jogador = 1;
	int escolha;
	char marca;
	bool ativo = true;
	
	while (ativo) {
		cout << "\nTabuleiro:\n";
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                cout << tabuleiro[i][j] << " ";
            }
            cout << endl;
        }

	//trocar os jogadores 
	marca = (jogador == 1) ? 'X' : 'O';
	
	cout << "Jogador " << jogador << ", escolha um numero: ";
    cin >> escolha;
	
	switch (escolha) {
            case 1: if (tabuleiro[0][0] == '1') tabuleiro[0][0] = marca; else cout << "Posição já ocupada!\n"; break;
            case 2: if (tabuleiro[0][1] == '2') tabuleiro[0][1] = marca; else cout << "Posição já ocupada!\n"; break;
            case 3: if (tabuleiro[0][2] == '3') tabuleiro[0][2] = marca; else cout << "Posição já ocupada!\n"; break;
            case 4: if (tabuleiro[1][0] == '4') tabuleiro[1][0] = marca; else cout << "Posição já ocupada!\n"; break;
            case 5: if (tabuleiro[1][1] == '5') tabuleiro[1][1] = marca; else cout << "Posição já ocupada!\n"; break;
            case 6: if (tabuleiro[1][2] == '6') tabuleiro[1][2] = marca; else cout << "Posição já ocupada!\n"; break;
            case 7: if (tabuleiro[2][0] == '7') tabuleiro[2][0] = marca; else cout << "Posição já ocupada!\n"; break;
            case 8: if (tabuleiro[2][1] == '8') tabuleiro[2][1] = marca; else cout << "Posição já ocupada!\n"; break;
            case 9: if (tabuleiro[2][2] == '9') tabuleiro[2][2] = marca; else cout << "Posição já ocupada!\n"; break;
            default:
                cout << "Escolha inválida! Tente novamente.\n";
                continue;
        }
    
	for (int i = 0; i < 3; i++) {
        if ((tabuleiro[i][0] == marca && tabuleiro[i][1] == marca && tabuleiro[i][2] == marca) ||
            (tabuleiro[0][i] == marca && tabuleiro[1][i] == marca && tabuleiro[2][i] == marca)) {
            cout << "Jogador " << jogador << " venceu!\n";
            ativo = false;
        }
    }
        if ((tabuleiro[0][0] == marca && tabuleiro[1][1] == marca && tabuleiro[2][2] == marca) ||
            (tabuleiro[0][2] == marca && tabuleiro[1][1] == marca && tabuleiro[2][0] == marca)) {
            cout << "Jogador " << jogador << " venceu!\n";
            ativo = false;
        }

        // Verificando empate
        bool empate = true;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (tabuleiro[i][j] != 'X' && tabuleiro[i][j] != 'O') {
                    empate = false;
                }
            }
        }
        if (empate) {
            cout << "Velha!!\n";
            ativo = false;
        }
        jogador = (jogador == 1) ? 2 : 1;
    }
    return 0;
}
*/


//FORCA
/*
int main () {
	string palavra = "";
	
	//oferta ao usuario de escolher a palavra "multiplayer":
	cout << "Escolha a palavra (tudo minusculo sem acento!): ";
	// guardar toda a linha nao tem como por espaço!
	//	getline(cin, palavra);
	cin >> palavra;
	
	string letrastentativa = "";
	string palavraoculta(palavra.size(), '_');
	int tentativas = 8;
	
	while (tentativas > 0 && palavraoculta!=palavra) {
		cout << "\nPalavra: " << palavraoculta << endl;
        cout << "Tentativas restantes: " << tentativas << endl;
        cout << "Letras tentadas: " << letrastentativa << endl;

        char letra;
        cout << "Digite uma letra: ";
        cin >> letra;

        // Verifica se a letra já foi tentada
        if (letrastentativa.find(letra) != string::npos) {
            cout << "Você já tentou essa letra. Tente outra.\n";
            continue;
        }

        letrastentativa += letra; // Adiciona a letra tentada

        // Verifica se a letra está na palavra
        bool letraEncontrada = false;
        for (int i = 0; i < palavra.size(); i++) {
            if (palavra[i] == letra) {
                palavraoculta[i] = letra; // Revela a letra na palavra oculta
                letraEncontrada = true;
            }
        }
        
        if (!letraEncontrada) {
            tentativas--; // Reduz o número de tentativas se a letra não estiver na palavra
            cout << "Letra não encontrada!\n";
        }
	}
	if (palavraoculta == palavra) {
        cout << "\nParabéns! Você adivinhou a palavra: " << palavra << endl;
  	} else {
        cout << "\nVocê perdeu! A palavra era: " << palavra << endl;
    }
    return 0;
}
*/
