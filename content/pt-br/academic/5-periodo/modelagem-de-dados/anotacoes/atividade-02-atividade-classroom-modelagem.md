---
publish: false
title: Atividade 02 - Atividade Classroom - Modelagem
created: 2026-04-23 14:49
modified: 2026-09-22 22:41
encrypted: true
tags:
- atividade
- trabalho
- engenharia-de-computacao
cssclasses:
- page-layout
icon: lucide-book-open
---
# Atividade 02 - Atividade Classroom - Modelagem

## Resumo Executivo

Atividade proposta no Classroom contendo 5 questões de modelagem conceitual de dados para diferentes domínios: plataforma de cursos corporativos, sistema de manutenção hospitalar, gestão de eventos acadêmicos, locadora de veículos industriais e biblioteca de laboratório.

## Informações & Checklist de Entrega

Questões propostas:
1. Plataforma de cursos corporativos
2. Sistema de manutenção de equipamentos hospitalares
3. Sistema de gestão de eventos acadêmicos
4. Locadora de veículos para uso industrial
5. Sistema de biblioteca de laboratório universitário

## Objetivos do Trabalho

Desenvolver modelos conceituais para 5 sistemas diferentes, identificando entidades, atributos, relacionamentos e cardinalidades.

## Metodologia & Desenvolvimento Prático

### Questão 1: Plataforma de Cursos Corporativos

#### ENTIDADES E ATRIBUTOS
- EMPRESA_CLIENTE: cnpj, razao_social, nome_fantasia, email_contato, telefone_principal
- CURSO: codigo_curso, titulo, carga_horaria, modalidade, nivel
- TURMA: codigo_turma, data_inicio_prevista, data_termino_prevista, formato_oferta, status
- INSTRUTOR: matricula, nome, email_corporativo, especialidade_principal, tipo_vinculo
- PARTICIPANTE: cpf, nome, email, cargo, setor
- AVALIACAO: codigo_avaliacao, tipo, data_aplicacao, peso
- NOTA: valor_obtido, data_lancamento, situacao
- PARCELA: numero_parcela, data_vencimento, valor_previsto, data_pagamento, situacao_pagamento

#### RELACIONAMENTOS
- EMPRESA_CLIENTE contrata CURSO (N:N)
- EMPRESA_CLIENTE possui TURMA (1:N)
- CURSO origina TURMA (1:N)
- INSTRUTOR responsavel_por TURMA (1:N)
- EMPRESA_CLIENTE possui PARTICIPANTE (1:N)
- PARTICIPANTE inscreve_se_em TURMA (N:N)
- TURMA possui AVALIACAO (1:N)
- PARTICIPANTE recebe NOTA (1:N)
- TURMA possui PARCELA (1:N)

### Questão 2: Sistema de Manutenção de Equipamentos Hospitalares

#### ENTIDADES E ATRIBUTOS
- EQUIPAMENTO: num_patrimonio, descricao, fabricante, modelo, data_aquisicao, status_operacional
- SETOR_HOSPITALAR: codigo_setor, nome, ramal_principal
- MANUTENCAO: codigo_manutencao, tipo, data_abertura, data_conclusao, descricao_problema, situacao
- TECNICO: matricula, nome, especialidade, telefone, tipo_vinculo
- PECA_REPOSICAO: codigo_peca, descricao, fabricante, valor_unitario
- CATEGORIA_EQUIPAMENTO: codigo_categoria, nome, intervalo_preventiva_padrao
- LAUDO: numero_laudo, data_emissao, tipo_laudo, parecer_tecnico

#### RELACIONAMENTOS
- SETOR_HOSPITALAR possui EQUIPAMENTO (1:N)
- CATEGORIA_EQUIPAMENTO classifica EQUIPAMENTO (1:N)
- EQUIPAMENTO passa_por MANUTENCAO (1:N)
- TECNICO atua_em MANUTENCAO (N:N) -> Atributos: horas_trabalhadas, funcao
- MANUTENCAO utiliza PECA_REPOSICAO (N:N) -> Atributo: quantidade_utilizada
- MANUTENCAO gera LAUDO (1:N)

### Questão 3: Sistema de Gestão de Eventos Acadêmicos

