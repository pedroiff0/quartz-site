#include <iostream>
#include <string>

using namespace std;

struct aluno {
    string nome;
    int matricula;
};

struct horario {
    int hora;
    int minuto;
};

struct registroAluno {
    aluno info;
    horario entrada;
    horario saida;
    bool presente;
};

void registrarEntrada(registroAluno* alunos, int numAlunos, int& contador) {
    if (contador >= numAlunos) {
        cout << "Não há mais espaço para novos registros." << endl;
        return;
    }
    
    cout << "Digite o nome do aluno: ";
    cin >> alunos[contador].info.nome;
    
    cout << "Digite a matrícula do aluno: ";
    cin >> alunos[contador].info.matricula;

    cout << "Digite a hora de entrada (hh mm): ";
    cin >> alunos[contador].entrada.hora >> alunos[contador].entrada.minuto;

    alunos[contador].presente = true;
    contador++; 
}

void registrarSaida(registroAluno* alunos, int contador) {
    int matricula;
    cout << "Digite a matrícula do aluno: ";
    cin >> matricula;

    for (int i = 0; i < contador; i++) {
        if (alunos[i].info.matricula == matricula) {
            if (!alunos[i].presente) {
                cout << "O aluno já saiu." << endl;
                return;
            }

            cout << "Digite a hora de saída (hh mm): ";
            cin >> alunos[i].saida.hora >> alunos[i].saida.minuto;

            // Calcula o tempo de permanência
            int permanenciaHoras = alunos[i].saida.hora - alunos[i].entrada.hora;
            int permanenciaMinutos = alunos[i].saida.minuto - alunos[i].entrada.minuto;

            if (permanenciaMinutos < 0) {
                permanenciaHoras--;
                permanenciaMinutos += 60;
            }

            alunos[i].presente = false; // Marca como ausente
            cout << "Tempo de permanência: " << permanenciaHoras << " horas e " << permanenciaMinutos << " minutos." << endl;
            return;
        }
    }
    
    cout << "Aluno não encontrado." << endl;
}

void pesquisarAluno(registroAluno* alunos, int contador) {
    int matricula;
    cout << "Digite a matrícula do aluno: ";
    cin >> matricula;

    for (int i = 0; i < contador; i++) {
        if (alunos[i].info.matricula == matricula) {
            if (alunos[i].presente) {
                cout << "O aluno está no colégio." << endl;
            } else {
                cout << "O aluno esteve no colégio mas já foi embora." << endl;
            }
            return;
        }
    }

    cout << "O aluno não esteve no colégio." << endl;
}

void mostrarRelatorioDiario(registroAluno* alunos, int contador) {
    cout << "\nRelatório Diário:\n";
    for (int i = 0; i < contador; i++) {
        cout << "Nome: " << alunos[i].info.nome 
             << ", Matrícula: " << alunos[i].info.matricula 
             << ", Horário de Entrada: " 
             << alunos[i].entrada.hora << ":" 
             << (alunos[i].entrada.minuto < 10 ? "0" : "") 
             << alunos[i].entrada.minuto 
             << ", Horário de Saída: ";

        if (alunos[i].presente) {
            cout << "Ainda presente" << endl;
        } else {
            cout << alunos[i].saida.hora << ":" 
                 << (alunos[i].saida.minuto < 10 ? "0" : "") 
                 << alunos[i].saida.minuto 
                 << endl;
        }
    }
}

// Função para particionar o array por matrícula
int partitionByMatricula(registroAluno* alunos, int low, int high) {
    int pivot = alunos[high].info.matricula;
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (alunos[j].info.matricula <= pivot) {
            i++;
            swap(alunos[i], alunos[j]);
        }
    }
    
    swap(alunos[i + 1], alunos[high]);
    return i + 1;
}

int partitionByNome(registroAluno* alunos, int low, int high) {
    string pivot = alunos[high].info.nome; // Pivô é o último elemento
    int i = low - 1; // Índice do menor elemento

    for (int j = low; j < high; j++) {
        if (alunos[j].info.nome <= pivot) { // Compara nomes para ordenação
            i++;
            swap(alunos[i], alunos[j]); // Troca os elementos
        }
    }
    
    swap(alunos[i + 1], alunos[high]); // Coloca o pivô na posição correta
    return i + 1; // Retorna o índice do pivô
}

// Função principal do Quick Sort por matrícula
void quickSortByMatricula(registroAluno* alunos, int low, int high) {
    if (low < high) {
        int pi = partitionByMatricula(alunos, low, high); 
        quickSortByMatricula(alunos, low, pi - 1);
        quickSortByMatricula(alunos, pi + 1, high);
    }
}

// Função principal do Quick Sort por nome
void quickSortByNome(registroAluno* alunos, int low, int high) {
    if (low < high) {
        int pi = partitionByNome(alunos, low, high);

        quickSortByNome(alunos, low, pi - 1);
        quickSortByNome(alunos, pi + 1, high);
    }
}

int main() {
    int numAlunos, contador = 0;

    cout << "Digite o número de alunos da turma: ";
    cin >> numAlunos;

    registroAluno* alunos = new registroAluno[numAlunos];

    int opcao;

    do {
        cout << "\nMenu:\n";
        cout << "0 - Sair\n";
        cout << "1 - Registrar entrada de aluno\n";
        cout << "2 - Registrar saída de aluno\n";
        cout << "3 - Pesquisar aluno\n";
        cout << "4 - Mostrar relatório diário\n";
        cout << "5 - Ordenar lista de alunos por matrícula\n";
        cout << "6 - Ordenar lista de alunos por nome\n"; 
        cout << "Escolha uma opção: ";
        cin >> opcao;

        switch (opcao) {
            case 1:
                registrarEntrada(alunos, numAlunos, contador);
                break;
            case 2:
                registrarSaida(alunos, contador);
                break;
            case 3:
                pesquisarAluno(alunos, contador);
                break;
            case 4:
                mostrarRelatorioDiario(alunos, contador);
                break;
            case 5:
                quickSortByMatricula(alunos, 0, contador - 1);
                cout << "Lista de alunos ordenada por matrícula com sucesso!" << endl;
                break;
            case 6:
                quickSortByNome(alunos, 0, contador - 1);
                cout << "Lista de alunos ordenada por nome com sucesso!" << endl;
                break;
            case 0:
                break;
            default:
                cout << "Opção inválida. Tente novamente." << endl;
        }
        
    } while (opcao != 0);

    delete[] alunos;
    return 0;
}
