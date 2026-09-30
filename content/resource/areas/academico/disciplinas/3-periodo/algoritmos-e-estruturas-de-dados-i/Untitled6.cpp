#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>

using namespace std;

// Definição da estrutura InformacoesPessoais
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

// Função para ler os candidatos do arquivo e armazená-los em um array fixo
void lerCandidatos(Concorrente *concorrentes, int totalCandidatos) {
    ifstream arquivo("candidatos.txt");

    if (!arquivo.is_open()) {
        cout << "Erro ao abrir o arquivo para leitura." << endl;
        return; // Retorna se não conseguir abrir o arquivo
    }

    for (int i = 0; i < totalCandidatos; i++) {
        string linha;
        getline(arquivo, linha);
        
        size_t pos = 0;

        // Lê informações pessoais
        pos = linha.find(",");
        concorrentes[i].infoPessoal.nome = linha.substr(0, pos);
        linha.erase(0, pos + 1);

        pos = linha.find(",");
        concorrentes[i].infoPessoal.cpf = linha.substr(0, pos);
        linha.erase(0, pos + 1);

        // Lê pratos e notas
        for (int j = 0; j < 3; j++) { // Para cada prato
            pos = linha.find(",");
            concorrentes[i].pratos[j].nome = linha.substr(0, pos);
            linha.erase(0, pos + 1);

            for (int k = 0; k < 5; k++) { // Para cada nota
                pos = linha.find(",");
                string token = linha.substr(0, pos);
                concorrentes[i].pratos[j].notas[k] = stof(token); // Converte string para float
                linha.erase(0, pos + 1);
            }
        }
    }

    arquivo.close(); // Fecha o arquivo
}

// Função para ordenar os candidatos por nome usando Quick Sort
void quickSortPorNome(Concorrente *concorrentes, int inicio, int fim) {
   if (inicio < fim) {
       string pivot = concorrentes[fim].infoPessoal.nome;
       int i = inicio - 1;

       for (int j = inicio; j < fim; j++) {
           if (concorrentes[j].infoPessoal.nome < pivot) { // Ordena em ordem crescente por nome
               i++;
               swap(concorrentes[i], concorrentes[j]);
           }
       }
       swap(concorrentes[i + 1], concorrentes[fim]);
       int pivoIndex = i + 1;

       quickSortPorNome(concorrentes, inicio, pivoIndex - 1);
       quickSortPorNome(concorrentes, pivoIndex + 1, fim);
   }
}

// Função para exibir todas as informações dos candidatos cadastrados
void exibirCandidatos(Concorrente *concorrentes, int totalCandidatos) {
   cout << fixed << setprecision(2); // Formatação das médias

   cout << "\nInformações dos Candidatos:\n";
   cout << setw(20) << left << "Nome"
        << setw(15) << left << "CPF"
        << setw(20) << left << "Prato Entrada"
        << setw(10) << left << "Média Entrada"
        << setw(20) << left << "Prato Principal"
        << setw(10) << left << "Média Principal"
        << setw(20) << left<< "Prato Sobremesa"
        << setw(10)<< left<< "Média Sobremesa" 
        << endl;

   for (int i = 0; i < totalCandidatos; i++) {
       float mediaEntrada = calcularMedia(concorrentes[i].pratos[0].notas, 5);
       float mediaPrincipal = calcularMedia(concorrentes[i].pratos[1].notas, 5);
       float mediaSobremesa = calcularMedia(concorrentes[i].pratos[2].notas, 5);

       cout<<setw(20)<<left<<concorrentes[i].infoPessoal.nome 
           <<setw(15)<<left<<concorrentes[i].infoPessoal.cpf 
           <<setw(20)<<left<<concorrentes[i].pratos[0].nome 
           <<setw(10)<<left<<mediaEntrada 
           <<setw(20)<<left<<concorrentes[i].pratos[1].nome 
           <<setw(10)<<left<<mediaPrincipal 
           <<setw(20)<<left<<concorrentes[i].pratos[2].nome 
           <<setw(10)<<left<<mediaSobremesa 
           <<" \n";
   }
}

// Função principal
int main() {
   const int maxCandidatos = 10; // Número máximo de candidatos permitidos.
   Concorrente concorrentes[maxCandidatos]; // Array fixo para armazenar os candidatos.
   int totalCandidatos;

   int opcao;

   do {
       cout<<"\nMenu:\n";
       cout<<"0 - Sair\n";
       cout<<"1 - Cadastrar dados de um concorrente\n";
       cout<<"2 - Mostrar total de candidatos cadastrados\n";
       cout<<"3 - Mostrar todos os candidatos\n";
       cout<<"Escolha uma opção: ";
       cin>>opcao;
       cin.ignore(); // Ignora o caractere de nova linha deixado pelo cin

       switch(opcao){
           case 0:
               break;
           case 1:
               totalCandidatos = contarCandidatos(); // Atualiza o total de candidatos a partir do arquivo.
               if(totalCandidatos < maxCandidatos){ // Verifica se ainda há espaço no array fixo.
                   cadastrarConcorrente(concorrentes[totalCandidatos]);
               } else {
                   cout<<"Limite de candidatos atingido."<<endl;
               }
               break;
           case 2:
               totalCandidatos = contarCandidatos(); // Atualiza o total de candidatos a partir do arquivo.
               cout<<"Total de candidatos cadastrados: "<<totalCandidatos<<endl;
               break;
           case 3:
               totalCandidatos = contarCandidatos(); // Atualiza o total de candidatos a partir do arquivo.
               lerCandidatos(concorrentes,totalCandidatos); // Lê os candidatos do arquivo.
               quickSortPorNome(concorrentes,0,totalCandidatos-1); // Ordena os candidatos por nome.
               exibirCandidatos(concorrentes,totalCandidatos); // Exibe as informações dos candidatos.
               break;

