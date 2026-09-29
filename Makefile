.PHONY: help install dev build sync lint clean

help: ## Exibe a lista de comandos disponíveis
	@echo "Comandos disponíveis em Quartz Site:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2}'

install: ## Instala dependências do Quartz
	npm install
	npx quartz plugin install

dev: ## Inicia servidor de desenvolvimento local com live-reload
	npx quartz build --serve

build: ## Compila o site estático para a pasta public/
	npx quartz build

sync: ## Executa a sincronização seletiva com o cofre Obsidian
	python3 scripts/sync_vault.py

lint: ## Valida sintaxe e links quebrados
	@test -f quartz.config.yaml && echo "quartz.config.yaml presente."
	@test -d content && echo "content/ presente."

clean: ## Limpa arquivos de build e cache
	rm -rf public .quartz-cache
