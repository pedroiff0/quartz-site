#include <iostream>
using namespace std;

struct No {
    int valor;
    No* esquerda;
    No* direita;
};

No* criarNo(int valor) {
    No* novo = new No;
    novo->valor = valor;
    novo->esquerda = nullptr;
    novo->direita = nullptr;
    return novo;
}

No* inserir(No* raiz, int valor) {
    if (raiz == nullptr) {
        return criarNo(valor);
    }
    if (valor < raiz->valor) {
        raiz->esquerda = inserir(raiz->esquerda, valor);
    } else if (valor > raiz->valor) {
        raiz->direita = inserir(raiz->direita, valor);
    }
    return raiz;
}

void imprimirEmOrdem(No* raiz) {
    if (raiz != nullptr) {
        imprimirEmOrdem(raiz->esquerda);
        cout << raiz->valor << " ";
        imprimirEmOrdem(raiz->direita);
    }
}

bool buscar(No* raiz, int valor) {
    if (raiz == nullptr) return false;
    if (raiz->valor == valor) return true;
    if (valor < raiz->valor)
        return buscar(raiz->esquerda, valor);
    else
        return buscar(raiz->direita, valor);
}

No* encontrarMinimo(No* raiz) {
    while (raiz->esquerda != nullptr)
        raiz = raiz->esquerda;
    return raiz;
}

No* remover(No* raiz, int valor) {
    if (raiz == nullptr) return nullptr;

    if (valor < raiz->valor) {
        raiz->esquerda = remover(raiz->esquerda, valor);
    } else if (valor > raiz->valor) {
        raiz->direita = remover(raiz->direita, valor);
    } else {
        if (raiz->esquerda == nullptr && raiz->direita == nullptr) {
            delete raiz;
            return nullptr;
        } else if (raiz->esquerda == nullptr) {
            No* temp = raiz->direita;
            delete raiz;
            return temp;
        } else if (raiz->direita == nullptr) {
            No* temp = raiz->esquerda;
            delete raiz;
            return temp;
        }
        No* sucessor = encontrarMinimo(raiz->direita);
        raiz->valor = sucessor->valor;
        raiz->direita = remover(raiz->direita, sucessor->valor);
    }

    return raiz;
}

void destruirArvore(No* raiz) {
    if (raiz != nullptr) {
        destruirArvore(raiz->esquerda);
        destruirArvore(raiz->direita);
        delete raiz;
    }
}

