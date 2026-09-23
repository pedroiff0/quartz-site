#include <iostream>
#include <fstream>
#include <string>

// Função para abrir um arquivo
bool abrirArquivo(std::ifstream &arquivo, std::string nomeArquivo) {
    arquivo.open(nomeArquivo.c_str()); // Usa c_str() para converter std::string para const char*
    return arquivo.is_open(); // Retorna true se o arquivo foi aberto com sucesso
}

// Função para contar as linhas de um arquivo
int contarLinhas(std::ifstream &arquivo) {
    std::string linha;
    int contador = 0;
    while (std::getline(arquivo, linha)) {
        contador++; // Incrementa o contador para cada linha lida
    }
    return contador; // Retorna o número total de linhas
}

// Função principal
int main() {
    std::ifstream arquivo;
    std::string nomeArquivo = "filename.txt"; // Nome do arquivo

    // Tenta abrir o arquivo
    if (!abrirArquivo(arquivo, nomeArquivo)) {
        std::cerr << "Erro ao abrir o arquivo para leitura." << std::endl;
        return 1; // Retorna erro se não conseguir abrir o arquivo
    }

    // Conta as linhas do arquivo
    int totalLinhas = contarLinhas(arquivo);
    
    // Fecha o arquivo
    arquivo.close();

    // Exibe o resultado
    std::cout << "O arquivo possui " << totalLinhas << " linhas." << std::endl;
    
    return 0; // Sucesso
}

