#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>

using namespace std;

// Definição da estrutura Aluno
struct InformacoesPessoais {
    string nome;
    string cpf;
};

// Definição da estrutura Prato
struct Prato {
    string nome;
    float notas[5]; // 5 notas para cada prato
};

// Definição da estrutura Concorrente
struct Concorrente {
    InformacoesPessoais infoPessoal;
    Prato pratos[3]; // 3 pratos: entrada, principal e sobremesa
};

// Função para calcular a média das notas de um prato
float calcularMedia(float notas[], int tamanho) {
    float soma = 0;
    for (int i = 0; i < tamanho; i++) {
        soma += notas[i];
    }
    return soma / tamanho;
}

// Função para calcular a média geral dos pratos
float calcularMediaGeral(Concorrente &concorrente) {
    float mediaEntrada = calcularMedia(concorrente.pratos[0].notas, 5);
    float mediaPrincipal = calcularMedia(concorrente.pratos[1].notas, 5);
    float mediaSobremesa = calcularMedia(concorrente.pratos[2].notas, 5);
    return (mediaEntrada + mediaPrincipal + mediaSobremesa) / 3;
}

// Função para cadastrar dados de um concorrente
void cadastrarConcorrente(Concorrente &concorrente) {
    cout << "Cadastro do concorrente:\n";

    cout << "Digite o nome: ";
    getline(cin >> ws, concorrente.infoPessoal.nome); // Lê o nome

    cout << "Digite o CPF: ";
    getline(cin >> ws, concorrente.infoPessoal.cpf); // Lê o CPF

    for (int i = 0; i < 3; i++) { // Para cada prato
        cout << "Digite o nome do prato " << (i == 0 ? "Entrada" : (i == 1 ? "Principal" : "Sobremesa")) << ": ";
        getline(cin >> ws, concorrente.pratos[i].nome); // Lê o nome do prato

        for (int j = 0; j < 5; j++) { // Para cada nota
            cout << "Digite a nota " << (j + 1) << ": ";
            cin >> concorrente.pratos[i].notas[j]; // Lê a nota
        }
    }

    // Salva os dados no arquivo
    ofstream arquivo("candidatos.txt", ios::app);
    
    if (!arquivo.is_open()) {
        cout << "Erro ao abrir o arquivo para gravação." << endl;
        return; // Retorna se não conseguir abrir o arquivo
    }

    // Escreve os dados do concorrente no arquivo
    arquivo << concorrente.infoPessoal.nome << ","
            << concorrente.infoPessoal.cpf << ","
            << concorrente.pratos[0].nome << ",";

    for (int j = 0; j < 5; j++) {
        arquivo << concorrente.pratos[0].notas[j] << (j < 4 ? "," : "");
    }

    arquivo << "," << concorrente.pratos[1].nome << ",";

    for (int j = 0; j < 5; j++) {
        arquivo << concorrente.pratos[1].notas[j] << (j < 4 ? "," : "");
    }

    arquivo << "," << concorrente.pratos[2].nome << ",";

    for (int j = 0; j < 5; j++) {
        arquivo << concorrente.pratos[2].notas[j] << (j < 4 ? "," : "");
    }

    arquivo << endl;
    
    arquivo.close(); // Fecha o arquivo
}

// Função para contar quantos candidatos foram cadastrados
int contarCandidatos() {
    ifstream arquivo("candidatos.txt");
    
    if (!arquivo.is_open()) {
        cout << "Erro ao abrir o arquivo para leitura." << endl;
        return 0; // Retorna zero se não conseguir abrir o arquivo
    }

    int contador = 0;
    string linha;

    while (getline(arquivo, linha)) {
        contador++; // Incrementa o contador para cada linha lida
    }

    arquivo.close(); // Fecha o arquivo
    return contador; // Retorna o número total de candidatos cadastrados
}

// Função principal
int main() {
    Concorrente concorrentes[10]; // Array fixo para armazenar até 10 candidatos
    int totalCandidatos = 0;

    int opcao;

    do {
        cout << "\nMenu:\n";
        cout << "0 - Sair\n";
        cout << "1 - Cadastrar dados de um concorrente\n";
        cout << "2 - Mostrar total de candidatos cadastrados\n";
        cout << "Escolha uma opção: ";
        cin >> opcao;
        cin.ignore(); // Ignora o caractere de nova linha deixado pelo cin

        switch (opcao) {
            case 0:
                break;
            case 1:
                if (totalCandidatos < 10) { // Verifica se ainda há espaço no array fixo
                    cadastrarConcorrente(concorrentes[totalCandidatos]);
                    totalCandidatos++; // Incrementa o contador de candidatos após cadastro
                } else {
                    cout << "Limite de candidatos atingido." << endl;
                }
                break;
            case 2:
                totalCandidatos = contarCandidatos(); // Atualiza o total de candidatos a partir do arquivo
                cout << "Total de candidatos cadastrados: " << totalCandidatos << endl;
                break;
            default:
                cout << "Opção inválida. Tente novamente." << endl;
                break;
        }
        
    } while (opcao != 0);

    return 0; // Sucesso
}

