# Para usar o projeto

```powershell
python -m venv .venv
#Linux
source ./.venv/bin/activate
#Windows
.\.venv\Scripts\Activate.ps1

# Instale ou atualize pacotes conforme necessário
pip install <nome_do_pacote>
pip install --upgrade <nome_do_pacote>

# Atualize o arquivo requirements.txt
pip freeze > requirements.txt
# Quando o arquivo requirements.txt ja existir
pip install -r ./src/requirements.txt
```

## Criar um arquivo executavel

```powershell
pip install pyinstaller

pyinstaller --onefile simnext-fullscreen.py

```


## Para executar na inicialização do windows

```powershell
# No windows 11, Windows + R
# shell:startup
# Inclua essas linhas no script simnext.bat
timeout /t 10 /nobreak
start "" "caminho\para\simnext-fullscreen.exe"
```
