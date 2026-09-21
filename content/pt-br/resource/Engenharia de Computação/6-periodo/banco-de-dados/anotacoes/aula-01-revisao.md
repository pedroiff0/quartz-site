---
publish: false
title: Aula 01 - Revisão
created: 2026-09-15 13:47
modified: 2026-09-19 13:18
encrypted: true
tags:
- aula
- engenharia-de-computacao
icon: lucide-book-open
cssclasses:
  - page-layout
---

<div class="progress-bar-container" style="background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 8px; padding: 12px 16px; margin: 1.5rem 0;">
  <div style="font-weight: 600; font-size: 0.85rem; color: var(--dark, #334155); margin-bottom: 6px;">Progresso das Aulas da Disciplina</div>
  <div style="background: var(--lightgray, #e2e8f0); border-radius: 4px; overflow: hidden; height: 8px;">
    <div style="background: var(--secondary, #6d28d9); width: 10%; height: 100%;"></div>
  </div>
</div>

# Aula 01 - Revisão

> [!info]- Informações & Checklist da Aula
> - **Data da Aula:** 15/09/2026
> - **Status de Revisão:**
>   - [ ] Anotações em sala de aula
>   - [ ] Revisão e fixação de conceitos
>   - [ ] Resolução de exercícios recomendados
>   - [ ] Destilação para [[07-permanente/notas-permanentes|Notas Permanentes]]

---

## Anotações do Quadro & Conteúdo

### Tópico :
- Trabalho 30% Indiv. + 20% Banco e Consultas + 20%  de Apresentação (Organização);

1. Criar Banco
2. Inserir Dados
3. Ler Dados
4. Editar Dados
5. Apagar Dados
6. Otimizar Armazenamento
7. Otimizar Leitura
8. Segurança (RBAC)

Contábil Brasil - CHB, Pedro, Bernardo P. 

Modelagem:
* Diagrama Entidade Relacionamento (DER)
* Descrever os casos de Uso.
* Permissões por autor (Segurança)
* Regras de Negócio
* Cada membro apresentar
	* o seu caso de uso, a criação da tabelas necessárias e “CRUD” a manipulação
* 

* Avaliação 30% Av. Individual
### Revisão de Modelagem
- Cliente(cpf,nome,telefone,email,data_nasc) (1,1) 
- Pedido(data,itens,cliente.cpf(FK),) (0,n)

Chaves Candidatas (CK) -> DDL:
* cpf
* email

Chaves Primárias (PK):
* cpf

Chave Estrangeira (FK):
* cpf


### Generalização e Especialização

* cliente(cpf,nome,codigo_desc);
* fornecedor(cpf,nome,cnpj);
* Generalização PESSOA(cpf,nome);

* ItemDePedido(quantidade,preco,pedido:id(FK),produto:id(FK));




---

## Resumo Conceitual
- **Conceito Central:** 
- **Fórmulas / Algoritmos Relevantes:**
- **Pegadinhas / Atenção em Provas:**

---

## Esquemas & Anotações Visuais (excalidraw)
<!-- No iPad: insira desenhos com 'excalidraw: Create and embed new drawing' para desenhar com Apple Pencil -->

---

## Flashcards de Fixação (Spaced Repetition)
# flashcard
<!-- Sintaxe: Pergunta::Resposta ou Pergunta:::Resposta invertida -->
- 

---

## Dúvidas & Exercícios Recomendados
- [ ] 