int main() {
    No* raiz = nullptr;
    int opcao, valor;

    do {
        cout << "\n--- MENU ---\n";
        cout << "1. Inserir valor\n";
        cout << "2. Remover valor\n";
        cout << "3. Buscar valor\n";
        cout << "4. Imprimir em ordem\n";
        cout << "5. Sair\n";
        cout << "Opcao: ";
        cin >> opcao;

        switch (opcao) {
            case 1:
                cout << "Digite o valor a inserir: ";
                cin >> valor;
                raiz = inserir(raiz, valor);
                break;
            case 2:
                cout << "Digite o valor a remover: ";
                cin >> valor;
                raiz = remover(raiz, valor);
                break;
            case 3:
                cout << "Digite o valor a buscar: ";
                cin >> valor;
                if (buscar(raiz, valor))
                    cout << valor << " encontrado na arvore.\n";
                else
                    cout << valor << " nao encontrado.\n";
                break;
            case 4:
                cout << "Arvore em ordem: ";
                imprimirEmOrdem(raiz);
                cout << endl;
                break;
            case 5:
                destruirArvore(raiz);
                cout << "Arvore destruida. Encerrando...\n";
                break;
            default:
                cout << "Opcao invalida!\n";
        }
    } while (opcao != 5);

    return 0;
}
/*
#include <iostream>
using namespace std;

struct No {
    int valor;
    int altura;
    No* esquerda;
    No* direita;
};

int altura(No* no) {
    if (no == nullptr) return 0;
    return no->altura;
}

int max(int a, int b) {
    return (a > b) ? a : b;
}

No* criarNo(int valor) {
    No* novo = new No;
    novo->valor = valor;
    novo->altura = 1;
    novo->esquerda = nullptr;
    novo->direita = nullptr;
    return novo;
}

No* rotacaoDireita(No* y) {
    No* x = y->esquerda;
    No* T2 = x->direita;

    x->direita = y;
    y->esquerda = T2;

    y->altura = max(altura(y->esquerda), altura(y->direita)) + 1;
    x->altura = max(altura(x->esquerda), altura(x->direita)) + 1;

    return x;
}

No* rotacaoEsquerda(No* x) {
    No* y = x->direita;
    No* T2 = y->esquerda;

    y->esquerda = x;
    x->direita = T2;

    x->altura = max(altura(x->esquerda), altura(x->direita)) + 1;
    y->altura = max(altura(y->esquerda), altura(y->direita)) + 1;

    return y;
}

int getBalanceamento(No* no) {
    if (no == nullptr) return 0;
    return altura(no->esquerda) - altura(no->direita);
}

No* inserir(No* raiz, int valor) {
    if (raiz == nullptr)
        return criarNo(valor);

    if (valor < raiz->valor)
        raiz->esquerda = inserir(raiz->esquerda, valor);
    else if (valor > raiz->valor)
        raiz->direita = inserir(raiz->direita, valor);
    else
        return raiz; // duplicatas não são permitidas

    // Atualiza altura
    raiz->altura = 1 + max(altura(raiz->esquerda), altura(raiz->direita));

    // Verifica balanceamento
    int balance = getBalanceamento(raiz);

    // Casos de rotação
    if (balance > 1 && valor < raiz->esquerda->valor)
        return rotacaoDireita(raiz);

    if (balance < -1 && valor > raiz->direita->valor)
        return rotacaoEsquerda(raiz);

    if (balance > 1 && valor > raiz->esquerda->valor) {
        raiz->esquerda = rotacaoEsquerda(raiz->esquerda);
        return rotacaoDireita(raiz);
    }

    if (balance < -1 && valor < raiz->direita->valor) {
        raiz->direita = rotacaoDireita(raiz->direita);
        return rotacaoEsquerda(raiz);
    }

    return raiz;
}

No* encontrarMinimo(No* no) {
    while (no->esquerda != nullptr)
        no = no->esquerda;
    return no;
}

No* remover(No* raiz, int valor) {
    if (raiz == nullptr)
        return raiz;

    if (valor < raiz->valor)
        raiz->esquerda = remover(raiz->esquerda, valor);
    else if (valor > raiz->valor)
        raiz->direita = remover(raiz->direita, valor);
    else {
        if ((raiz->esquerda == nullptr) || (raiz->direita == nullptr)) {
            No* temp = raiz->esquerda ? raiz->esquerda : raiz->direita;

            if (temp == nullptr) {
                temp = raiz;
                raiz = nullptr;
            } else {
                *raiz = *temp;
            }

            delete temp;
        } else {
            No* temp = encontrarMinimo(raiz->direita);
            raiz->valor = temp->valor;
            raiz->direita = remover(raiz->direita, temp->valor);
        }
    }

    if (raiz == nullptr)
        return raiz;

    // Atualiza altura
    raiz->altura = 1 + max(altura(raiz->esquerda), altura(raiz->direita));

    int balance = getBalanceamento(raiz);

    // Casos de rotação
    if (balance > 1 && getBalanceamento(raiz->esquerda) >= 0)
        return rotacaoDireita(raiz);

    if (balance > 1 && getBalanceamento(raiz->esquerda) < 0) {
        raiz->esquerda = rotacaoEsquerda(raiz->esquerda);
        return rotacaoDireita(raiz);
    }

    if (balance < -1 && getBalanceamento(raiz->direita) <= 0)
        return rotacaoEsquerda(raiz);

    if (balance < -1 && getBalanceamento(raiz->direita) > 0) {
        raiz->direita = rotacaoDireita(raiz->direita);
        return rotacaoEsquerda(raiz);
    }

    return raiz;
}

bool buscar(No* raiz, int valor) {
    if (raiz == nullptr) return false;
    if (raiz->valor == valor) return true;
    if (valor < raiz->valor)
        return buscar(raiz->esquerda, valor);
    else
        return buscar(raiz->direita, valor);
}

void imprimirEmOrdem(No* raiz) {
    if (raiz != nullptr) {
        imprimirEmOrdem(raiz->esquerda);
        cout << raiz->valor << " ";
        imprimirEmOrdem(raiz->direita);
    }
}

void destruirArvore(No* raiz) {
    if (raiz != nullptr) {
        destruirArvore(raiz->esquerda);
        destruirArvore(raiz->direita);
        delete raiz;
    }
}

int main() {
    No* raiz = nullptr;
    int opcao, valor;

    do {
        cout << "\n--- MENU AVL ---\n";
        cout << "1. Inserir valor\n";
        cout << "2. Remover valor\n";
        cout << "3. Buscar valor\n";
        cout << "4. Imprimir em ordem\n";
        cout << "5. Sair\n";
        cout << "Opcao: ";
        cin >> opcao;

        switch (opcao) {
            case 1:
                cout << "Digite o valor a inserir: ";
                cin >> valor;
                raiz = inserir(raiz, valor);
                break;
            case 2:
                cout << "Digite o valor a remover: ";
                cin >> valor;
                raiz = remover(raiz, valor);
                break;
            case 3:
                cout << "Digite o valor a buscar: ";
                cin >> valor;
                if (buscar(raiz, valor))
                    cout << valor << " encontrado na arvore.\n";
                else
                    cout << valor << " nao encontrado.\n";
                break;
            case 4:
                cout << "Arvore em ordem: ";
                imprimirEmOrdem(raiz);
                cout << endl;
                break;
            case 5:
                destruirArvore(raiz);
                cout << "Arvore destruida. Encerrando...\n";
                break;
            default:
                cout << "Opcao invalida!\n";
        }
    } while (opcao != 5);

    return 0;
}
*/
