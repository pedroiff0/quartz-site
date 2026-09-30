#include <iostream>
#include <fstream>
#include <cstdlib>  // para rand() e srand()
#include <ctime>    // para time()
#include <algorithm> // para sort
#include <string>
#include <sstream>
#include <locale.h>
#define MAX 1000

using namespace std;

struct valor {
 	int valor;
 	int segmento;
};

int gerar_valores() {
    ofstream arquivo("entrada.txt");
    if (!arquivo) {
        cerr << "Erro ao criar o arquivo." << endl;
        return 1;
    }

    srand(time(NULL));

    // 1. Define uma quantidade aleatória de números entre 100 e 1000
    int total_numeros = (rand() % (1000 - 100 + 1)) + 100;

    for (int i = 0; i < total_numeros; ++i) {
        // 2. Gera um número aleatório entre 10 e 1000
        int numero = (rand() % (1000 - 10 + 1)) + 10;
        
        arquivo << numero << endl;
    }

    arquivo.close();
    cout << "Arquivo 'entrada.txt' criado com " << total_numeros << " números." << endl;
    return 0;
}

int distribui_simples(int n_caminhos,int  tam_memoria){
	
    // Criar os arquivos fita1.txt at  fitan.txt
    for (int i = 1; i <= n_caminhos; ++i) {
    	stringstream ss;// pq o to_string n o funciona no dev 
		ss << i;
		string nome = "fita" + ss.str() + ".txt";
		ofstream fita(nome.c_str());
		//ofstream fita("fita" + to_string(i) + ".txt");
		        
        if (!fita) {// verifica se criou a fita corretamente
            cerr << "Erro ao criar fita" << i << ".txt" << endl;
            return 1;
        }
        fita.close();// fecha a fita criada
    }

    // Abrir o arquivo de entrada
    ifstream entrada("entrada.txt");
    if (!entrada) {
        cerr << "Erro ao abrir o arquivo entrada.txt" << endl;
        return 1;
    }

    int* memoria = new int[tam_memoria]; // vetor para armazenar o valor que ser  comparado de cada fita
    int contador = 0; //indice do vetor
    int valor; // auxiliar para guardar o valor pego do aqruivo
    int indice_fita = 1; 
    int max_fita = n_caminhos / 2; //metade das fitas para distribui  o e depois usa a outra metade para intercala  o

    while (entrada >> valor) {// pega o valor do arquivo de entrada
        memoria[contador++] = valor; // coloca no vet

        if (contador == tam_memoria) {//quando vetor estiver cheio
            sort(memoria, memoria + tam_memoria);// ordena vetor
            //salvar na fita adequada
            stringstream ss;// pq o to_string n o funciona no dev 
			ss << indice_fita;
			string nome = "fita" + ss.str() + ".txt";
	        ofstream fita(nome.c_str(),ios::app);
            //ofstream fita("fita" + to_string(indice_fita) + ".txt", ios::app);
            for (int i = 0; i < tam_memoria; ++i) {
                fita << memoria[i] << "\n"; // salva o valor do vetor no arquivo de sa da e pula linha
            }
            fita.close();
			// passa para proximo grupo de valores, e proxima fita
            contador = 0;
            indice_fita++;
            if (indice_fita > max_fita)// volta no inicio das fitas validas
                indice_fita = 1;
        }
    }

    // Se restarem valores na mem ria
    if (contador > 0) {// se ainda restar valor no vetor repete o processo com os valores restantes
        sort(memoria, memoria + contador);
        
   		stringstream ss;// pq o to_string n o funciona no dev 
		ss << indice_fita;
		string nome = "fita" + ss.str() + ".txt";
	    ofstream fita(nome.c_str(), ios::app);
        //ofstream fita("fita" + to_string(indice_fita) + ".txt", ios::app);
        
		for (int i = 0; i < contador; ++i) {
            fita << memoria[i] << "\n";
        }
        fita.close();
    }

    delete[] memoria;
    entrada.close();

    cout << "Distribuição concluída nos arquivos fita1.txt até fita " << max_fita << ".txt" << endl;
    return 0;
}

