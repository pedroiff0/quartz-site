#include <iostream>
using namespace std;

// Heap node for k-way merge
typedef struct { int value; int idx; } HeapNode;

// Min-heap insert
void heapInsert(HeapNode heap[], int &size, HeapNode node) {
    int i = size++;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (heap[p].value <= node.value) break;
        heap[i] = heap[p];
        i = p;
    }
    heap[i] = node;
}

// Min-heap remove
HeapNode heapRemoveMin(HeapNode heap[], int &size) {
    HeapNode root = heap[0];
    HeapNode last = heap[--size];
    int i = 0;
    while (true) {
        int l = 2 * i + 1;
        int r = 2 * i + 2;
        if (l >= size) break;
        int s = (r < size && heap[r].value < heap[l].value) ? r : l;
        if (last.value <= heap[s].value) break;
        heap[i] = heap[s];
        i = s;
    }
    heap[i] = last;
    return root;
}

// Round-robin run generation (simulate input array)
int generateRuns(int arr[], int n, int mem, int tapesRuns[], int tapeCount) {
    int tape = 1;
    int runCount = 0;
    for (int i = 0; i < n; i += mem) {
        int end = i + mem < n ? i + mem : n;
        // Insertion sort on arr[i..end-1]
        for (int j = i + 1; j < end; ++j) {
            int key = arr[j];
            int k = j - 1;
            while (k >= i && arr[k] > key) {
                arr[k + 1] = arr[k];
                --k;
            }
            arr[k + 1] = key;
        }
        // Display run generation
        cout << "Run " << runCount + 1 << " sorted on tape " << tape << ": ";
        for (int j = i; j < end; ++j) cout << arr[j] << " ";
        cout << "\n";
        tapesRuns[tape]++;
        ++runCount;
        tape = (tape % (tapeCount - 1)) + 1;
    }
    return runCount;
}

// K-way merge demonstration on in-memory runs
void kWayMergeDemo(int arr[], int n, int mem, int tapesRuns[], int tapeCount) {
    int freeTape = tapeCount;
    HeapNode heap[10]; // max tapes <=10
    int heapSize;
    int pos[10], endPos[10];
    int inputs[10], inCount;

    while (true) {
        // identify input tapes
        inCount = 0;
        for (int t = 1; t < tapeCount; ++t) {
            if (t != freeTape && tapesRuns[t] > 0) inputs[inCount++] = t;
        }
        if (inCount <= 1) break;
        cout << "\nMerging run on free tape " << freeTape << " from tapes:";
        for (int i = 0; i < inCount; ++i) cout << " " << inputs[i];
        cout << "\n";

        // simulate pointers
        int offset = 0;
        for (int i = 0; i < inCount; ++i) {
            pos[i] = offset;
            int runs = tapesRuns[inputs[i]];
            endPos[i] = offset + runs * mem;
            offset = endPos[i];
        }
        heapSize = 0;
        // init heap
        for (int i = 0; i < inCount; ++i) {
            if (pos[i] < endPos[i]) heapInsert(heap, heapSize, HeapNode{arr[pos[i]++], i});
        }
        // merge
        cout << "Merged sequence: ";
        while (heapSize) {
            HeapNode mn = heapRemoveMin(heap, heapSize);
            cout << mn.value << " ";
            int idx = mn.idx;
            if (pos[idx] < endPos[idx]) heapInsert(heap, heapSize, HeapNode{arr[pos[idx]++], idx});
        }
        cout << "\n";

        // update runs: consume one run per input
        for (int i = 0; i < inCount; ++i) tapesRuns[inputs[i]]--;
        tapesRuns[freeTape] = inCount;
        // pick next free
        for (int t = 1; t <= tapeCount; ++t) {
            if (tapesRuns[t] == 0) { freeTape = t; break; }
        }
    }
}

int main() {
    int choice;
    do {
        cout << "\nMenu de Ordenacao:\n";
        cout << "1. Intercalacao Balanceada\n";
        cout << "2. Intercalacao Balanceada Segmento Variado\n";
        cout << "3. Intercalacao Polifasica\n";
        cout << "4. Sair\n";
        cout << "Escolha uma opcao: ";
        cin >> choice;

        if (choice >=1 && choice <=3) {
            cout << "Digite o numero de elementos e limite de memoria por run: ";
            int n, mem; cin >> n >> mem;
            cout << "Digite numero de fitas (>=3): ";
            int F; cin >> F;

            int *arr = new int[n];
            cout << "Digite " << n << " elementos:\n";
            for (int i = 0; i < n; ++i) cin >> arr[i];

            int *runs = new int[F + 1];
            for (int i = 1; i <= F; ++i) runs[i] = 0;

            cout << "\n--- Gerando runs (round-robin) ---\n";
            generateRuns(arr, n, mem, runs, F + 1);

            cout << "\n--- Executando k-way merge ---\n";
            kWayMergeDemo(arr, n, mem, runs, F + 1);

            delete[] arr;
            delete[] runs;
        } else if (choice == 4) {
            cout << "Saindo...\n";
        } else {
            cout << "Opcao invalida!\n";
        }
    } while (choice != 4);

    return 0;
}
