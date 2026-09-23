#include <iostream>
#include <string>
using namespace std;

struct No {
    int valor;
    No* esquerda;
    No* direita;
    No* pai;
};

No* criarNo(int valor) {
    No* novo = new No();
    novo->valor = valor;
    novo->esquerda = nullptr;
    novo->direita = nullptr;
    novo->pai = nullptr;
    return novo;
}

// Função auxiliar para imprimir a árvore de forma hierárquica
void imprimirArvore(No* raiz, int nivel = 0, string prefixo = "") {
    if (raiz == nullptr) return;
    
    string indent = "";
    for (int i = 0; i < nivel; i++) {
        indent += "    ";
    }
    
    cout << indent << prefixo << raiz->valor;
    if (raiz->pai != nullptr) {
        cout << " (pai: " << raiz->pai->valor << ")";
    }
    cout << endl;
    
    imprimirArvore(raiz->esquerda, nivel + 1, "E-- ");
    imprimirArvore(raiz->direita, nivel + 1, "D-- ");
}

No* rotacaoDireita(No* y) {
    cout << "\nRotacao direita em " << y->valor << endl;
    
    No* x = y->esquerda;
    y->esquerda = x->direita;
    
    if (x->direita != nullptr)
        x->direita->pai = y;
    
    x->pai = y->pai;
    
    if (y->pai == nullptr) {
        // y era raiz, agora x será
    } else if (y == y->pai->esquerda) {
        y->pai->esquerda = x;
    } else {
        y->pai->direita = x;
    }
    
    x->direita = y;
    y->pai = x;
    
    cout << "Arvore apos rotacao:" << endl;
    imprimirArvore(x);
    
    return x;
}

No* rotacaoEsquerda(No* x) {
    cout << "\nRotacao esquerda em " << x->valor << endl;
    
    No* y = x->direita;
    x->direita = y->esquerda;
    
    if (y->esquerda != nullptr)
        y->esquerda->pai = x;
    
    y->pai = x->pai;
    
    if (x->pai == nullptr) {
        // x era raiz, agora y será
    } else if (x == x->pai->esquerda) {
        x->pai->esquerda = y;
    } else {
        x->pai->direita = y;
    }
    
    y->esquerda = x;
    x->pai = y;
    
    cout << "Arvore apos rotacao:" << endl;
    imprimirArvore(y);
    
    return y;
}

void splay(No*& raiz, No* x) {
    while (x->pai != nullptr) {
        if (x->pai->pai == nullptr) {
            // Caso Zig
            cout << "\nOperacao Zig em " << x->valor << endl;
            if (x == x->pai->esquerda) {
                raiz = rotacaoDireita(x->pai);
            } else {
                raiz = rotacaoEsquerda(x->pai);
            }
        } else if (x->pai == x->pai->pai->esquerda) {
            if (x == x->pai->esquerda) {
                // Caso Zig-Zig
                cout << "\nOperacao Zig-Zig em " << x->valor << endl;
                rotacaoDireita(x->pai->pai);
                raiz = rotacaoDireita(x->pai);
            } else {
                // Caso Zig-Zag
                cout << "\nOperacao Zig-Zag em " << x->valor << endl;
                rotacaoEsquerda(x->pai);
                raiz = rotacaoDireita(x->pai);
            }
        } else {
            if (x == x->pai->direita) {
                // Caso Zig-Zig
                cout << "\nOperacao Zig-Zig em " << x->valor << endl;
                rotacaoEsquerda(x->pai->pai);
                raiz = rotacaoEsquerda(x->pai);
            } else {
                // Caso Zig-Zag
                cout << "\nOperacao Zig-Zag em " << x->valor << endl;
                rotacaoDireita(x->pai);
                raiz = rotacaoEsquerda(x->pai);
            }
        }
    }
}