#### ENTIDADES E ATRIBUTOS
- EVENTO: codigo_evento, nome, tema_central, data_inicio, data_termino, cidade_sede
- DEPARTAMENTO: codigo_depto, nome, sigla
- SESSAO: codigo_sessao, titulo, tipo, data, horario_inicio, horario_termino, capacidade_max
- PALESTRANTE: cpf, nome, instituicao_origem, email, mini_curriculo
- INSCRITO: cpf, nome, email, categoria_inscricao, instituicao
- ARTIGO: codigo_artigo, titulo, resumo, area_tematica, status_avaliacao
- AVALIADOR: matricula, nome, email, area_especialidade
- AVALIACAO_ARTIGO: nota, parecer, data_avaliacao
- CERTIFICADO: numero_certificado, tipo, data_emissao, carga_horaria

#### RELACIONAMENTOS
- DEPARTAMENTO organiza EVENTO (N:N)
- EVENTO possui SESSAO (1:N)
- PALESTRANTE participa_de SESSAO (N:N)
- INSCRITO inscreve_se_em EVENTO (N:N)
- INSCRITO autor_principal ARTIGO (1:N)
- EVENTO recebe ARTIGO (1:N)
- AVALIADOR realiza AVALIACAO_ARTIGO (1:N)
- ARTIGO recebe AVALIACAO_ARTIGO (1:N) -> Requisito: min 2 avaliações
- EVENTO emite CERTIFICADO (1:N)
- INSCRITO recebe CERTIFICADO (1:N)

### Questão 4: Locadora de Veículos para Uso Industrial

#### ENTIDADES E ATRIBUTOS
- CLIENTE_CORPORATIVO: cnpj, razao_social, nome_fantasia, email_comercial, telefone
- VEICULO: placa, renavam, modelo, ano_fabricacao, tipo_veiculo, status
- BASE_OPERACIONAL: codigo_base, nome, cidade, estado
- CONTRATO_LOCACAO: numero_contrato, data_assinatura, inicio_vigencia, termino_vigencia, valor_mensal
- GESTOR_COMERCIAL: matricula, nome, email_corporativo, regional_atuacao
- ORDEM_SERVICO: codigo_os, tipo, data_abertura, data_execucao_prevista, status
- TECNICO_CAMPO: matricula, nome, telefone, especialidade
- ITEM_VERIFICACAO: numero_item, descricao, resultado, observacao

#### RELACIONAMENTOS
- CLIENTE_CORPORATIVO firma CONTRATO_LOCACAO (1:N)
- BASE_OPERACIONAL abriga VEICULO (1:N)
- CONTRATO_LOCACAO inclui VEICULO (N:N)
- GESTOR_COMERCIAL responsavel_por CONTRATO_LOCACAO (1:N)
- CONTRATO_LOCACAO gera ORDEM_SERVICO (1:N)
- TECNICO_CAMPO executa ORDEM_SERVICO (1:N)
- ORDEM_SERVICO possui ITEM_VERIFICACAO (1:N)

### Questão 5: Sistema de Biblioteca de Laboratório Universitário

#### ENTIDADES E ATRIBUTOS
- ITEM_ACERVO: tombo_patrimonial, nome_item, descricao, fabricante, estado_conservacao, tipo_item
- CATEGORIA_ACERVO: codigo_categoria, nome, prazo_emprestimo_dias
- USUARIO: matricula, nome, email_institucional, tipo_usuario, curso_setor
- EMPRESTIMO: codigo_emprestimo, data_retirada, data_prevista_devolucao, data_efetiva_devolucao, situacao
- ATENDENTE: matricula_funcional, nome, email_institucional
- TERMO_RESPONSABILIDADE: numero_termo, data_assinatura, finalidade_declarada, status
- RESERVA: codigo_reserva, data_solicitacao, data_limite_atendimento, situacao

#### RELACIONAMENTOS
- CATEGORIA_ACERVO classifica ITEM_ACERVO (1:N)
- USUARIO realiza EMPRESTIMO (1:N)
- ATENDENTE registra EMPRESTIMO (1:N)
- EMPRESTIMO inclui ITEM_ACERVO (N:N) -> Atributos: condicao_saida, condicao_retorno
- EMPRESTIMO possui TERMO_RESPONSABILIDADE (1:1)
- USUARIO faz RESERVA (1:N)
- ITEM_ACERVO objeto_de RESERVA (1:N)

## Resultados Obtidos & Conclusão

Cinco modelos conceituais completos mapeando domínios diversos, cada um com múltiplas entidades, atributos e relacionamentos. Todos os modelos seguem convenção ER padrão e explicitam cardinalidades.

## Referências & Links

Atividade Classroom - Modelagem Conceitual
