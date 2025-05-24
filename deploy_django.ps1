# Caminho do projeto
cd "C:\Users\Kin\Desktop\django"

# Variáveis do projeto
$RepoName = "meusite-django"
$GitUser = "yShioon"
$RemoteUrl = "https://github.com/yShioon/meusite-django.git"

# Inicializar Git se ainda não existe
if (!(Test-Path ".git")) {
    git init
    git add .
    git commit -m "Primeiro deploy do projeto Django"
}

# Adicionar remoto (se não existir)
$remotoExiste = git remote | Select-String "origin"
if (-not $remotoExiste) {
    git remote add origin $RemoteUrl
}

# Enviar para o GitHub
git branch -M main
git add .
git commit -m "Atualização para deploy no Render" # Não se preocupe se aparecer 'nada para commitar'
git push -u origin main

Write-Host "Projeto enviado para o GitHub com sucesso!"
Write-Host ""
Write-Host "Agora acesse https://render.com/, crie um novo Web Service e conecte ao repositório:"
Write-Host "    $RemoteUrl"
Write-Host ""
Write-Host "No Render, use estas configurações:"
Write-Host "  Build command: pip install -r requirements.txt && python manage.py collectstatic --noinput"
Write-Host "  Start command: gunicorn meusite.wsgi"
Write-Host ""
Write-Host "Adicione as variáveis de ambiente:"
Write-Host "  DJANGO_SETTINGS_MODULE=meusite.settings"
Write-Host "  SECRET_KEY=sua-chave-super-secreta"
Write-Host "  DEBUG=False"
Write-Host ""
Write-Host "Seu site será publicado em um endereço como https://meusite-django.onrender.com"