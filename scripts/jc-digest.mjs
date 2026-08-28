#!/usr/bin/env node
// Monta o corpo do e-mail semanal do Journal Club de Engenharia de Computação
// e imprime no stdout. Sem dependências: lê os próprios arquivos do repositório
// e faz um parse mínimo do frontmatter (só os campos que interessam).
//
// Uso local:  node scripts/jc-digest.mjs
// No CI:      .github/workflows/jc-digest.yaml captura a saída e envia.

import fs from "node:fs"
import path from "node:path"

const BASE_URL = "https://www.phrandrade.com"
const PASTA = "content/pt-br/research/journal-clubs/engcomp"
const GRUPO = "engcompbji@googlegroups.com"
const JANELA_DIAS = 14

const TOPICOS = [
  ["Segurança", "cs.CR"],
  ["Engenharia de Software", "cs.SE"],
  ["Linguagens de Programação", "cs.PL"],
  ["Algoritmos", "cs.DS"],
  ["Inteligência Artificial", "cs.AI"],
  ["Aprendizado de Máquina", "cs.LG"],
  ["Linguagem Natural", "cs.CL"],
  ["Distribuído e Paralelo", "cs.DC"],
  ["Sistemas Operacionais", "cs.OS"],
  ["Redes", "cs.NI"],
  ["Arquitetura de Hardware", "cs.AR"],
  ["Processamento de Sinais", "eess.SP"],
]

// Parse deliberadamente burro: pega `chave: valor` de primeiro nível dentro do
// bloco de frontmatter, sem suportar aninhamento nem listas. É tudo que os
// campos usados aqui precisam, e evita puxar um parser de YAML só para isto.
function lerFrontmatter(arquivo) {
  const texto = fs.readFileSync(arquivo, "utf-8")
  const match = texto.match(/^---\r?\n([\s\S]*?)\r?\n---/)
  if (!match) return {}
  const dados = {}
  for (const linha of match[1].split(/\r?\n/)) {
    const par = linha.match(/^([A-Za-z0-9_-]+):\s*(.*)$/)
    if (!par) continue
    dados[par[1]] = par[2].trim().replace(/^["']|["']$/g, "")
  }
  return dados
}

function artigosRecentes() {
  let arquivos = []
  try {
    arquivos = fs.readdirSync(PASTA).filter((f) => f.endsWith(".md") && f !== "index.md")
  } catch {
    return []
  }

  const limite = new Date()
  limite.setDate(limite.getDate() - JANELA_DIAS)

  return (
    arquivos
      .map((f) => lerFrontmatter(path.join(PASTA, f)))
      // `arxiv` é o que distingue uma nota de artigo das páginas de apoio
      // (topicos, dashboard), que carregam as mesmas tags.
      .filter((fm) => fm.arxiv && (fm.discussed || fm.discutido))
      .map((fm) => ({ ...fm, data: new Date(fm.discussed || fm.discutido) }))
      .filter((fm) => !Number.isNaN(fm.data.getTime()) && fm.data >= limite)
      .sort((a, b) => b.data - a.data)
  )
}

function montar() {
  const linhas = []
  linhas.push("Pessoal, passando a chamada do Journal Club de Engenharia de Computação.")
  linhas.push("")

  const recentes = artigosRecentes()
  if (recentes.length > 0) {
    linhas.push(`Discutidos nas últimas ${JANELA_DIAS / 7} semanas:`)
    for (const artigo of recentes) {
      const apresentador = artigo.presenter || artigo.apresentador
      const quem = apresentador ? ` (apresentou: ${apresentador})` : ""
      linhas.push(`- ${artigo.title}${quem}`)
      linhas.push(`  ${artigo.arxiv}`)
    }
    linhas.push("")
  }

  linhas.push("Onde procurar o artigo da próxima semana — listas de recentes do arXiv:")
  for (const [nome, categoria] of TOPICOS) {
    linhas.push(`- ${nome} (${categoria}): https://arxiv.org/list/${categoria}/recent`)
  }
  linhas.push("")
  linhas.push(`Para sugerir uma leitura, é só responder este e-mail ou mandar para ${GRUPO}.`)
  linhas.push("")
  linhas.push("Tópicos e critérios de escolha:")
  linhas.push(`${BASE_URL}/pt-br/research/journal-clubs/engcomp/topicos`)
  linhas.push("")
  linhas.push("Histórico do que já discutimos:")
  linhas.push(`${BASE_URL}/pt-br/research/journal-clubs/engcomp`)
  linhas.push("")
  linhas.push("Como o clube vem andando:")
  linhas.push(`${BASE_URL}/pt-br/research/journal-clubs/engcomp/dashboard`)

  return linhas.join("\n")
}

process.stdout.write(montar() + "\n")
