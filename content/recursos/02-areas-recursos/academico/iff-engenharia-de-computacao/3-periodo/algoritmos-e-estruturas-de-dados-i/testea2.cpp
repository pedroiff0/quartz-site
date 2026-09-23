#include <iostream>
#include <fstream>
#include <string>

using namespace std;

// Definindo a estrutura para armazenar os dados do aluno
struct Aluno {
    string nome;
    int matricula;
};

// Função para adicionar um novo aluno ao arquivo
void adicionarAluno(const string& filename) {
    Aluno aluno;

    cout << "Digite o nome do aluno: ";
    cin.ignore(); // Limpa o buffer de entrada
    getline(cin, aluno.nome);
    
    cout << "Digite a matrícula do aluno: ";
    cin >> aluno.matricula;

    ofstream outputFile("filename", ios::app); // Abre o arquivo em modo de append
    if (!outputFile) {
        cerr << "Erro ao abrir o arquivo " << filename << endl;
        return;
    }

    outputFile << aluno.nome << "," << aluno.matricula << endl; // Escreve os dados no arquivo
    outputFile.close();

    cout << "Aluno adicionado com sucesso!" << endl;
}

// Função para contar quantos registros existem no arquivo
int contarRegistros(const string& filename) {
    ifstream inputFile("filename");
    if (!inputFile) {
        cerr << "Erro ao abrir o arquivo " << filename << endl;
        return 0;
    }

    int count = 0;
    string line;
    
    while (getline(inputFile, line)) {
        count++;
    }

    inputFile.close();
    return count;
}

// Função para exibir todos os alunos no arquivo
void exibirAlunos(const string& filename) {
    ifstream inputFile("filename");
    if (!inputFile) {
        cerr << "Erro ao abrir o arquivo " << filename << endl;
        return;
    }

    Aluno aluno;
    cout << "\nLista de Alunos:\n";
    
    while (getline(inputFile, aluno.nome, ',')) { // Lê até a vírgula
        inputFile >> aluno.matricula; // Lê a matrícula
        inputFile.ignore(); // Ignora o caractere de nova linha

        cout << "Nome: " << aluno.nome << ", Matrícula: " << aluno.matricula << endl;
    }

    inputFile.close();
}

// Função para editar um registro existente
void editarAluno(const string& filename) {
    cout << "Digite a matrícula do aluno a ser editado: ";
    int matriculaBusca;
    cin >> matriculaBusca;

    ifstream inputFile("filename");
    if (!inputFile) {
        cerr << "Erro ao abrir o arquivo " << filename << endl;
        return;
    }

    // Criação de um array temporário para armazenar os alunos
    Aluno* alunos = new Aluno[100]; // Supondo um máximo de 100 alunos
    int count = 0;

    // Lê todos os alunos e armazena em um array
    while (getline(inputFile, alunos[count].nome, ',')) {
        inputFile >> alunos[count].matricula; // Lê a matrícula
        inputFile.ignore(); // Ignora o caractere de nova linha
        count++;
    }
    
    inputFile.close();

    // Busca pelo aluno a ser editado
    bool encontrado = false;
    
    for (int i = 0; i < count; i++) {
        if (alunos[i].matricula == matriculaBusca) {
            encontrado = true;
            cout << "Aluno encontrado: Nome: " << alunos[i].nome 
                 << ", Matrícula: " << alunos[i].matricula << endl;

            cout << "Digite o novo nome do aluno: ";
            cin.ignore();
            getline(cin, alunos[i].nome);
            cout << "Digite a nova matrícula do aluno: ";
            cin >> alunos[i].matricula;

            break;
        }
    }

    if (!encontrado) {
        cout << "Aluno não encontrado." << endl;
        delete[] alunos; // Libera memória alocada
        return;
    }

    // Reescreve todos os alunos no arquivo
    ofstream outputFile("filename");
    
    for (int i = 0; i < count; i++) {
        outputFile << alunos[i].nome << "," << alunos[i].matricula << endl; // Escreve os dados no arquivo
    }
    
    outputFile.close();
    
    delete[] alunos; // Libera memória alocada

    cout << "Registro editado com sucesso!" << endl;
}

// Função para particionar o array para Quick Sort
int partition(Aluno arr[], int low, int high) {
    int pivot = arr[high].matricula; // Escolhe a matrícula como pivô
    int i = low - 1; // Índice do menor elemento

    for (int j = low; j < high; j++) {
        if (arr[j].matricula < pivot) { // Se a matrícula atual for menor que o pivô
            i++; // Incrementa o índice do menor elemento
            
            // Troca arr[i] e arr[j] usando uma variável temporária
            Aluno temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }

   // Coloca o pivô na posição correta
   Aluno temp = arr[i + 1];
   arr[i + 1] = arr[high];
   arr[high] = temp;

   return i + 1; // Retorna o índice do pivô
}

// Função Quick Sort para ordenar alunos por matrícula
void quickSort(Aluno arr[], int low, int high) {
   if (low < high) {
       int pi = partition(arr, low, high); // Particiona o array

       quickSort(arr, low, pi - 1); // Ordena a parte esquerda
       quickSort(arr, pi + 1, high); // Ordena a parte direita
   }
}

// Função para ordenar e exibir alunos ordenados por matrícula
void ordenarAlunos(const string& filename) {
   ifstream inputFile("filename");
   if (!inputFile) {
       cerr << "Erro ao abrir o arquivo " << filename << endl;
       return;
   }

   Aluno* alunos = new Aluno[100]; // Supondo um máximo de 100 alunos
   int count = 0;

   while (getline(inputFile, alunos[count].nome, ',')) { 
       inputFile >> alunos[count].matricula; 
       inputFile.ignore(); 
       count++;
   }
   
   inputFile.close();

   quickSort(alunos, 0, count - 1); // Ordena os alunos

   cout << "\nAlunos ordenados por matrícula:\n";
   for (int i = 0; i < count; i++) {
       cout << "Nome: " << alunos[i].nome 
            << ", Matrícula: " << alunos[i].matricula << endl;
   }

   delete[] alunos; // Libera memória alocada
}

int main() {
   const string filename = "alunos.txt";
   int opcao;

   do {
       cout << "\nMenu:\n";
       cout << "1 - Adicionar Aluno\n";
       cout << "2 - Contar Registros\n";
       cout << "3 - Exibir Alunos\n";
       cout << "4 - Editar Aluno\n";
       cout << "5 - Ordenar Alunos\n";
       cout << "0 - Sair\n";
       cout << "Escolha uma opção: ";
       cin >> opcao;

       switch (opcao) {
           case 1:
               adicionarAluno(filename);
               break;
           case 2:
               {
                   int total = contarRegistros(filename);
                   cout << "Total de registros: " << total << endl;
               }
               break;
           case 3:
               exibirAlunos(filename);
               break;
           case 4:
               editarAluno(filename);
               break;
           case 5:
               ordenarAlunos(filename);
               break;
           case 0:
               cout << "Saindo..." << endl;
               break;
           default:
               cout << "Opção inválida. Tente novamente." << endl;
       }
       
   } while (opcao != 0);

   return 0;
}
