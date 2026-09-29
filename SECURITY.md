# Política de Segurança — Quartz Site

## Relato de Vulnerabilidades
Para reportar vulnerabilidades ou vazamentos de dados/notas privadas no site público, entre em contato:
- **Responsável:** Pedro Iff
- **E-mail:** `pedroiff0@gmail.com`

## Criptografia e Privacidade
- Notas privadas contêm flag `publish: false` ou são criptografadas via Quartz Encrypt (`QUARTZ_ENCRYPT_PASSWORD`).
- O build de deploy é configurado para omitir qualquer nota de diário pessoal ou arquivo com dados sensíveis.