void intercala_fixo(int n_caminhos, int tam_memoria) {
    int n_entrada = n_caminhos / 2; // metade das fitas
    int n_saida = n_caminhos / 2;//n_caminhos - n_entrada;
	int rodada = 0; // vai controlar qual metade das fitas fica como entrada
	int bloco = tam_memoria;  // muda de acordo com a passada
	int inicio_entrada, inicio_saida;
	// cada rodada
	while (bloco < MAX) {// quando o tamanho de bloco for igual ou maior que max,   pq todos os valores est o na mesma fita, ordenados
	//intercala entre arquivos
	inicio_entrada = (rodada % 2 == 0) ? 1 : n_entrada + 1; //se rodada for par entrada come a em 1 , e saida come a na metade p/ frente
	inicio_saida   = (rodada % 2 == 0) ? n_entrada + 1 : 1;
	
    ifstream* entradas = new ifstream[n_entrada];   // Arquivos de entrada 
    ofstream* saidas = new ofstream[n_saida];       // Arquivos de sa da
    for (int i = 0; i < n_entrada; ++i) {
        stringstream ss;
        ss << "fita" << (inicio_entrada+i) << ".txt";
        entradas[i].open(ss.str().c_str());
    }

    // Abrir fitas de sa da para escrita
    for (int i = 0; i < n_saida; i++) {
        stringstream ss;
        ss << "fita" << (inicio_saida+i) << ".txt";
        saidas[i].open(ss.str().c_str());
    }

    int* valores = new int[n_entrada];  // Armazena o valor atual de cada fita
    bool* ativos = new bool[n_entrada]; // Indica se a fita ainda tem valor para ser analisado nessa rodada
    int* usados = new int[n_entrada];    // Contador de quantos valores j  usamos nessa rodada
    int fita_saida = 0;  //  ndice  da fita de sa da atual no vetor de saida
		
    // Inicializa os valores e os status das fitas de entrada
    for (int i = 0; i < n_entrada; i++) {
        if (entradas[i] >> valores[i]) {//pega um valor da entrada e salva no valores  de indice correspondente
            ativos[i] = true;// ativa a fita
            usados[i] = 0; // zera o contador de usados
        } else { // se n o conseguir mais ler valores na fita de entrada
            ativos[i] = false;// bloqueia a fita
        }
    }

    while (true) { // executa para cada grupo do tamanho do bloco
	//ser  quebrado quando todos os arquivos tiverem terminado
        // Encontra o menor valor entre os dispon veis no vetor de valores
		int menor;
        bool primeiro = true;
        for (int i = 0; i < n_entrada; i++) {
            if (ativos[i]) {// considerando apenas as fitas ativas
                if (primeiro || valores[i] < valores[menor]) {
                    menor = i;// guarda posi  o de onde est  o menor
                    primeiro=false;
                }
            }
        }

        if (primeiro) break;

        // Escreve o menor valor na fita de sa da atual
        saidas[fita_saida] << valores[menor] << "\n";
        usados[menor]++; // conta um valor usado

        // se ainda puder ler valores na fita, l  pr ximo valor da fita de onde tiramos o menor
        if (usados[menor] < bloco && entradas[menor] >> valores[menor]) {
            ativos[menor] = true;// mantem o bloco ativo
        } else {// n o h  valores para ler, ou ja leu o tamanho do bloco
            ativos[menor] = false;
        }

        // Se j  usamos 'tam_memoria' valores, passamos para a pr xima fita de sa da
        bool finalizado=true;
        for (int i=0; i< n_entrada; i++)
        	if(ativos[i])
        		finalizado=false;
        	
		if (finalizado) {// prox rodada ate terminar valores do grupo.
            fita_saida = (fita_saida + 1) % n_saida; // Rotaciona entre as fitas de sa da
       		for (int i=0; i< n_entrada; i++)
			   if (entradas[i] >> valores[i]) {
	            ativos[i] = true;
	            usados[i] = 0;
		    	} else {
		            ativos[i] = false;
		        }
		        
	   }
	   // se nao mudar para ativo   pq acabou valores de entrada quando terminar passada
	   finalizado=true;
        for (int i=0; i< n_entrada; i++)
        	if(ativos[i])
        		finalizado=false;
    	if(finalizado) break;
	   
    }
	
    // Fecha todos os arquivos
    for (int i = 0; i < n_entrada; i++) entradas[i].close();
    for (int i = 0; i < n_saida; i++) saidas[i].close();

    delete[] valores;
    delete[] ativos;
    delete[] usados;
    delete[] entradas;
    delete[] saidas;
    
    cout << "Rodada " << rodada + 1 << " concluída (bloco = " << bloco << ").\n"; 
        bloco *= n_entrada;// atualiza o tamanho do bloco                        
        rodada++; // atualiza a rodada, que define quais arquivos ser o usados como leitura e escrita
    }  

cout << " valores ordenados na fita "<<inicio_saida ;

}

int main() {
	gerar_valores();
	int n_caminhos, tam_memoria;
    cout << "Digite o número de caminhos (arquivos): ";
    cin >> n_caminhos;
    cout << "Digite o tamanho da memória (número de inteiros por vez): ";
    cin >> tam_memoria;
    distribui_simples(n_caminhos, tam_memoria);
	intercala_fixo(n_caminhos, tam_memoria);
	
	return 0;
}