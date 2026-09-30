#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <sstream>

using namespace std;

struct HeapNode {
    int segmento;
    int valor;
    int fitaOriginal;
};

void gerarNumerosAleatorios(int total, bool usarSequenciaFixa = true) {
    ofstream arquivo("numeros.txt");
    if (!arquivo) {
        cerr << "Erro ao criar numeros.txt" << endl;
        exit(1);
    }

    if (usarSequenciaFixa) {
        int fixos[] = {
            5, 28, 10, 40, 35, 7, 12, 6, 21, 11,
            29, 27, 9, 38, 8, 49, 3, 15, 13, 30,
            17, 46, 18, 36, 1, 4, 34, 16, 19, 22
        };
        int qtdFixos = sizeof(fixos) / sizeof(fixos[0]);
        for (int i = 0; i < qtdFixos; i++) {
            arquivo << fixos[i] << "\n";
        }
    } else {
        srand((unsigned)time(nullptr));
        for (int i = 0; i < total; i++) {
            arquivo << (rand() % 100) << "\n";
        }
    }

    arquivo.close();
}

void heapifyUp(HeapNode heap[], int idx) {
    while (idx > 0) {
        int pai = (idx - 1) / 2;
        if (heap[idx].segmento < heap[pai].segmento ||
            (heap[idx].segmento == heap[pai].segmento && heap[idx].valor < heap[pai].valor)) {
            swap(heap[idx], heap[pai]);
            idx = pai;
        } else {
            break;
        }
    }
}

void heapifyDown(HeapNode heap[], int heapSize, int idx) {
    while (true) {
        int menor = idx;
        int esq = 2 * idx + 1;
        int dir = 2 * idx + 2;

        if (esq < heapSize &&
            (heap[esq].segmento < heap[menor].segmento ||
             (heap[esq].segmento == heap[menor].segmento && heap[esq].valor < heap[menor].valor))) {
            menor = esq;
        }
        if (dir < heapSize &&
            (heap[dir].segmento < heap[menor].segmento ||
             (heap[dir].segmento == heap[menor].segmento && heap[dir].valor < heap[menor].valor))) {
            menor = dir;
        }
        if (menor != idx) {
            swap(heap[idx], heap[menor]);
            idx = menor;
        } else {
            break;
        }
    }
}

void distribuirPolifasica(int numFitas, int tamanhoHeap) {
    ifstream arquivoEntrada("numeros.txt");
    if (!arquivoEntrada) {
        cerr << "Erro ao abrir numeros.txt" << endl;
        exit(1);
    }

    int metade = numFitas / 2;  // metade para distribuição

    ofstream* fitas = new ofstream[numFitas];
    for (int i = 0; i < numFitas; i++) {
        string nomeArquivo = "Arq" + to_string(i + 1) + ".txt";
        fitas[i].open(nomeArquivo, ios::trunc);
        if (!fitas[i]) {
            cerr << "Erro ao abrir " << nomeArquivo << endl;
            exit(1);
        }
    }

    HeapNode* heap = new HeapNode[tamanhoHeap];
    int heapSize = 0;

    int segmentoAtual = 0;
    int fitaSaidaAtual = 0;

    int ultimoValorExtraido = -1;

    int valorLido;
    while (heapSize < tamanhoHeap && (arquivoEntrada >> valorLido)) {
        HeapNode novo;
        novo.fitaOriginal = -1;
        novo.segmento = 0;
        novo.valor = valorLido;

        heap[heapSize++] = novo;
        heapifyUp(heap, heapSize - 1);
    }

    bool* primeiroValorNaFita = new bool[metade];
    for (int i = 0; i < metade; i++) primeiroValorNaFita[i] = true;

    cout << "Início da extração e distribuição:" << endl;

    while (heapSize > 0) {
        HeapNode min = heap[0];

        // if (!primeiroValorNaFita[fitaSaidaAtual]) fitas[fitaSaidaAtual];
        fitas[fitaSaidaAtual] << min.segmento << "-" << min.valor << "\n";
        primeiroValorNaFita[fitaSaidaAtual] = false;

        cout << "[Extração] Valor " << min.valor << " do segmento " << min.segmento
             << " => Escrevendo na fita de saída " << fitaSaidaAtual + 1 << endl;

        heap[0] = heap[--heapSize];
        if (heapSize > 0) heapifyDown(heap, heapSize, 0);

        if (min.segmento == segmentoAtual) {
            ultimoValorExtraido = min.valor;
        }

        if (arquivoEntrada >> valorLido) {
            HeapNode novo;
            novo.fitaOriginal = -1;

            if (valorLido < ultimoValorExtraido) {
                novo.segmento = min.segmento + 1;
                cout << ">> Novo segmento iniciado: " << novo.segmento
                     << " para valor " << valorLido << endl;
            } else {
                novo.segmento = min.segmento;
            }
            novo.valor = valorLido;

            heap[heapSize++] = novo;
            heapifyUp(heap, heapSize - 1);

            cout << "[Inserção] Valor " << valorLido << " do segmento " << novo.segmento
                 << " inserido no heap" << endl;
        }

        if (heapSize > 0 && heap[0].segmento > segmentoAtual) {
            segmentoAtual = heap[0].segmento;
            fitaSaidaAtual = (fitaSaidaAtual + 1) % metade;
            ultimoValorExtraido = -1;
            cout << ">> Segmento atual mudou para " << segmentoAtual
                 << ", fita saída agora é " << fitaSaidaAtual + 1 << endl;
        }
    }

    for (int i = 0; i < metade; i++) {
        // fitas[i] << ";" << endl;
        fitas[i].close();
    }

    delete[] heap;
    delete[] primeiroValorNaFita;
    delete[] fitas;
}

