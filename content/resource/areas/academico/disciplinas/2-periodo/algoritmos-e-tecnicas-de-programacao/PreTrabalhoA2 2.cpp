//CODE GENERATOR
#include <iostream>
#include <iomanip>
#include <string>
#include <math.h>

using namespace std;


//EXEMPLO CALCULO DE MATRIZES DIAGONAL PRINCIPAL E SECUNDARIA;
#define N 3  // Definindo o tamanho da matriz
int main() {
    int matriz[N][N];

    // Preenchendo a matriz com valores
    cout << "Digite os valores para a matriz " << N << "x" << N << ":\n";
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cout << "Elemento [" << i << "][" << j << "]: ";
            cin >> matriz[i][j];
        }
    }

    int diagonalPrincipal = 0, diagonalSecundaria = 0;

    // Calculando a soma da diagonal principal e secundaria
    for (int i = 0; i < N; i++) {
        diagonalPrincipal += matriz[i][i];                // Diagonal principal
        diagonalSecundaria += matriz[i][N - 1 - i];       // Diagonal secundária
    }

    cout << "\nSoma da diagonal principal: " << diagonalPrincipal << endl;
    cout << "Soma da diagonal secundária: " << diagonalSecundaria << endl;

    return 0;
}

//EXEMPLO MATIRZ DE ALUNOS COM NOTAS
#define N_ALUNOS 20  // Número máximo de alunos
int main() {
    string nomes[N_ALUNOS];
    float notas[N_ALUNOS][4]; // Prova A1, Trabalho A1, Prova A2, Trabalho A2
    float a1[N_ALUNOS], a2[N_ALUNOS];
    int n;

    cout << "Digite o número de alunos (máximo " << N_ALUNOS << "): ";
    cin >> n;

    // Entrada de dados
    for (int i = 0; i < n; i++) {
        cout << "\nAluno " << i + 1 << ":\n";
        cout << "Nome: ";
        cin.ignore();
        getline(cin, nomes[i]);
        cout << "Nota Prova A1: ";
        cin >> notas[i][0];
        cout << "Nota Trabalho A1: ";
        cin >> notas[i][1];
        cout << "Nota Prova A2: ";
        cin >> notas[i][2];
        cout << "Nota Trabalho A2: ";
        cin >> notas[i][3];

        a1[i] = (notas[i][0] + notas[i][1]) / 2; // Média A1
        a2[i] = (notas[i][2] + notas[i][3]) / 2; // Média A2
    }

    // Resultados
    for (int i = 0; i < n; i++) {
        cout << "\nAluno: " << nomes[i] << endl;
        cout << "Média A1: " << fixed << setprecision(2) << a1[i] << endl;
        cout << "Média A2: " << fixed << setprecision(2) << a2[i] << endl;
        float mediaFinal = (a1[i] + a2[i]) / 2;
        cout << "Média Final: " << mediaFinal << endl;

        if (mediaFinal >= 6.0)
            cout << "Status: Aprovado" << endl;
        else {
            float falta = 6.0 - mediaFinal;
            cout << "Status: Reprovado, faltaram " << falta << " pontos." << endl;
        }
    }

    return 0;
}

//EXEMPLO JOGO DA VELHA
int main() {
    char tabuleiro[3][3] = {{'1', '2', '3'}, {'4', '5', '6'}, {'7', '8', '9'}};
    int jogador = 1;
    int escolha;
    char marca;
    bool vencedor = false;

    for (int i = 0; i < 9 && !vencedor; i++) {
        // Mostrar tabuleiro
        cout << "\n";
        for (int r = 0; r < 3; r++) {
            for (int c = 0; c < 3; c++) {
                cout << tabuleiro[r][c] << " ";
            }
            cout << "\n";
        }

        jogador = i % 2 + 1;
        marca = (jogador == 1) ? 'X' : 'O';

        cout << "Jogador " << jogador << ", escolha uma posição: ";
        cin >> escolha;

        // Atualizar tabuleiro
        for (int r = 0; r < 3; r++) {
            for (int c = 0; c < 3; c++) {
                if (tabuleiro[r][c] == (char)(escolha + '0')) {
                    tabuleiro[r][c] = marca;
                }
            }
        }

        // Verificar vencedor
        for (int r = 0; r < 3; r++) {
            if (tabuleiro[r][0] == tabuleiro[r][1] && tabuleiro[r][1] == tabuleiro[r][2])
                vencedor = true;
            if (tabuleiro[0][r] == tabuleiro[1][r] && tabuleiro[1][r] == tabuleiro[2][r])
                vencedor = true;
        }
        if (tabuleiro[0][0] == tabuleiro[1][1] && tabuleiro[1][1] == tabuleiro[2][2])
            vencedor = true;
        if (tabuleiro[0][2] == tabuleiro[1][1] && tabuleiro[1][1] == tabuleiro[2][0])
            vencedor = true;
    }

    // Mostrar resultado
    cout << "\n";
    for (int r = 0; r < 3; r++) {
        for (int c = 0; c < 3; c++) {
            cout << tabuleiro[r][c] << " ";
        }
        cout << "\n";
    }

    if (vencedor)
        cout << "Jogador " << jogador << " venceu!\n";
    else
        cout << "Empate!\n";

    return 0;
}

//EXEMPLO JOGO DA FORCA
int main() {
    string palavraSecreta = "BANANA";
    string palavraOculta(palavraSecreta.size(), '_');
    int tentativas = 6;
    char palpite;
    bool acertou;

    while (tentativas > 0 && palavraOculta != palavraSecreta) {
        cout << "\nPalavra: " << palavraOculta << endl;
        cout << "Tentativas restantes: " << tentativas << endl;
        cout << "Digite uma letra: ";
        cin >> palpite;
        palpite = toupper(palpite);
        acertou = false;

        for (int i = 0; i < palavraSecreta.size(); i++) {
            if (palavraSecreta[i] == palpite) {
                palavraOculta[i] = palpite;
                acertou = true;
            }
        }

        if (!acertou) {
            tentativas--;
            cout << "Letra incorreta! Você perdeu uma tentativa.\n";
        }
    }

    if (palavraOculta == palavraSecreta)
        cout << "\nParabéns! Você acertou a palavra: " << palavraSecreta << endl;
    else
        cout << "\nGame Over! A palavra era: " << palavraSecreta << endl;

    return 0;
}
