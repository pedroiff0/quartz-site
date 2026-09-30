#include <string>
using namespace std;

const int TAM = 10;

struct Aluno {
    int matricula;
    string nome;
    bool ocupado;  // indica se a posição está ocupada
};

struct TabelaHash {
    Aluno* tabela[TAM];
};

// Interface da TAD
TabelaHash* criarTabela();
void destruirTabela(TabelaHash* th);
void inserir(TabelaHash* th, int matricula, string& nome);
bool buscar(TabelaHash* th, int matricula, string& nome);
void remover(TabelaHash* th, int matricula);
void imprimirTabela(TabelaHash* th);