void intercalarPolifasica(int numFitas, int tamanhoHeap) {
    int fitasEntrada = numFitas / 2;
    int fitasSaida = numFitas - fitasEntrada;

    ifstream* entrada = new ifstream[fitasEntrada];
    ofstream* saida = new ofstream[fitasSaida];

    // Abre fitas de entrada
    for (int i = 0; i < fitasEntrada; i++) {
        string nome = "Arq" + to_string(i + 1) + ".txt";
        entrada[i].open(nome);
        if (!entrada[i]) {
            cerr << "Erro ao abrir " << nome << " para leitura\n";
            exit(1);
        }
        cout << "Aberto para leitura: " << nome << endl;
    }

    // Abre fitas de saída
    for (int i = 0; i < fitasSaida; i++) {
        string nome = "Arq" + to_string(fitasEntrada + i + 1) + ".txt";
        saida[i].open(nome, ios::trunc);
        if (!saida[i]) {
            cerr << "Erro ao abrir " << nome << " para escrita\n";
            exit(1);
        }
        cout << "Aberto para escrita: " << nome << endl;
    }

    struct Item {
        int valor;
        int origem;
        int segmento;
    };

    Item* heap = new Item[tamanhoHeap];
    int heapSize = 0;

    auto lerProximo = [&](int id, int& val) -> bool {
        string linha;
        if (getline(entrada[id], linha)) {
            size_t pos = linha.find('-');
            if (pos != string::npos) {
                val = stoi(linha.substr(pos + 1));
                return true;
            }
        }
        return false;
    };

    for (int i = 0; i < fitasEntrada && heapSize < tamanhoHeap; i++) {
        int val;
        if (lerProximo(i, val)) {
            heap[heapSize++] = { val, i, 0 };
            cout << "Inicial: fita " << i + 1 << ", valor " << val << endl;
        }
    }

    auto cmp = [](const Item& a, const Item& b) {
        if (a.segmento != b.segmento) return a.segmento > b.segmento;
        return a.valor > b.valor;
    };

    make_heap(heap, heap + heapSize, cmp);

    int fitaSaidaAtual = 0;
    int ultimoSegmento = 0;
    bool primeiroNaFita = true;

    while (heapSize > 0) {
        pop_heap(heap, heap + heapSize, cmp);
        Item atual = heap[--heapSize];

        if (atual.segmento != ultimoSegmento) {
            fitaSaidaAtual = (fitaSaidaAtual + 1) % fitasSaida;
            ultimoSegmento = atual.segmento;
            primeiroNaFita = true;
            cout << "Mudança para segmento " << ultimoSegmento << " -> Fita saída " << fitaSaidaAtual + fitasEntrada + 1 << endl;
        }

        saida[fitaSaidaAtual] << atual.segmento << "-" << atual.valor << "\n";
        primeiroNaFita = false;

        cout << "Extraindo valor " << atual.valor << " da fita " << atual.origem + 1
             << " para fita saída " << fitaSaidaAtual + fitasEntrada + 1 << endl;

        int novoValor;
        if (lerProximo(atual.origem, novoValor)) {
            int novoSegmento = (novoValor < atual.valor) ? atual.segmento + 1 : atual.segmento;
            heap[heapSize++] = { novoValor, atual.origem, novoSegmento };
            push_heap(heap, heap + heapSize, cmp);
        }
    }

    for (int i = 0; i < fitasEntrada; i++) entrada[i].close();
    for (int i = 0; i < fitasSaida; i++) saida[i].close();
    delete[] entrada;
    delete[] saida;
    delete[] heap;

    cout << "Intercalação polifásica concluída.\n";

    // ==== Etapa final: intercalação k-way dos arquivos Arq3.txt e Arq4.txt ====

    ifstream* finalIn = new ifstream[fitasSaida];
    ofstream finalOut("arquivoFinal.txt", ios::trunc);
    if (!finalOut) {
        cerr << "Erro ao abrir arquivoFinal.txt\n";
        exit(1);
    }
    cout << "\nIniciando intercalação final...\n";

    for (int i = 0; i < fitasSaida; i++) {
        string nome = "Arq" + to_string(fitasEntrada + i + 1) + ".txt";
        finalIn[i].open(nome);
        if (!finalIn[i]) {
            cerr << "Erro ao abrir " << nome << " para leitura final\n";
            exit(1);
        }
        cout << "Aberto para leitura: " << nome << endl;
    }

    struct FItem {
        int valor;
        int origem;
    };

    FItem* heapFinal = new FItem[fitasSaida];
    int hSize = 0;

    auto lerValorFinal = [&](int id, int& val) -> bool {
        string linha;
        if (getline(finalIn[id], linha)) {
            size_t pos = linha.find('-');
            if (pos != string::npos) {
                val = stoi(linha.substr(pos + 1));
                return true;
            }
        }
        return false;
    };

    for (int i = 0; i < fitasSaida; i++) {
        int val;
        if (lerValorFinal(i, val)) {
            heapFinal[hSize++] = { val, i };
        }
    }

    auto menor = [](const FItem& a, const FItem& b) {
        return a.valor > b.valor;
    };

    make_heap(heapFinal, heapFinal + hSize, menor);

    while (hSize > 0) {
        pop_heap(heapFinal, heapFinal + hSize, menor);
        FItem atual = heapFinal[--hSize];
        finalOut << atual.valor << "\n";

        int val;
        if (lerValorFinal(atual.origem, val)) {
            heapFinal[hSize++] = { val, atual.origem };
            push_heap(heapFinal, heapFinal + hSize, menor);
        }
    }

    for (int i = 0; i < fitasSaida; i++) finalIn[i].close();
    finalOut.close();
    delete[] finalIn;
    delete[] heapFinal;

    cout << "Intercalação final concluída em arquivoFinal.txt\n";
}

int main() {
    int numFitas, tamanhoHeap;

    gerarNumerosAleatorios(0, true);

    cout << "Número total de fitas (par, mínimo 2): ";
    cin >> numFitas;
    if (numFitas < 2 || numFitas % 2 != 0) {
        cerr << "Erro: número de fitas deve ser par e >= 2." << endl;
        return 1;
    }

    cout << "Tamanho do heap (buffer): ";
    cin >> tamanhoHeap;
    if (tamanhoHeap <= 0) {
        cerr << "Erro: tamanho inválido." << endl;
        return 1;
    }

    cout << "Distribuindo." << endl;
    distribuirPolifasica(numFitas, tamanhoHeap);
    cout << "Distribuição concluída." << endl;

    cout << "Intercalando." << endl;
    intercalarPolifasica(numFitas, tamanhoHeap);
    cout << "\nIntercalação concluída. Resultado final salvo em ArqFinal.txt\n";

    return 0;
}