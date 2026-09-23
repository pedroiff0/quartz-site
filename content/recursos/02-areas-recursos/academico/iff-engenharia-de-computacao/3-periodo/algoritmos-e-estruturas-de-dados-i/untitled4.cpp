#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>

using namespace std;

// Estrutura para armazenar informações pessoais do candidato
struct InformacoesPessoais {
    string nome;
    string cpf;
};

// Estrutura para armazenar informações dos pratos
struct Prato {
    string nome;
    float notas[5]; // 5 notas para cada prato
};

// Estrutura para armazenar informações do concorrente
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

// Função para ordenar os concorrentes por média geral usando Quick Sort
void quickSort(Concorrente *concorrentes, int inicio, int fim) {
    if (inicio < fim) {
        float pivot = calcularMediaGeral(concorrentes[fim]);
        int i = inicio - 1;

        for (int j = inicio; j < fim; j++) {
            if (calcularMediaGeral(concorrentes[j]) > pivot) { // Ordena em ordem decrescente
                i++;
                swap(concorrentes[i], concorrentes[j]);
            }
        }
        swap(concorrentes[i + 1], concorrentes[fim]);
        int pivoIndex = i + 1;

        quickSort(concorrentes, inicio, pivoIndex - 1);
        quickSort(concorrentes, pivoIndex + 1, fim);
    }
}

// Função para cadastrar dados de um concorrente
void cadastrarConcorrente(Concorrente *concorrentes, int index) {
    cout << "Cadastro do concorrente " << index + 1 << endl;

    cout << "Digite o nome: ";
    getline(cin >> ws, concorrentes[index].infoPessoal.nome); // Lê o nome

    cout << "Digite o CPF: ";
    getline(cin >> ws, concorrentes[index].infoPessoal.cpf); // Lê o CPF

    for (int i = 0; i < 3; i++) { // Para cada prato
        cout << "Digite o nome do prato " << (i == 0 ? "Entrada" : (i == 1 ? "Principal" : "Sobremesa")) << ": ";
        getline(cin >> ws, concorrentes[index].pratos[i].nome); // Lê o nome do prato

        for (int j = 0; j < 5; j++) { // Para cada nota
            cout << "Digite a nota " << (j + 1) << ": ";
            cin >> concorrentes[index].pratos[i].notas[j]; // Lê a nota
        }
    }

    // Salva os dados no arquivo
    ofstream arquivo("candidatos.txt", ios::app);
    arquivo << concorrentes[index].infoPessoal.nome << ","
            << concorrentes[index].infoPessoal.cpf << ","
            << concorrentes[index].pratos[0].nome << ",";

    for (int j = 0; j < 5; j++) {
        arquivo << concorrentes[index].pratos[0].notas[j] << (j < 4 ? "," : "");
    }

    arquivo << "," << concorrentes[index].pratos[1].nome << ",";

    for (int j = 0; j < 5; j++) {
        arquivo << concorrentes[index].pratos[1].notas[j] << (j < 4 ? "," : "");
    }

    arquivo << "," << concorrentes[index].pratos[2].nome << ",";

    for (int j = 0; j < 5; j++) {
        arquivo << concorrentes[index].pratos[2].notas[j] << (j < 4 ? "," : "");
    }

    arquivo << endl;
    arquivo.close();
}

// Função para mostrar todos os candidatos e suas médias por pratos
void mostrarCandidatos(Concorrente *concorrentes, int totalCandidatos) {
    cout << fixed << setprecision(2); // Formatação das médias

    for (int i = 0; i < totalCandidatos; i++) {
        cout << "Nome: " << concorrentes[i].infoPessoal.nome 
             << ", CPF: " << concorrentes[i].infoPessoal.cpf 
             << ", Media Entrada: " << calcularMedia(concorrentes[i].pratos[0].notas, 5)
             << ", Media Principal: " << calcularMedia(concorrentes[i].pratos[1].notas, 5)
             << ", Media Sobremesa: " << calcularMedia(concorrentes[i].pratos[2].notas, 5)
             << ", Media Geral: " << calcularMediaGeral(concorrentes[i]) 
             << endl;
    }
}

// Função principal
int main() {
    int totalCandidatos;
    
    cout << "Quantos candidatos foram inscritos? ";
    cin >> totalCandidatos;

    // Alocação dinâmica de memória
    Concorrente *concorrentes = new Concorrente[totalCandidatos];
    
    int opcao;

    do {
        cout << "\nMenu:\n";
        cout << "0 - Sair do cadastramento\n";
        cout << "1 - Cadastrar dados de um concorrente\n";
        cout << "2 - Mostrar todos os candidatos\n";
        cout << "Escolha uma opção: ";
        cin >> opcao;
        cin.ignore(); // Ignora o caractere de nova linha deixado pelo cin

        switch (opcao) {
            case 0:
                break;
            case 1:
                for (int i = 0; i < totalCandidatos; i++) {
                    cadastrarConcorrente(concorrentes, i);
                }
                break;
            case 2:
                mostrarCandidatos(concorrentes, totalCandidatos);
                break;
            default:
                cout << "Opção inválida. Tente novamente." << endl;
                break;
        }
        
    } while (opcao != 0);

    // Ordena os candidatos por média geral
    quickSort(concorrentes, 0, totalCandidatos - 1);

    // Mostra ranking dos três primeiros colocados
    cout << "\nRanking dos três primeiros colocados:\n";
    
    for (int i = 0; i < min(3, totalCandidatos); i++) {
        cout << i + 1 << ". Nome: " 
             << concorrentes[i].infoPessoal.nome 
             << ", Média Geral: "
             << calcularMediaGeral(concorrentes[i]) 
             << endl;
    }

    delete[] concorrentes; // Libera a memória alocada

    return 0; // Sucesso
}

