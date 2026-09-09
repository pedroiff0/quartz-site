---
publish: true
title: Aula 02 - Capítulo 3.3
subtitle: ""
created: 2026-09-08 15:33
modified: 2026-09-08 16:16
discipline: ""
period: ""
professor: ""
encrypted: true
password: "eng232"

# 🔗 Materiais e Arquivos da Aula (Disponíveis em _materiais da Disciplina)
slides_aula: ""
roteiro_aula: ""
anexos: ""

tags:
  - aula
  - engenharia-de-computacao
  - anotacoes
cssclasses:
  - page-layout
---

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="../index">Hub da Disciplina</a></b></div>
  <div>🏠 <b><a href="../index">Visão Geral</a></b></div>
  <div>➡️ <b><a href="../index">Aulas</a></b></div>
</div>

# 📝 Aula 02 - Capítulo 3.3

> [!info] 📌 Informações da Aula
> - **Docente:** 
> - **Data da Aula:** 08/09/2026
> - **Tópico Central:** 
> - **Status das Anotações:** 
>   - [x] 🟡 Planejando 
>   - [ ] 🟠 Em Andamento 
>   - [ ] 🟢 Concluído

## 📂 Materiais & Recursos Didáticos da Aula

> [!tip] 🔗 Arquivos e Materiais da Disciplina
> - 📄 **Slides do Docente:** *Consulte os anexos vinculados*
> - 📑 **Roteiro / Texto de Apoio:** *Consulte os materiais de aula*
> - 📦 **Exercícios / Anexos:** *Disponíveis no repositório*

