---
publish: true
title: Portal Acadêmico IFF (academicoWeb)
created: 2026-03-13 13:04:00-03:00
modified: 2026-09-30T13:05:50-03:00
tags:
- web-app
- iff
- scraping
- arquivado
repo: https://github.com/pedroiff0/academicoWeb
status: privado
cssclasses:
- page-layout
icon: lucide-graduationcap
sitesync: true
---

- Origem: [[pt-br/projects/site-publico-hub|Site Público]]

# Portal Acadêmico IFF 

Um sistema web moderno para acessar e gerenciar seus dados acadêmicos do Instituto Federal Fluminense (IFF) de forma rápida e intuitiva.

## Características

- **Login Integrado**: Autenticação usando as mesmas credenciais do portal acadêmico oficial
- **Dashboard Intuitivo**: Painel de controle com acesso rápido a todas as informações
- **Diário Acadêmico**: Acompanhe frequência, avisos e informações diárias
- **Material de Aula**: Acesso centralizado aos materiais disponibilizados pelos professores
- **Boletim**: Consulte suas notas e desempenho em todas as disciplinas
- **Histórico Escolar**: Visualize seu histórico acadêmico completo
- **Notificações**: Sistema de alertas para mensagens importantes
- **Design Responsivo**: Interface adaptada para desktop, tablet e celular
- **Cores Institucionais**: Design usando as cores oficiais do IFF (vermelho e verde)
- **Controle de Acesso**: Sistema robusto de autenticação com proteção de rotas

## Instalação

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Chrome/Chromium instalado (para Selenium)

### Passo 1: Clonar ou copiar o projeto

```bash
cd /Users/pedro/Documents/Repositorios/Academicos/academicoWeb
```

### Passo 2: Criar ambiente virtual

```bash
python3 -m venv .venv
source .venv/bin/activate  # No Windows: .venv\Scripts\activate
```

### Passo 3: Instalar dependências

```bash
pip install -r requirements.txt
```

### Passo 4: Configurar variáveis de ambiente

```bash
cp .env.example .env
# Editar .env com suas configurações
```

### Passo 5: Executar a aplicação

```bash
python run.py
```

A aplicação estará disponível em: **http://localhost:5000**

## Estrutura do Projeto

```
academicoWeb/
 app/
    __init__.py           # Aplicação Flask principal
    scraper.py            # Módulo de web scraping
 config/
    config.py             # Configurações da aplicação
 templates/
    base.html             # Template base com navbar e sidebar
    login.html            # Página de login
    dashboard.html        # Dashboard principal
    diary.html            # Página de diário
    materials.html        # Página de materiais
    grades.html           # Página de boletim
    history.html          # Página de histórico
    notifications.html    # Página de notificações
    404.html              # Página de erro 404
    500.html              # Página de erro 500
 static/
    css/
       style.css         # Estilos CSS (cores IFF, responsivo)
    js/
        main.js           # Scripts JavaScript
 run.py                    # Script de entrada
 requirements.txt          # Dependências do projeto
 .env.example              # Exemplo de variáveis de ambiente
 README.md                 # Este arquivo
```

## Segurança

- **Autenticação**: Login integrado com o portal acadêmico do IFF
- **Sessões**: Gerenciamento seguro de sessões com Flask-Session
- **Proteção de Rotas**: Decorador `@login_required` em todas as rotas internas
- **Variáveis de Ambiente**: Senhas e credenciais não são armazenadas em código
- **HTTPS**: Recomenda-se usar HTTPS em produção

## Fluxo de Funcionamento

1. **Login**: Usuário insere matrícula e senha
2. **Autenticação**: Sistema faz login no portal acadêmico via Selenium
3. **Scraping**: Dados são extraídos do portal acadêmico
4. **Armazenamento**: Sessão do usuário é mantida
5. **Acesso**: Usuário pode acessar as diferentes seções
6. **Logout**: Sessão é encerrada e driver Selenium é fechado

## Rotas Disponíveis

### Públicas
- `GET /` - Redireciona para dashboard (se autenticado) ou login
- `GET /login` - Página de login
- `POST /login` - Processar login

### Protegidas (requerem autenticação)
- `GET /dashboard` - Dashboard principal
- `GET /diary` - Diário acadêmico
- `GET /materials` - Material de aula
- `GET /grades` - Boletim
- `GET /history` - Histórico escolar
- `GET /notifications` - Notificações
- `GET /api/notifications` - API de notificações (JSON)
- `GET /logout` - Fazer logout

## Tecnologias Utilizadas

- **Backend**: Flask 3.0.0
- **Web Scraping**: Selenium 4.15.2, BeautifulSoup4 4.12.2
- **Gerenciamento de Sessões**: Flask-Session 0.5.0
- **Web Driver**: WebDriver Manager 4.0.1
- **Frontend**: HTML5, CSS3, JavaScript vanilla
- **Variáveis de Ambiente**: python-dotenv 1.0.0

## Customização

### Cores Institucionais do IFF

O projeto utiliza as cores oficiais do IFF:
- **Vermelho**: `#C41E3A`
- **Verde**: `#1F7F4F`

Essas cores podem ser customizadas no arquivo `static/css/style.css`:

```css
:root {
    --iff-red: #C41E3A;
    --iff-green: #1F7F4F;
    /* ... outras cores ... */
}
```

