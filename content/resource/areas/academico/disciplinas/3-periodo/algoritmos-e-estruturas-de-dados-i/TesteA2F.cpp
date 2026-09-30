#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <sstream>

using namespace std;

struct Pessoa {
string nome;
int idade;
};


int main () {
int opcao;

do {
cout <<"\n1. Cadastrar pessoa";
cout <<"\n2. Exibir Cadastros";
cout <<"\n3. Editar Cadastros";
cout <<"\n4. Ordenar cadastros";
cout <<"\n5. Sair" << endl;
cin >> opcao;

switch (opcao) {
case 1:
{
cout << "Iniciando Cadastro de Pessoa!" << endl;
ofstream arquivo("cads.txt", ios::app);

if(!arquivo.is_open()) {
cerr << "\nErro ao abrir o arquivo para escrita." << endl;
return 1;
}

string nome;
int idade;


cout << "\nDigite as informações pedidas para finalizar o registro." << endl;
cin.ignore();
cout << "Nome: ";
getline(cin, nome);
cout << "Idade: ";
cin >> idade;
arquivo << nome << "," << idade << endl;
arquivo.close();
break;
}
case 2:
{
cout << "\nIniciando Exibição dos Cadastros!" << endl;
ifstream arquivo2("cads.txt");
if(!arquivo2.is_open()) {
cerr << "\nErro ao abrir o arquivo para escrita." << endl;
return 1;
}
string linha;
while (getline(arquivo2,linha)){
cout << linha << endl;
}
break;
}
case 3:
{
cout << "Iniciando Edição de Pessoa!";

ifstream arquivo2("cads.txt");
if(!arquivo2.is_open()) {
cerr << "\nErro ao abrir o arquivo para escrita." << endl;
return 1;
}

string linha;
int contador = 0;

while(getline(arquivo2,linha)) {
contador++;
};

//alocar dinamicamente
Pessoa* vet = new Pessoa[contador];

//voltar pro 0
arquivo2.clear();
arquivo2.seekg(0,ios::beg);

//copiar pro vetor
int i = 0;
while(getline(arquivo2,linha)) {
size_t pos = linha.find(",");
string teste = linha.substr(pos+1,pos+2);
if (pos != string::npos) {
vet[i].nome = linha.substr(0, pos);
}
vet[i].idade = stoi(teste);
i++;
}

cin.ignore();
string nome;
cout << "Informe o nome a ser alterado: ";
getline(cin,nome);
int ida = 0;


            //alterar
for(i = 0; i < contador; i++) {
   if(nome == vet[i].nome) {
       cout << "Informe a nova idade: ";
       cin >> ida;
       vet[i].idade = ida;
       break;
       }
}

arquivo2.close();
ofstream arquivo3("cads.txt", ios::trunc);

ofstream arquivo4("cads.txt", ios::app);

if(!arquivo4.is_open()) {
cerr << "\nErro ao abrir o arquivo para escrita." << endl;
return 1;
}
for (i = 0; i < contador; i++) {
    arquivo4 << vet[i].nome << "," << vet[i].idade << endl;
}
delete[] vet;
break;
}
case 4:
{
cout << "Iniciando Ordenações dos Cadastros!";

ifstream arquivo2("cads.txt");
if(!arquivo2.is_open()) {
cerr << "\nErro ao abrir o arquivo para escrita." << endl;
return 1;
}

string linha;
int contador = 0;

while(getline(arquivo2,linha)) {
contador++;
};

//alocar dinamicamente
Pessoa* vet = new Pessoa[contador];

//voltar pro 0
arquivo2.clear();
arquivo2.seekg(0,ios::beg);

   //copiar pro vetor
int i = 0;
while(getline(arquivo2,linha)) {
size_t pos = linha.find(",");
string teste = linha.substr(pos+1,pos+2);
if (pos != string::npos) {
vet[i].nome = linha.substr(0, pos);
}
vet[i].idade = stoi(teste);
i++;
}
           
            //ordenação
            int j, aux;
   
            for(i=0; i<contador; i++){
                aux = vet[i].idade;
                j = i - 1;
               
                while(vet[j].idade < aux && j >= 0){
                    vet[j+1].idade = vet[j].idade;
               
                    j--;    
                }
                vet[j+1].idade = aux;
            }
           
            cout << "\n--------------------ORDENADOS-----------------" << endl;
            for(int i = 0; i < contador; i++) {
                cout << vet[i].nome << "," << vet[i].idade << endl;
            }
            delete[] vet;
break;
}
}
} while (opcao != 5);

return 0;
}