## 📋 Sumário Interativo
- [📍 Anotações](#-anotações)
- [🧠 Resumo](#-resumo)
- [📝 Dúvida](#-dúvida)

---

## 📍 Anotações

### 08/09

#### Capítulo 3.3


> [!PDF|255, 208, 0] [[pt-br/resource/Engenharia de Computação/_materiais/6-periodo/comunicacao-de-dados/Forouzan_Comunicacao_de_dados_e_redes_de.pdf#page=71&annotation=6482R|Forouzan_Comunicacao_de_dados_e_redes_de, p.38]]
> > A maioria dos sinais digitais é não periódica e, conseqüentemente, freqüência e período não são características adequadas. Outro termo  taxa de transferência (em vez de freqüência) é usado para descrever sinais digitais. A taxa de transferência é o número de bits enviados em 1s, expresso em bits por segundo (bps).
 
> [!PDF|8, 109, 221] [[pt-br/resource/Engenharia de Computação/_materiais/6-periodo/comunicacao-de-dados/Forouzan_Comunicacao_de_dados_e_redes_de.pdf#page=71&annotation=6485R|Forouzan_Comunicacao_de_dados_e_redes_de, p.38]]
> > O comprimento de bits é a distância que um bit ocupa no meio de transmissão

![[pt-br/resource/Engenharia de Computação/_materiais/6-periodo/comunicacao-de-dados/Forouzan_Comunicacao_de_dados_e_redes_de.pdf#page=72&rect=125,223,547,482&color=note|Forouzan_Comunicacao_de_dados_e_redes_de, p.39]]

> [!PDF|234, 82, 82] [[pt-br/resource/Engenharia de Computação/_materiais/6-periodo/comunicacao-de-dados/Forouzan_Comunicacao_de_dados_e_redes_de.pdf#page=73&annotation=6488R|Forouzan_Comunicacao_de_dados_e_redes_de, p.40]]
> > A transmissão banda-base requer que tenhamos um canal passa-baixa, um canal com largura de banda que começa em zero. Este é o caso se tivermos um meio de transmissão dedicado com toda largura de banda alocada em apenas um canal. 
> 
> 

> [!PDF|187, 97, 229] [[pt-br/resource/Engenharia de Computação/_materiais/6-periodo/comunicacao-de-dados/Forouzan_Comunicacao_de_dados_e_redes_de.pdf#page=74&annotation=6476R|Forouzan_Comunicacao_de_dados_e_redes_de, p.41]]
> > precisamos enviar todo o espectro, o intervalo contínuo de freqüências entre zero e infinito. Isso é possível se tivermos um meio dedicado com uma largura de banda infinita entre o emissor e o receptor que preserva a amplitude exata de cada componente do sinal composto
> 

> [!PDF|234, 82, 82] [[pt-br/resource/Engenharia de Computação/_materiais/6-periodo/comunicacao-de-dados/Forouzan_Comunicacao_de_dados_e_redes_de.pdf#page=74&annotation=6479R|Forouzan_Comunicacao_de_dados_e_redes_de, p.41]]
> > A transmissão banda-base de um sinal digital que preserve a forma do sinal digital é possível apenas se tivermos um canal passa-baixa com largura de banda infinita ou muito ampla.

> [!PDF|187, 97, 229] [[pt-br/resource/Engenharia de Computação/_materiais/6-periodo/comunicacao-de-dados/Forouzan_Comunicacao_de_dados_e_redes_de.pdf#page=75&annotation=6473R|Forouzan_Comunicacao_de_dados_e_redes_de, p.42]]
> > Para simular esses dois casos, precisamos de um sinal analógico de freqüência  f  =  N/2. Suponhamos que 1 seja o valor máximo positivo e 0, o valor máximo negativo. Enviamos 2 bits em cada ciclo; a freqüência do sinal ana- lógico é a metade da taxa de transferência, ou seja,  N/2. Entretanto, essa única freqüência não é capaz de reproduzir todos os padrões; precisamos de mais componentes. A freqüência máxima é  N/2.

> [!PDF|234, 82, 82] [[pt-br/resource/Engenharia de Computação/_materiais/6-periodo/comunicacao-de-dados/Forouzan_Comunicacao_de_dados_e_redes_de.pdf#page=75&annotation=6491R|Forouzan_Comunicacao_de_dados_e_redes_de, p.42]]
> > Melhor Aproximação Para fazer que a forma do sinal analógico se pareça mais com a de um sinal digital, precisamos acrescentar mais harmônicas das freqüências. Precisamos aumentar a largura de banda. Podemos aumentar a largura de banda para 3N/2, 5N/2, 7N/2 e assim por diante. A Figura 3.22 ilustra o efeito desse aumento para um dos piores casos, o padrão 010

![[pt-br/resource/Engenharia de Computação/_materiais/6-periodo/comunicacao-de-dados/Forouzan_Comunicacao_de_dados_e_redes_de.pdf#page=76&rect=124,414,553,712&color=red|Forouzan_Comunicacao_de_dados_e_redes_de, p.43]]
![[pt-br/resource/Engenharia de Computação/_materiais/6-periodo/comunicacao-de-dados/Forouzan_Comunicacao_de_dados_e_redes_de.pdf#page=76&rect=190,100,482,216&color=important|Forouzan_Comunicacao_de_dados_e_redes_de, p.43]]
> [!PDF|8, 109, 221] [[pt-br/resource/Engenharia de Computação/_materiais/6-periodo/comunicacao-de-dados/Forouzan_Comunicacao_de_dados_e_redes_de.pdf#page=77&annotation=6494R|Forouzan_Comunicacao_de_dados_e_redes_de, p.44]]
> > A transmissão banda larga, ou modulação, significa transformar o sinal digital em sinal analógico para transmissão. A modulação nos permite usar um canal passa-faixa um canal com largura de banda que não se inicie em zero.
![[pt-br/resource/Engenharia de Computação/_materiais/6-periodo/comunicacao-de-dados/Forouzan_Comunicacao_de_dados_e_redes_de.pdf#page=78&rect=126,465,536,714&color=note|Forouzan_Comunicacao_de_dados_e_redes_de, p.45]]

> [!PDF|187, 97, 229] [[pt-br/resource/Engenharia de Computação/_materiais/6-periodo/comunicacao-de-dados/Forouzan_Comunicacao_de_dados_e_redes_de.pdf#page=78&annotation=6497R|Forouzan_Comunicacao_de_dados_e_redes_de, p.45]]
> >  solução é considerar o canal um canal passa-faixa, converter o sinal digital em analógico e transmitir o sinal analógico. Podemos instalar dois conversores para transformar o sinal digital em analógico e vice-versa no lado receptor. O conversor, nesse caso, é chamado modem (modulador/demodulador)

> [!PDF|234, 82, 82] [[pt-br/resource/Engenharia de Computação/_materiais/6-periodo/comunicacao-de-dados/Forouzan_Comunicacao_de_dados_e_redes_de.pdf#page=78&annotation=6500R|Forouzan_Comunicacao_de_dados_e_redes_de, p.45]]
> > Precisamos converter a voz digitalizada em sinal analógico composto antes de transmiti-lo. Os celulares digitais convertem o sinal de áudio analógico em digital e depois o convertem novamente em analógico para transmissão através de um canal passa-faixa


---

## 🧠 Resumo

| Tópico | Princípio Central | Atenção Especial / Pegadinha |
| :----- | :---------------- | :--------------------------- |
|        |                   |                              |

> [!tip] 💡 Dica de Prova do Professor
> Destaques e orientações mencionadas pelo docente durante a aula.

---

## 📝 Dúvida
- [ ] 
