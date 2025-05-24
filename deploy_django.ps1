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

# Configurar safe.directory (para evitar problemas de permissão)
git config --global --add safe.directory "C:/Users/Kin/Desktop/django"

# Enviar para o GitHub
git branch -M main
git add .
git commit -m "Site otimizado para AdSense e SEO" 
git push -u origin main

Write-Host "✅ Projeto enviado para o GitHub com sucesso!"
Write-Host ""
Write-Host "🔧 Configurações para o Render:"
Write-Host "  Build Command: pip install -r requirements.txt && python manage.py collectstatic --noinput"
Write-Host "  Start Command: python manage.py migrate && gunicorn meusite.wsgi"
Write-Host ""
Write-Host "🔑 Variáveis de ambiente necessárias:"
Write-Host "  DJANGO_SETTINGS_MODULE=meusite.settings"
Write-Host "  SECRET_KEY=sua-chave-super-secreta-aqui"
Write-Host "  DEBUG=False"
Write-Host ""
Write-Host "🌐 Seu site será publicado em: https://meusite-django.onrender.com"