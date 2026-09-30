#include <iostream>
#include "hash.h"
using namespace std;

int main() {
    TabelaHash* th = criarTabela();
    int opcao, matricula;
    string nome;

    do {
        cout << "\n==== MENU TABELA HASH ====\n";
        cout << "1 - Inserir\n";
        cout << "2 - Buscar\n";
        cout << "3 - Remover\n";
        cout << "4 - Imprimir tabela\n";
        cout << "5 - Sair\n";
        cout << "Escolha uma opcao: ";
        cin >> opcao;

        switch(opcao) {
            case 1:
                cout << "Digite a matricula: ";
                cin >> matricula;
                cin.ignore(); // limpar buffer
                cout << "Digite o nome: ";
                getline(cin, nome);
                inserir(th, matricula, nome);
                break;

            case 2:
                cout << "Digite a matricula para buscar: ";
                cin >> matricula;
                if (buscar(th, matricula, nome)) {
                    cout << "Aluno encontrado: " << nome << endl;
                } else {
                    cout << "Aluno nao encontrado." << endl;
                }
                break;

            case 3:
                cout << "Digite a matricula para remover: ";
                cin >> matricula;
                remover(th, matricula);
                break;

            case 4:
                imprimirTabela(th);
                break;

            case 5:
                cout << "Saindo...\n";
                break;

            default:
                cout << "Opcao invalida.\n";
        }

    } while (opcao != 5);

    destruirTabela(th);
    return 0;
}
