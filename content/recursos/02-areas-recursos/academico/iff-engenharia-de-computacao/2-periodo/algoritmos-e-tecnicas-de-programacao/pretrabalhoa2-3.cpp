//GEMINI
#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

//EXEMPLO CALCULO DE MATRIZES DIAGONAL PRINCIPAL E SECUNDARIA;
#define N 5 // Tamanho da matriz
int main() {
    int matriz[N][N];

    // Preenchendo a matriz (você pode personalizar a forma de preenchimento)
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            matriz[i][j] = i * j; // Exemplo de preenchimento
        }
    }

    // Calculando a soma da diagonal principal
    int soma_diagonal_principal = 0;
    for (int i = 0; i < N; i++) {
        soma_diagonal_principal += matriz[i][i];
    }

    // Calculando a soma da diagonal secundária
    int soma_diagonal_secundaria = 0;
    for (int i = 0; i < N; i++) {
        soma_diagonal_secundaria += matriz[i][N - i - 1];
    }

    // Imprimindo os resultados
    std::cout << "Soma da diagonal principal: " << soma_diagonal_principal << std::endl;
    std::cout << "Soma da diagonal secundária: " << soma_diagonal_secundaria << std.endl;

    return 0;
}


//EXEMPLO MATIRZ DE ALUNOS COM NOTAS
#define N_ALUNOS 20
int main() {
    std::string nomes[N_ALUNOS];
    double notas_a1[N_ALUNOS], notas_a2[N_ALUNOS];

    // Lendo os dados dos alunos
    for (int i = 0; i < N_ALUNOS; i++) {
        std::cout << "Digite o nome do aluno " << i + 1 << ": ";
        std::cin >> nomes[i];
        std::cout << "Digite a nota A1 do aluno " << i + 1 << ": ";
        std::cin >> notas_a1[i];
        std::cout << "Digite a nota A2 do aluno " << i + 1 << ": ";
        std::cin >> notas_a2[i];
    }

    // Calculando as médias e verificando se passou ou não
    for (int i = 0; i < N_ALUNOS; i++) {
        double media = (notas_a1[i] + notas_a2[i]) / 2;
        std::cout << nomes[i] << ": ";
        if (media >= 6) {
            std::cout << "Aprovado(a)" << std::endl;
        } else {
            std::cout << "Reprovado(a). Faltaram " << 6 - media << " pontos." << std::endl;
        }
    }

    return 0;
}

//EXEMPLO JOGO DA VELHA
char tabuleiro[3][3] = {{' ', ' ', ' '}, {' ', ' ', ' '}, {' ', ' ', ' '}};

void imprimir_tabuleiro() {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cout << tabuleiro[i][j] << " ";
        }
        cout << endl;
    }
}

int main() {
    char jogador = 'X';
    int linha, coluna;

    do {
        imprimir_tabuleiro();
        cout << "Jogador " << jogador << ", escolha a linha (1-3): ";
        cin >> linha;
        cout << "Jogador " << jogador << ", escolha a coluna (1-3): ";
        cin >> coluna;

        // Verificar se a posição é válida e marcar no tabuleiro
        if (linha >= 1 && linha <= 3 && coluna >= 1 && coluna <= 3 && tabuleiro[linha - 1][coluna - 1] == ' ') {
            tabuleiro[linha - 1][coluna - 1] = jogador;
        } else {
            cout << "Jogada inválida. Tente novamente." << endl;
            continue;
        }

        // Verificar se alguém venceu (implementação simplificada)
        // ...

        jogador = (jogador == 'X') ? 'O' : 'X';
    } while (/* Condição para continuar o jogo */);

    return 0;
}


//EXEMPLO JOGO DA FORCA
#include <vector>

using namespace std;

int main() {
    string palavraSecreta;
    vector<char> letrasChutadas;
    vector<char> palavraVisivel;

    // Escolhendo a palavra secreta (pode ser aleatória ou inserida pelo usuário)
    cout << "Digite a palavra secreta: ";
    cin >> palavraSecreta;

    // Inicializando o vetor de espaços em branco
    for (char letra : palavraSecreta) {
        palavraVisivel.push_back('_');
    }

    int erros = 0;
    const int MAX_ERROS = 6;

    while (erros < MAX_ERROS && palavraVisivel != palavraSecreta) {
        cout << "Palavra: ";
        for (char letra : palavraVisivel) {
            cout << letra << " ";
        }
        cout << endl;

        char chute;
        cout << "Digite uma letra: ";
        cin >> chute;

        bool acertou = false;
        for (int i = 0; i < palavraSecreta.length(); i++) {
            if (palavraSecreta[i] == chute) {
                palavraVisivel[i] = chute;
                acertou = true;
            }
        }

        if (!acertou) {
            erros++;
            letrasChutadas.push_back(chute);
            cout << "Letra errada! Letras já chutadas: ";
            for (char letra : letrasChutadas) {
                cout << letra << " ";
            }
            cout << endl;
        }
    }

    if (erros == MAX_ERROS) {
        cout << "Você perdeu! A palavra era: " << palavraSecreta << endl;
    } else {
        cout << "Parabéns! Você acertou a palavra!" << endl;
    }

    return 0;
}
