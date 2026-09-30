#include <iostream>
#include <fstream>
#include <string>

using namespace std;

// Definindo a estrutura para armazenar os dados do aluno
struct Aluno {
    string nome;
    int matricula;
    float nota; // Nota final do aluno
};

// Função para adicionar um novo aluno ao arquivo
void adicionarAluno(const string& filename) {
    Aluno aluno;

    cout << "Digite o nome do aluno: ";
    cin.ignore(); // Limpa o buffer de entrada
    getline(cin, aluno.nome);
    
    cout << "Digite a matrícula do aluno: ";
    cin >> aluno.matricula;

    cout << "Digite a nota final do aluno: ";
    cin >> aluno.nota;

    ofstream outputFile(filename, ios::app); // Abre o arquivo em modo de append
    if (!outputFile) {
        cerr << "Erro ao abrir o arquivo " << filename << endl;
        return;
    }

    outputFile << aluno.nome << "," << aluno.matricula << "," << aluno.nota << endl; // Escreve os dados no arquivo
    outputFile.close();

    cout << "Aluno adicionado com sucesso!" << endl;
}

// Função para contar quantos registros existem no arquivo
int contarRegistros(const char* filename) {
    ifstream inputFile(filename);
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
void exibirAlunos(const char* filename) {
    ifstream inputFile(filename);
    if (!inputFile) {
        cerr << "Erro ao abrir o arquivo " << filename << endl;
        return;
    }

    Aluno aluno;
    cout << "\nLista de Alunos:\n";
    
    while (getline(inputFile, aluno.nome, ',')) { // Lê até a vírgula
        inputFile >> aluno.matricula; // Lê a matrícula
        inputFile.ignore(); // Ignora o caractere de nova linha
        inputFile >> aluno.nota; // Lê a nota final
        inputFile.ignore(); // Ignora o caractere de nova linha

        cout << "Nome: " << aluno.nome 
             << ", Matrícula: " << aluno.matricula 
             << ", Nota: " << aluno.nota << endl;
    }

    inputFile.close();
}

// Função para buscar um aluno por nome ou matrícula
void buscarAluno(const char* filename) {
    cout << "Escolha a forma de busca:\n";
    cout << "1 - Buscar por Nome\n";
    cout << "2 - Buscar por Matrícula\n";
    
    int escolha;
    cin >> escolha;

    ifstream inputFile(filename);
    if (!inputFile) {
        cerr << "Erro ao abrir o arquivo " << filename << endl;
        return;
    }

    Aluno aluno;
    
    if (escolha == 1) {
        string nomeBusca;
        cout << "Digite o nome do aluno: ";
        cin.ignore();
        getline(cin, nomeBusca);

        bool encontrado = false;

        while (getline(inputFile, aluno.nome, ',')) { 
            inputFile >> aluno.matricula; 
            inputFile.ignore(); 
            inputFile >> aluno.nota; 
            inputFile.ignore(); 

            if (aluno.nome == nomeBusca) {
                encontrado = true;
                cout << "Aluno encontrado: Nome: " << aluno.nome 
                     << ", Matrícula: " << aluno.matricula 
                     << ", Nota: " << aluno.nota << endl;
                break;
            }
        }

        if (!encontrado) {
            cout << "Aluno não encontrado." << endl;
        }
        
    } else if (escolha == 2) {
        int matriculaBusca;
        cout << "Digite a matrícula do aluno: ";
        cin >> matriculaBusca;

        bool encontrado = false;

        while (getline(inputFile, aluno.nome, ',')) { 
            inputFile >> aluno.matricula; 
            inputFile.ignore(); 
            inputFile >> aluno.nota; 
            inputFile.ignore(); 

            if (aluno.matricula == matriculaBusca) {
                encontrado = true;
                cout << "Aluno encontrado: Nome: " << aluno.nome 
                     << ", Matrícula: " << aluno.matricula 
                     << ", Nota: " << aluno.nota << endl;
                break;
            }
        }

        if (!encontrado) {
            cout << "Aluno não encontrado." << endl;
        }
        
    } else {
        cout << "Escolha inválida."<< endl;
    }

    inputFile.close();
}

// Função para particionar o array para Quick Sort (por nome)
int partitionByName(Aluno arr[], int low, int high) {
   Aluno pivot = arr[high]; // Escolhe o último elemento como pivô
   int i = low - 1; 

   for (int j = low; j < high; j++) {
       if (arr[j].nome < pivot.nome) { 
           i++; 
           Aluno temp = arr[i];
           arr[i] = arr[j];
           arr[j] = temp;
       }
   }

   Aluno temp = arr[i + 1];
   arr[i + 1] = arr[high];
   arr[high] = temp;

   return i + 1; 
}

// Função Quick Sort para ordenar alunos por nome
void quickSortByName(Aluno arr[], int low, int high) {
   if (low < high) {
       int pi = partitionByName(arr, low, high); 

       quickSortByName(arr, low, pi - 1); 
       quickSortByName(arr, pi + 1, high); 
   }
}

// Função para particionar o array para Quick Sort (por matrícula)
int partitionByMatricula(Aluno arr[], int low, int high) {
   int pivot = arr[high].matricula; 
   int i = low - 1;

   for (int j = low; j < high; j++) {
       if (arr[j].matricula < pivot) { 
           i++; 
           Aluno temp = arr[i];
           arr[i] = arr[j];
           arr[j] = temp;
       }
   }

   Aluno temp = arr[i + 1];
   arr[i + 1] = arr[high];
   arr[high] = temp;

   return i + 1; 
}

// Função Quick Sort para ordenar alunos por matrícula
void quickSortByMatricula(Aluno arr[], int low, int high) {
   if (low < high) {
       int pi = partitionByMatricula(arr, low, high); 

       quickSortByMatricula(arr, low, pi - 1); 
       quickSortByMatricula(arr, pi + 1, high); 
   }
}

// Função para ordenar e exibir alunos ordenados por nome ou matrícula
void ordenarAlunos(const char* filename) {
   ifstream inputFile(filename);
   if (!inputFile) {
       cerr << "Erro ao abrir o arquivo " << filename << endl;
       return;
   }

   Aluno* alunos = new Aluno[100]; // Supondo um máximo de 100 alunos
   int count = 0;

   while (getline(inputFile, alunos[count].nome, ',')) { 
       inputFile >> alunos[count].matricula; 
       inputFile.ignore(); 
       inputFile >> alunos[count].nota; 
       inputFile.ignore(); 
       count++;
   }
   
   inputFile.close();

   cout << "\nEscolha como deseja ordenar:\n";
   cout << "1 - Por Nome\n";
   cout << "2 - Por Matrícula\n";
   
   int escolha;
   cin >> escolha;

   if (escolha == 1) {
       quickSortByName(alunos, 0, count - 1); // Ordena por nome

       cout << "\nAlunos ordenados por Nome:\n";
       for (int i = 0; i < count; i++) {
           cout << "Nome: " << alunos[i].nome 
                << ", Matrícula: " << alunos[i].matricula 
                << ", Nota: " << alunos[i].nota<< endl;
       }
   } else if (escolha == 2) {
       quickSortByMatricula(alunos, 0, count - 1); // Ordena por matrícula

       cout << "\nAlunos ordenados por Matrícula:\n";
       for (int i = 0; i < count; i++) {
           cout<< "Nome: "<< alunos[i].nome 
               <<" , Matrícula: "<< alunos[i].matricula  
               <<" , Nota: "<< alunos[i].nota<<endl;
       }
   } else {
       cout<< "Escolha inválida."<< endl;
   }

   delete[] alunos; // Libera memória alocada
}

int main() {
   const char* filename = "alunos.txt";
   int opcao;

   do {
       cout<< "\nMenu:\n";
       cout<< "1 - Adicionar Aluno\n";
       cout<< "2 - Contar Registros\n";
       cout<< "3 - Exibir Alunos\n";
       cout<< "4 - Buscar Aluno\n";
       cout<< "5 - Ordenar Alunos\n";
       cout<< "0 - Sair\n";
       cout<< "Escolha uma opção: ";
       cin>> opcao;

       switch(opcao) {
           case 1:
               adicionarAluno(filename);
               break;
           case 2:
               {
                   int total = contarRegistros(filename);
                   cout<< "Total de registros: "<< total<< endl;
               }
               break;
           case 3:
               exibirAlunos(filename);
               break;
           case 4:
               buscarAluno(filename);
               break;
           case 5:
               ordenarAlunos(filename);
               break;
           case 0:
               cout<< "Saindo..."<< endl;
               break;
           default:
               cout<< "Opção inválida. Tente novamente."<< endl;
       }
       
   } while(opcao != 0);

   return 0;
}