No* inserir(No* raiz, int valor) {
    cout << "\nInserindo valor " << valor << endl;
    
    if (raiz == nullptr) {
        No* novo = criarNo(valor);
        cout << "Arvore apos insercao:" << endl;
        imprimirArvore(novo);
        return novo;
    }
    
    No* atual = raiz;
    No* pai = nullptr;
    
    while (atual != nullptr) {
        pai = atual;
        if (valor < atual->valor) {
            atual = atual->esquerda;
        } else if (valor > atual->valor) {
            atual = atual->direita;
        } else {
            cout << "Valor " << valor << " ja existe na arvore." << endl;
            return raiz;
        }
    }
    
    No* novo = criarNo(valor);
    novo->pai = pai;
    
    if (valor < pai->valor) {
        pai->esquerda = novo;
    } else {
        pai->direita = novo;
    }
    
    cout << "Arvore antes do splay:" << endl;
    imprimirArvore(raiz);
    
    splay(raiz, novo);
    
    cout << "Arvore apos splay:" << endl;
    imprimirArvore(novo);
    
    return novo;
}

No* encontrarMinimo(No* no) {
    while (no->esquerda != nullptr) {
        no = no->esquerda;
    }
    return no;
}

No* remover(No* raiz, int valor) {
    cout << "\nRemovendo valor " << valor << endl;
    
    if (raiz == nullptr) {
        cout << "Arvore vazia." << endl;
        return nullptr;
    }
    
    No* atual = raiz;
    No* pai = nullptr;
    
    while (atual != nullptr && atual->valor != valor) {
        pai = atual;
        if (valor < atual->valor) {
            atual = atual->esquerda;
        } else {
            atual = atual->direita;
        }
    }
    
    if (atual == nullptr) {
        cout << "Valor " << valor << " nao encontrado." << endl;
        return raiz;
    }
    
    cout << "Arvore antes do splay:" << endl;
    imprimirArvore(raiz);
    
    splay(raiz, atual);
    
    cout << "Arvore apos splay:" << endl;
    imprimirArvore(raiz);
    
    No* novaRaiz;
    if (raiz->esquerda == nullptr) {
        novaRaiz = raiz->direita;
        if (novaRaiz != nullptr) novaRaiz->pai = nullptr;
    } else if (raiz->direita == nullptr) {
        novaRaiz = raiz->esquerda;
        if (novaRaiz != nullptr) novaRaiz->pai = nullptr;
    } else {
        No* minDireita = encontrarMinimo(raiz->direita);
        raiz->valor = minDireita->valor;
        raiz->direita = remover(raiz->direita, minDireita->valor);
        if (raiz->direita != nullptr) raiz->direita->pai = raiz;
        novaRaiz = raiz;
    }
    
    delete atual;
    
    cout << "Arvore apos remocao:" << endl;
    if (novaRaiz != nullptr) {
        imprimirArvore(novaRaiz);
    } else {
        cout << "Arvore vazia." << endl;
    }
    
    return novaRaiz;
}

bool buscar(No*& raiz, int valor) {
    cout << "\nBuscando valor " << valor << endl;
    
    No* atual = raiz;
    No* pai = nullptr;
    
    while (atual != nullptr) {
        if (atual->valor == valor) {
            cout << "Valor encontrado. Realizando splay..." << endl;
            cout << "Arvore antes do splay:" << endl;
            imprimirArvore(raiz);
            
            splay(raiz, atual);
            raiz = atual;
            
            cout << "Arvore apos splay:" << endl;
            imprimirArvore(raiz);
            
            return true;
        }
        
        pai = atual;
        if (valor < atual->valor) {
            atual = atual->esquerda;
        } else {
            atual = atual->direita;
        }
    }
    
    cout << "Valor nao encontrado. Realizando splay no ultimo no acessado..." << endl;
    if (pai != nullptr) {
        cout << "Arvore antes do splay:" << endl;
        imprimirArvore(raiz);
        
        splay(raiz, pai);
        raiz = pai;
        
        cout << "Arvore apos splay:" << endl;
        imprimirArvore(raiz);
    }
    
    return false;
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
        cout << "\n--- MENU SPLAY ---\n";
        cout << "1. Inserir valor\n";
        cout << "2. Remover valor\n";
        cout << "3. Buscar valor\n";
        cout << "4. Imprimir arvore\n";
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
                cout << "Estrutura da arvore:" << endl;
                imprimirArvore(raiz);
                break;
            case 5:
                destruirArvore(raiz);
                cout << "Arvore destruida. Encerrando...\n";
                break;
            default:
                cout << "Opcao invalida!\n";
                break;
        }
    } while (opcao != 5);
    
    return 0;
}