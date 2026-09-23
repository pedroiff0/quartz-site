#include <iostream>
using namespace std;

// Estrutura de um nó da fila
struct No {
    int telefone;      // Valor armazenado no nó (número de telefone)
    No* proximo;     // Ponteiro para o próximo nó na fila
};

// Função para inserir um atendimento na fila
void inserir(No*& inicio, No*& fim, int telefone) {
    // Cria um novo nó
    No* novoNo = new No;
    novoNo->telefone = telefone; // Define o valor do nó
    novoNo->proximo = *inicio;   // O próximo nó é null, pois será o último
    // Não tratando inicio e fim da fila corretamente (sem passar o fim como parâmetro):
    // inicio = novoNo;
    
    //Tratando o caso da fila estar vazia, utilizando o No*& fim
    if (*inicio == nullptr) {
        // Se a fila estiver vazia, o novo nó é o início e o fim
        *inicio = novoNo;
        *fim = novoNo;
    } else {
        // Se não estiver vazia, adiciona o novo nó ao fim da fila
        (*fim)->proximo = novoNo;
        *fim = novoNo;
    }
    cout << "Atendimento inserido: " << telefone << endl;
}

// Função para remover o próximo atendimento da fila
void remover(No*& inicio, No*& fim) {
    if (*inicio == nullptr) {
        cout << "Fila vazia! Nao ha atendimentos para remover.\n";
        return;
    }

    No* temp = *inicio; // Guarda o nó que será removido
    int telefone = temp->telefone; // Salva o valor do nó

    *inicio = (*inicio)->proximo; // Atualiza o início da fila
    delete temp; // Libera a memória do nó removido

    cout << "Atendimento removido: " << telefone << endl;

    // Se a fila ficar vazia após a remoção, atualiza o fim para null
    if (*inicio == nullptr) {
        *fim = nullptr;
    }
}

// Função para visualizar o próximo atendimento
void proximo_atendimento(No* inicio) {
    if (inicio == nullptr) {
        cout << "Fila vazia! Nao ha proximo atendimento.\n";
    } else {
        cout << "Proximo atendimento: " << inicio->telefone << endl;
    }
}

// Função para exibir todos os atendimentos na fila
void exibir(No* inicio) {
    if (inicio == nullptr) {
        cout << "Fila vazia! Nao ha proximo atendimento.\n";
    } else {
        cout << "Proximo atendimento: " << inicio->telefone << endl;
    }

    cout << "Clientes aguardando atendimento:\n";
    No* atual = inicio; // Começa pelo início da fila
    while (atual != nullptr) {
        cout << atual->telefone << endl; // Exibe o valor do nó
        atual = atual->proximo; // Avança para o próximo nó
    }
}

// Função para liberar a memória da fila
void liberar_fila(No*& inicio) {
    while (*inicio != nullptr) {
        remover(inicio, inicio); // Remove todos os nós da fila
    }
}

int main() {
    No* inicio = nullptr; // Ponteiro para o início da fila
    No* fim = nullptr;    // Ponteiro para o fim da fila

    int opcao, telefone;
    do {
        cout << "\n--- Menu de Opcoes ---\n";
        cout << "1. Inserir atendimento\n";
        cout << "2. Remover atendimento\n";
        cout << "3. Visualizar proximo atendimento\n";
        cout << "4. Verificar se a fila esta vazia\n";
        cout << "5. Exibir todos os atendimentos\n";
        cout << "0. Sair\n";
        cout << "Escolha uma opcao: ";
        cin >> opcao;

        switch (opcao) {
            case 1:
                cout << "Digite o numero de telefone: ";
                cin >> telefone;
                inserir(&inicio, &fim, telefone);
                break;
            case 2:
                remover(&inicio, &fim);
                break;
            case 3:
                proximo_atendimento(inicio);
                break;
            case 4:
                if (inicio == nullptr) {
                    cout << "A fila esta vazia.\n";
                } else {
                    cout << "A fila nao esta vazia.\n";
                }
                break;
            case 5:
                exibir(inicio);
                break;
            case 0:
                cout << "Saindo...\n";
                break;
            default:
                cout << "Opcao invalida! Tente novamente.\n";
        }
    } while (opcao != 0);

    liberar_fila(&inicio); // Libera a memória da fila
    return 0;
}
