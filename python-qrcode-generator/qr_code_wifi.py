import qrcode
from pathlib import Path
import os
from dotenv import load_dotenv

# Formato padrão para credenciais de Wi-Fi
load_dotenv()
nome_rede = os.getenv("nome_rede")
senha_rede = os.getenv("senha_rede")
texto_wifi = f"WIFI:T:WPA;S:{nome_rede};P:{senha_rede};;" # Esse texto é crucial na aplicação!

# Gera a imagem do QR Code
img = qrcode.make(texto_wifi)

local_script = Path(__file__).parent
destino_imagem = local_script / "qrcode_img"

caminho_imagem = destino_imagem / "qr_code_wifi.png"

img.save(caminho_imagem)
