#include <iostream>
#include <fstream>
#include <cstdlib>  // para rand() e srand()
#include <ctime>    // para time()
#include <algorithm> // para sort
#include <string>
#include <sstream>
#include <locale.h>
#define MAX 20

using namespace std;
typedef struct valor {
 	int valor;
 	int segmento;
};

int gerar_valores(){
	ofstream arquivo("entrada.txt"); // cria arquivo e abre para escrita
    if (!arquivo) {// verifica se criou
        cerr << "Erro ao criar o arquivo." << endl;
        return 1;
    }

    srand(time(NULL)); // semente para n�meros aleat�rios com base no horario do so
    for (int i = 0; i < MAX; ++i) {// repete para quantos ns quiser criar
        int numero = rand() % 100; // n�mero aleat�rio de 0 a 99
        arquivo << numero << endl; // escreve o n�mero no aqruivo e pula de linha
    }
    arquivo.close();// fecha arquivo
    cout << "Arquivo 'entrada.txt' criado com "<<MAX<<" n�meros aleat�rios." << endl;
}

int distribui_simples(int n_caminhos,int  tam_memoria){
	
    // Criar os arquivos fita1.txt at� fitan.txt
    for (int i = 1; i <= n_caminhos; ++i) {
    	stringstream ss;// pq o to_string n�o funciona no dev 
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

    int* memoria = new int[tam_memoria]; // vetor para armazenar o valor que ser� comparado de cada fita
    int contador = 0; //indice do vetor
    int valor; // auxiliar para guardar o valor pego do aqruivo
    int indice_fita = 1; 
    int max_fita = n_caminhos / 2; //metade das fitas para distribui��o e depois usa a outra metade para intercala��o

    while (entrada >> valor) {// pega o valor do arquivo de entrada
        memoria[contador++] = valor; // coloca no vet

        if (contador == tam_memoria) {//quando vetor estiver cheio
            sort(memoria, memoria + tam_memoria);// ordena vetor
            //salvar na fita adequada
            stringstream ss;// pq o to_string n�o funciona no dev 
			ss << indice_fita;
			string nome = "fita" + ss.str() + ".txt";
	        ofstream fita(nome.c_str(),ios::app);
            //ofstream fita("fita" + to_string(indice_fita) + ".txt", ios::app);
            for (int i = 0; i < tam_memoria; ++i) {
                fita << memoria[i] << "\n"; // salva o valor do vetor no arquivo de sa�da e pula linha
            }
            fita.close();
			// passa para proximo grupo de valores, e proxima fita
            contador = 0;
            indice_fita++;
            if (indice_fita > max_fita)// volta no inicio das fitas validas
                indice_fita = 1;
        }
    }

    // Se restarem valores na mem�ria
    if (contador > 0) {// se ainda restar valor no vetor repete o processo com os valores restantes
        sort(memoria, memoria + contador);
        
   		stringstream ss;// pq o to_string n�o funciona no dev 
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

    cout << "Distribui��o conclu�da nos arquivos fita1.txt at� fita " << max_fita << ".txt" << endl;

}

int distribui_polifasico(int n_caminhos, int tam_memoria) {
    // Criar os arquivos fita1.txt at� fita{n_caminhos}.txt
    for (int i = 1; i <= n_caminhos; i++) {
        stringstream ss;
        ss << i;
        string nome = "fita" + ss.str() + ".txt";
        ofstream fita(nome.c_str());
        if (!fita) {
            cerr << "Erro ao criar " << nome << endl;
            return -1;
        }
        fita.close();
    }

    // Abrir o arquivo de entrada
    ifstream entrada("entrada.txt");
    if (!entrada) {
        cerr << "Erro ao abrir o arquivo entrada.txt" << endl;
        return -1;
    }

    struct valor* memoria = new valor[tam_memoria];
    int contador = 0, pos;
    int valor, menor_valor, menor_segmento;
    bool aux_menor=true;
    int indice_fita = 0, seg_atual=0;
    int max_fita = n_caminhos / 2;
    
    ofstream entradas[max_fita];   // Arquivos de entrada (fita1 at� fita_n/2)
    // Abrir fitas de entrada para escrita
    for (int i = 0; i < max_fita; i++) {
        stringstream ss;
        ss << "fita" << (i+1) << ".txt";
        entradas[i].open(ss.str().c_str());
    }
    
     while (entrada >> valor) {// pega cada valor do arquivo de entrada
        memoria[contador].valor = valor; // coloca no vet
        memoria[contador].segmento=seg_atual;
        //cout<<memoria[contador].valor<<"-"<<memoria[contador].segmento<<endl;
        contador++;
        if(contador == tam_memoria) break;
	}
	do{
            // menor segmento
            aux_menor=true;
            int menor_s;
            for(int i=0; i<contador; i++){
            	if( aux_menor || memoria[i].segmento< menor_s){
            		menor_s=memoria[i].segmento;
            		aux_menor=false;
				}
            }
            //menor valor do menor segmento
            aux_menor=true;
			for(int i=0; i<contador; i++){
				if((aux_menor && memoria[i].segmento==menor_s) ||(memoria[i].segmento==menor_s && memoria[i].valor < menor_valor)){
		    		menor_valor=memoria[i].valor;
		    		pos=i;
		    		aux_menor=false;
				}
			}
			
			swap(memoria[0], memoria[pos]);// coloca menor na primeira posi�ao
            //cout<<"\n menor:"<<memoria[0].valor;
			//salvar na fita adequada
            if(seg_atual!=memoria[0].segmento){
            	indice_fita= (indice_fita + 1) % max_fita;
            	seg_atual++;
			}
            entradas[indice_fita] << memoria[0].valor << "\n";
            
			if(entrada >> valor){
				if(valor < memoria[0].valor){
					memoria[0].valor = valor; // coloca no vet
	        		memoria[0].segmento=seg_atual+1;
        		}else{
        			memoria[0].valor = valor; // coloca no vet
	        		memoria[0].segmento=seg_atual;
				}
				//cout<<memoria[0].valor<<"-"<<memoria[0].segmento<<endl;
			}else{// valores restantes no vetor
				swap(memoria[0], memoria[contador-1]);
				contador--;	
			}           
			
    }while(contador>0);
  
    for (int i = 0; i < max_fita; i++) entradas[i].close();

    delete[] memoria;
    entrada.close();

    cout << "Distribui��o conclu�da nos arquivos fita1.txt at� fita" << max_fita << ".txt" << endl;

   
	
	

    
}

void intercala_fixo(int n_caminhos, int tam_memoria) {
    int n_entrada = n_caminhos / 2; // metade das fitas
    int n_saida = n_caminhos / 2;//n_caminhos - n_entrada;
	int rodada = 0; // vai controlar qual metade das fitas fica como entrada
	int bloco = tam_memoria;  // muda de acordo com a passada
	int inicio_entrada, inicio_saida;
	// cada rodada
	while (bloco < MAX) {// quando o tamanho de bloco for igual ou maior que max, � pq todos os valores est�o na mesma fita, ordenados
	//intercala entre arquivos
	inicio_entrada = (rodada % 2 == 0) ? 1 : n_entrada + 1; //se rodada for par entrada come�a em 1 , e saida come�a na metade p/ frente
	inicio_saida   = (rodada % 2 == 0) ? n_entrada + 1 : 1;
	
    ifstream entradas[n_entrada];   // Arquivos de entrada 
    ofstream saidas[n_saida];       // Arquivos de sa�da 

    // Abrir fitas de entrada para leitura
    for (int i = 0; i < n_entrada; ++i) {
        stringstream ss;
        ss << "fita" << (inicio_entrada+i) << ".txt";
        entradas[i].open(ss.str().c_str());
    }

    // Abrir fitas de sa�da para escrita
    for (int i = 0; i < n_saida; i++) {
        stringstream ss;
        ss << "fita" << (inicio_saida+i) << ".txt";
        saidas[i].open(ss.str().c_str());
    }

    int* valores = new int[n_entrada];  // Armazena o valor atual de cada fita
    bool* ativos = new bool[n_entrada]; // Indica se a fita ainda tem valor para ser analisado nessa rodada
    int* usados = new int[n_entrada];    // Contador de quantos valores j� usamos nessa rodada
    int fita_saida = 0;  // �ndice  da fita de sa�da atual no vetor de saida
		
    // Inicializa os valores e os status das fitas de entrada
    for (int i = 0; i < n_entrada; i++) {
        if (entradas[i] >> valores[i]) {//pega um valor da entrada e salva no valores  de indice correspondente
            ativos[i] = true;// ativa a fita
            usados[i] = 0; // zera o contador de usados
        } else { // se n�o conseguir mais ler valores na fita de entrada
            ativos[i] = false;// bloqueia a fita
        }
    }

    while (true) { // executa para cada grupo do tamanho do bloco
	//ser� quebrado quando todos os arquivos tiverem terminado
        // Encontra o menor valor entre os dispon�veis no vetor de valores
		int menor;
        bool primeiro = true;
        for (int i = 0; i < n_entrada; i++) {
            if (ativos[i]) {// considerando apenas as fitas ativas
                if (primeiro || valores[i] < valores[menor]) {
                    menor = i;// guarda posi��o de onde est� o menor
                    primeiro=false;
                }
            }
        }

        if (primeiro) break; // Todos os arquivos estao inativos/terminaram a passada

        // Escreve o menor valor na fita de sa�da atual
        saidas[fita_saida] << valores[menor] << "\n";
        usados[menor]++; // conta um valor usado

        // se ainda puder ler valores na fita, l� pr�ximo valor da fita de onde tiramos o menor
        if (usados[menor] < bloco && entradas[menor] >> valores[menor]) {
            ativos[menor] = true;// mantem o bloco ativo
        } else {// n�o h� valores para ler, ou ja leu o tamanho do bloco
            ativos[menor] = false;
        }

        // Se j� usamos 'tam_memoria' valores, passamos para a pr�xima fita de sa�da
        bool finalizado=true;
        for (int i=0; i< n_entrada; i++)
        	if(ativos[i])
        		finalizado=false;
        	
		if (finalizado) {// prox rodada ate terminar valores do grupo.
            fita_saida = (fita_saida + 1) % n_saida; // Rotaciona entre as fitas de sa�da
       		for (int i=0; i< n_entrada; i++)
			   if (entradas[i] >> valores[i]) {
	            ativos[i] = true;
	            usados[i] = 0;
		    	} else {
		            ativos[i] = false;
		        }
		        
	   }
	   // se nao mudar para ativo � pq acabou valores de entrada quando terminar passada
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
    
    cout << "Rodada " << rodada + 1 << " conclu�da (bloco = " << bloco << ").\n"; 
        bloco *= n_entrada;// atualiza o tamanho do bloco                        
        rodada++; // atualiza a rodada, que define quais arquivos ser�o usados como leitura e escrita
}
cout << " valores ordenados na fita "<<inicio_saida ;

}

void intercala_variavel (int n_caminhos, int tam_memoria){
	int n_entrada = n_caminhos / 2;
    int n_saida = n_caminhos / 2;//n_caminhos - n_entrada;
	int rodada = 0;
	//int bloco = tam_memoria; 
	int inicio_entrada, inicio_saida, n_lidos=0;
	
	int* pendente = new int[n_entrada];//guarda valores de novos segmentos
	for(int i=0; i<n_entrada; i++) pendente[i]=-1;
	
	// cada passada
	while (n_lidos<MAX) {
	n_lidos=0;
	//intercala entre arquivos
	inicio_entrada = (rodada % 2 == 0) ? 1 : n_entrada + 1; 
	inicio_saida   = (rodada % 2 == 0) ? n_entrada + 1 : 1;
	
    ifstream entradas[n_entrada];   // Arquivos de entrada (fita1 at� fita_n/2)
    ofstream saidas[n_saida];       // Arquivos de sa�da (fita_n/2+1 at� fita_n)

    // Abrir fitas de entrada para leitura
    for (int i = 0; i < n_entrada; ++i) {
        stringstream ss;
        ss << "fita" << (inicio_entrada+i) << ".txt";
        entradas[i].open(ss.str().c_str());
    }

    // Abrir fitas de sa�da para escrita
    for (int i = 0; i < n_saida; ++i) {
        stringstream ss;
        ss << "fita" << (inicio_saida+i) << ".txt";
        saidas[i].open(ss.str().c_str());
    }

    int* valores = new int[n_entrada];      // Armazena o valor atual de cada fita
    bool* ativos = new bool[n_entrada];     // Indica se a fita ainda tem valor

    int fita_saida = 0;  // �ndice da fita de sa�da atual
	
	
    // Inicializa os valores e os status das fitas de entrada
	for (int i = 0; i < n_entrada; i++) {
        if(pendente[i]>=0){
       		valores[i]=pendente[i];
       		pendente[i]=-1;
       		ativos[i] = true;
		}else if (entradas[i] >> valores[i]) {
	        ativos[i] = true;
		} else {
		    ativos[i] = false;
		}
    }

    while (true) {// uma passada para um agrupamento
        int menor;
        bool primeiro = true;

        // Encontra o menor valor entre os dispon�veis
        for (int i = 0; i < n_entrada; i++) {
            if (ativos[i]) {
                if (primeiro || valores[i] < valores[menor]) {
                    menor = i;
                    primeiro=false;
                }
            }
        }

        if (primeiro) break; // Todos os arquivos estao inativos/terminaram a passada

        // Escreve o menor valor na fita de sa�da atual
        saidas[fita_saida] << valores[menor] << "\n";
        if(fita_saida==0)n_lidos++;// acabou?
        // L� pr�ximo valor da fita de onde tiramos o menor
        int novo_valor;
        if (entradas[menor] >> novo_valor) {
        	if (novo_valor >= valores[menor]) {
		        valores[menor] = novo_valor;  // Continua no mesmo bloco
		        ativos[menor] = true;
		        pendente[menor]=-1;
	   	 	}else {
            	ativos[menor] = false;
            	pendente[menor]=novo_valor;
	        }
	    }else{
	    	ativos[menor] = false;
	    	pendente[menor]=-1;
		}
		
		//se todos inativos entao terminou a rodada
        bool finalizado=true;
        for (int i=0; i< n_entrada; i++)
        	if(ativos[i])
        		finalizado=false;
        	
		if (finalizado) {// prox rodada ate terminar valores do grupo.
            fita_saida = (fita_saida + 1) % n_saida; // Rotaciona entre as fitas de sa�da
       		for (int i=0; i< n_entrada; i++)
       			if(pendente[i]>=0){
       				valores[i]=pendente[i];
       				ativos[i] = true;
				}else if (entradas[i] >> valores[i]) {
	            	ativos[i] = true;
		    	} else {
		            ativos[i] = false;
		        }
		        
	   }
	   // se nao mudar para ativo � pq acabou valores de entrada
	   finalizado=true;
        for (int i=0; i< n_entrada; i++)
        	if(ativos[i])
        		finalizado=false;
    	if(finalizado){
    		break;
		} 
	   
    }
	
    // Fecha todos os arquivos
    for (int i = 0; i < n_entrada; i++) entradas[i].close();
    for (int i = 0; i < n_saida; i++) saidas[i].close();

    delete[] valores;
    delete[] ativos;
    delete[] pendente;
    
    cout << "Rodada " << rodada + 1 << " conclu�da.\n"; 
    rodada++; 
	}
	cout << " valores ordenados na fita "<<inicio_saida ;
}

int main(int argc, char** argv) {
	setlocale(LC_ALL, "Portuguese");
	gerar_valores();
	int n_caminhos, tam_memoria, op;
    cout << "Digite o n�mero de caminhos (arquivos): ";
    cin >> n_caminhos;
    cout << "Digite o tamanho da mem�ria (n�mero de inteiros por vez): ";
    cin >> tam_memoria;
    cout<<"\n1 para ordena��o balanceada de n caminhos e bloco fixo, \n2 para ordena��o balanceada de n caminhos e bloco vari�vel e \n3 para ordena��o polif�sica";
	cin>>op;
	if(op==1){
		distribui_simples(n_caminhos, tam_memoria);
		intercala_fixo(n_caminhos, tam_memoria);
	}
	if(op==2){
		distribui_simples(n_caminhos, tam_memoria);
		intercala_variavel (n_caminhos,tam_memoria);
	}
	if(op==3){
		distribui_polifasico(n_caminhos,tam_memoria);
		intercala_variavel(n_caminhos,tam_memoria);
	}
	
	return 0;
}
