#include <iostream>
#include "hash.h"
using namespace std;

int hashFunc(int chave) {
    return chave % TAM;
}

TabelaHash* criarTabela() {
    TabelaHash* th = new TabelaHash;
    for(int i = 0; i < TAM; i++) {
        th->tabela[i] = nullptr;
    }
    return th;
}

void destruirTabela(TabelaHash* th) {
    for(int i = 0; i < TAM; i++) {
        if (th->tabela[i] != nullptr) {
            delete th->tabela[i];
        }
    }
    delete th;
}

void inserir(TabelaHash* th, int matricula, string& nome) {
    int indice = hashFunc(matricula);
    if (th->tabela[indice] == nullptr) {
        th->tabela[indice] = new Aluno{matricula, nome, true};
        cout << "Aluno inserido na posicao " << indice << endl;
    } else {
        cout << "Colisao! Posicao " << indice << " ja ocupada." << endl;
    }
}

bool buscar(TabelaHash* th, int matricula, string& nome) {
    int indice = hashFunc(matricula);
    if (th->tabela[indice] != nullptr && th->tabela[indice]->ocupado &&
        th->tabela[indice]->matricula == matricula) {
        nome = th->tabela[indice]->nome;
        return true;
    }
    return false;
}

void remover(TabelaHash* th, int matricula) {
    int indice = hashFunc(matricula);
    if (th->tabela[indice] != nullptr && th->tabela[indice]->ocupado &&
        th->tabela[indice]->matricula == matricula) {
        th->tabela[indice]->ocupado = false;
        cout << "Aluno removido da posicao " << indice << endl;
    } else {
        cout << "Aluno nao encontrado para remocao." << endl;
    }
}

void imprimirTabela(TabelaHash* th) {
    for(int i = 0; i < TAM; i++) {
        cout << "[" << i << "]: ";
        if (th->tabela[i] != nullptr && th->tabela[i]->ocupado) {
            cout << "Matricula: " << th->tabela[i]->matricula
                 << ", Nome: " << th->tabela[i]->nome;
        } else {
            cout << "Vazio";
        }
        cout << endl;
    }
}

