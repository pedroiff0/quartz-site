//Perplexity
#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

//MATRIZ DIAGONAIS
#define N 3 // Dimensão da matriz
int main() {
    int matriz[N][N];

    // Preenchendo a matriz
    cout << "Preencha a matriz " << N << "x" << N << ":\n";
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cout << "Elemento [" << i << "][" << j << "]: ";
            cin >> matriz[i][j];
        }
    }

    // Exibindo a matriz
    cout << "\nMatriz:\n";
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cout << setw(4) << matriz[i][j];
        }
        cout << endl;
    }

    // Cálculo da soma da diagonal principal e secundária
    int somaDiagonalPrincipal = 0, somaDiagonalSecundaria = 0;
    for (int i = 0; i < N; i++) {
        somaDiagonalPrincipal += matriz[i][i]; // Diagonal principal
        somaDiagonalSecundaria += matriz[i][N - 1 - i]; // Diagonal secundária
    }

    cout << "\nSoma da Diagonal Principal: " << somaDiagonalPrincipal << endl;
    cout << "Soma da Diagonal Secundária: " << somaDiagonalSecundaria << endl;

    return 0;
}

//EXEMPLO JOGO DA VELHA
int main() {
    char tabuleiro[3][3] = {{'1', '2', '3'},
                            {'4', '5', '6'},
                            {'7', '8', '9'}};
    int jogador = 1; // Jogador 1 e 2
    int escolha;
    char marca; // X ou O
    bool jogoAtivo = true;

    while (jogoAtivo) {
        // Exibindo o tabuleiro
        cout << "Tabuleiro:\n";
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                cout << tabuleiro[i][j] << " ";
            }
            cout << endl;
        }

        // Alternando jogadores
        jogador = (jogador % 2) ? 1 : 2;
        marca = (jogador == 1) ? 'X' : 'O';

        // Escolha do jogador
        cout << "Jogador " << jogador << ", escolha um número: ";
        cin >> escolha;

        // Atualizando o tabuleiro
        switch (escolha) {
            case 1: tabuleiro[0][0] = marca; break;
            case 2: tabuleiro[0][1] = marca; break;
            case 3: tabuleiro[0][2] = marca; break;
            case 4: tabuleiro[1][0] = marca; break;
            case 5: tabuleiro[1][1] = marca; break;
            case 6: tabuleiro[1][2] = marca; break;
            case 7: tabuleiro[2][0] = marca; break;
            case 8: tabuleiro[2][1] = marca; break;
            case 9: tabuleiro[2][2] = marca; break;
            default:
                cout << "Escolha inválida! Tente novamente.\n";
                continue;
        }

        // Verificando vitória (linhas, colunas e diagonais)
        for (int i = 0; i < 3; i++) {
            if ((tabuleiro[i][0] == marca && tabuleiro[i][1] == marca && tabuleiro[i][2] == marca) ||
                (tabuleiro[0][i] == marca && tabuleiro[1][i] == marca && tabuleiro[2][i] == marca)) {
                cout << "Jogador " << jogador << " venceu!\n";
                jogoAtivo = false;
            }
        }
        if ((tabuleiro[0][0] == marca && tabuleiro[1][1] == marca && tabuleiro[2][2] == marca) ||
            (tabuleiro[0][2] == marca && tabuleiro[1][1] == marca && tabuleiro[2][0] == marca)) {
            cout << "Jogador " << jogador << " venceu!\n";
            jogoAtivo = false;
        }

        // Verificando empate
        bool empate = true;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (tabuleiro[i][j] != 'X' && tabuleiro[i][j] != 'O') {
                    empate = false;
                }
            }
        }
        if (empate) {
            cout << "Empate!\n";
            jogoAtivo = false;
        }
    }

    return 0;
}

//EXEMPLO NOTAS ALUNOS
#define N_ALUNOS 20
#define N_NOTAS 8 // 4 notas + 4 médias + 1 situação
int main() {
    string nomes[N_ALUNOS];
    float notas[N_ALUNOS][N_NOTAS]; // Matriz de notas

    // Coletando dados dos alunos
    for (int i = 0; i < N_ALUNOS; i++) {
        cout << "Digite o nome do aluno " << (i + 1) << ": ";
        cin >> nomes[i];

        cout << "Nota do Trabalho 1 (T1): ";
        cin >> notas[i][0];
        cout << "Nota da Prova 1 (P1): ";
        cin >> notas[i][1];
        cout << "Nota do Trabalho 2 (T2): ";
        cin >> notas[i][2];
        cout << "Nota da Prova 2 (P2): ";
        cin >> notas[i][3];

        // Calculando médias
        notas[i][4] = (notas[i][0] + notas[i][1]) / 2; // Média A1
        notas[i][5] = (notas[i][2] + notas[i][3]) / 2; // Média A2
        notas[i][6] = (notas[i][4] + notas[i][5]) / 2; // Média Final

        // Verificando se passou ou reprovou
        if (notas[i][6] >= 6) {
            notas[i][7] = 1; // Aprovado
        } else {
            notas[i][7] = 0; // Reprovado
        }
    }

    // Exibindo resultados
    cout << "\nResultados:\n";
    cout << setw(20) << "Nome" << setw(10) << "A1" << setw(10) << "A2" << setw(10) << "Final" << setw(10) << "Situação" << endl;
    for (int i = 0; i < N_ALUNOS; i++) {
        cout << setw(20) << nomes[i] 
             << setw(10) << notas[i][6] 
             << setw(10) << (notas[i][7] == 1 ? "Aprovado" : "Reprovado") << endl;
    }

    return 0;
}

//JOGO DA FORCA
int main() {
    string palavra = "PROGRAMACAO"; // Palavra a ser adivinhada
    string letrasTentadas = ""; // Letras já tentadas
    string palavraOculta = ""; // Palavra oculta
    int tentativas = 6; // Número de tentativas

    // Inicializando a palavra oculta com underscores
    for (int i = 0; i < palavra.length(); i++) {
        palavraOculta += "_";
    }

    while (tentativas > 0 && palavraOculta != palavra) {
        cout << "\nPalavra: " << palavraOculta << endl;
        cout << "Tentativas restantes: " << tentativas << endl;
        cout << "Letras tentadas: " << letrasTentadas << endl;

        char letra;
        cout << "Digite uma letra: ";
        cin >> letra;
        letra = toupper(letra); // Converte para maiúscula

        // Verifica se a letra já foi tentada
        if (letrasTentadas.find(letra) != string::npos) {
            cout << "Você já tentou essa letra. Tente outra.\n";
            continue;
        }

        letrasTentadas += letra; // Adiciona a letra tentada

        // Verifica se a letra está na palavra
        bool letraEncontrada = false;
        for (int i = 0; i < palavra.length(); i++) {
            if (palavra[i] == letra) {
                palavraOculta[i] = letra; // Revela a letra na palavra oculta
                letraEncontrada = true;
            }
        }

        if (!letraEncontrada) {
            tentativas--; // Reduz o número de tentativas se a letra não estiver na palavra
            cout << "Letra não encontrada!\n";
        }
    }

    // Verifica se o jogador ganhou ou perdeu
    if (palavraOculta == palavra) {
        cout << "\nParabéns! Você adivinhou a palavra: " << palavra << endl;
    } else {
        cout << "\nVocê perdeu! A palavra era: " << palavra << endl;
    }

    return 0;
}