### Temas

Para criar um tema diferente, edite as cores no CSS ou modifique `config/config.py`.

## Responsividade

O design é totalmente responsivo:
- **Desktop**: Layout com sidebar fixo
- **Tablet**: Ajustes de espaçamento
- **Mobile**: Menu colapsável, layout em coluna única

## Resolução de Problemas

### Erro: "Import selenium could not be resolved"
```bash
pip install -r requirements.txt
```

### Erro: "ChromeDriver not found"
O `webdriver-manager` baixará automaticamente a versão correta do ChromeDriver.

### Erro ao fazer login
- Verifique se as credenciais estão corretas
- Verifique a conectividade com a internet
- O portal acadêmico pode estar indisponível

### Dados não aparecem nas páginas
- Aguarde alguns segundos, o scraping leva tempo
- Verifique se a estrutura HTML do site académico não mudou

## Logs

Logs são exibidos no console durante a execução. Para mais detalhes, adicione em `app/__init__.py`:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Deploy em Produção

Para deployer em produção:

1. **Mudança de Ambiente**:
   ```bash
   export FLASK_ENV=production
   ```

2. **Usar um servidor WSGI** (ex: Gunicorn):
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

3. **Habilitar HTTPS** com certificado SSL

4. **Configurar variáveis de ambiente** em produção

5. **Usar um banco de dados** para armazenar dados em cache

## Suporte

Para problemas ou dúvidas:
- Verifique a documentação do Flask: https://flask.palletsprojects.com
- Verifique a documentação do Selenium: https://selenium.dev
- Abra uma issue no repositório do projeto

## Licença

Este projeto é fornecido como exemplo educacional para fins de aprendizado.

## Checklist de Implementação

- Estrutura base do projeto
- Autenticação com Selenium
- Rotas Flask protegidas
- Layout base responsivo
- Página de login
- Dashboard
- Página de diário
- Página de material
- Página de boletim
- Página de histórico
- Página de notificações
- CSS com cores IFF
- JavaScript interativo
- Páginas de erro (404, 500)
- Módulo de scraping
- Configurações centralizadas
- Documentação completa

## Próximos Passos

Funcionalidades futuras para aprimoramento:
- [ ] Cache de dados com Redis
- [ ] Background tasks com Celery
- [ ] Banco de dados (SQLAlchemy)
- [ ] API REST completa
- [ ] Autenticação OAuth
- [ ] Temas personalizáveis
- [ ] Exportação em PDF
- [ ] Notificações via email
- [ ] App mobile nativa
- [ ] Integração com ferramentas externas

---

**Desenvolvido com  para os alunos do IFF**

---

## Autor e Contato

- **Autor:** Pedro Henrique Rocha de Andrade
- **GitHub:** [pedroiff0](https://github.com/pedroiff0)
- **LinkedIn:** [Pedro Henrique Rocha de Andrade](https://linkedin.com/in/pedro-andrade-iff)

---

## Links e Referências

- **Repositório no GitHub:** [pedroiff0/academicoweb](https://github.com/pedroiff0/academicoweb)
- **Índice de Projetos:** [[pt-br/projects/projetos-publicos|Projetos Públicos]]

---

<p align=center>
  <a href="https://github.com/pedroiff0" target="_blank"><img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub" /></a>
  <a href="https://linkedin.com/in/pedro-andrade-iff" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="https://instagram.com/pedroiff0" target="_blank"><img src="https://img.shields.io/badge/Instagram-E4405F?style=flat-square&logo=instagram&logoColor=white" alt="Instagram" /></a>
  <a href="mailto:pedro.andrade@iff.edu.br"><img src="https://img.shields.io/badge/Email-D14836?style=flat-square&logo=gmail&logoColor=white" alt="Email" /></a>
  <a href="https://pedroiff.com" target="_blank"><img src="https://img.shields.io/badge/Website-000000?style=flat-square&logo=googlechrome&logoColor=white" alt="Website" /></a>
</p>

<p align=center>
  <sub>© 2026 <b><a href="https://pedroiff.com">Pedro Rocha</a></b> — Computer Engineering &amp; Computational Astrophysics</sub><br />
  <sub>Made with <img src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%23888888' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><path d='M10 2v2'/><path d='M14 2v2'/><path d='M16 8a1 1 0 0 1 1 1v8a4 4 0 0 1-4 4H7a4 4 0 0 1-4-4V9a1 1 0 0 1 1-1h14a4 4 0 1 1 0 8h-1'/><path d='M6 2v2'/></svg>" width="16" height="16" valign="middle" alt="coffee" />, <img src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%23888888' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><path d='m16 18 6-6-6-6'/><path d='m8 6-6 6 6 6'/></svg>" width="16" height="16" valign="middle" alt="code" /> and <img src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%23888888' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><circle cx='12' cy='12' r='3'/><path d='M3 12a9 9 0 0 1 9-9 9 9 0 0 1 9 9 9 9 0 0 1-9 9 9 9 0 0 1-9-9'/><path d='M5.5 5.5a13 13 0 0 0 13 13'/><path d='M18.5 5.5a13 13 0 0 1-13 13'/></svg>" width="16" height="16" valign="middle" alt="astrophysics" /> by <b><a href="https://github.com/pedroiff0">Pedro Henrique Rocha de Andrade</a></b></sub>
</p>
