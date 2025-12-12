# Gera QRCODE para "jogar para um site"

import qrcode
from pathlib import Path

# --- Configurações do QR Code ---
qr = qrcode.QRCode(
    version=1,  # Controla o tamanho do QR Code (1 a 40). None para ajuste automático.
    error_correction=qrcode.constants.ERROR_CORRECT_M,  # Nível de correção de erro (L, M, Q, H)
    box_size=15,  # Tamanho em pixels de cada "caixa" do QR Code
    border=4,     # Espessura da borda (o mínimo é 4)
)

# --- Dados e Geração da Imagem ---
URL = "https://gemini.google.com/app/539d771e6a4ca9e6?hl=pt-BR"
qr.add_data(URL)
qr.make(fit=True) # A opção fit=True ajusta a versão automaticamente

# Cria a imagem com cores personalizadas
img = qr.make_image(fill_color="black", back_color="white")

# Salva o arquivo de imagem
local_script = Path(__file__).parent 
pasta_destino = local_script / "qrcode_img"

pasta_destino.mkdir(parents=True, exist_ok=True)

caminho_do_arquivo = pasta_destino / "qrcode_site.png"

img.save(caminho_do_arquivo)

# version: É um número inteiro de 1 a 40 que controla o tamanho da matriz do QR Code (um version 1 tem 21x21 caixas). Se você usar fit=True na função make(), ele escolherá o menor tamanho possível para os seus dados.

# error_correction: Define o quanto de dano o QR Code pode sofrer e ainda ser lido.

# ERROR_CORRECT_L: Cerca de 7% de erros podem ser corrigidos.

# ERROR_CORRECT_M (padrão): Cerca de 15%.

# ERROR_CORRECT_Q: Cerca de 25%.

# ERROR_CORRECT_H: Cerca de 30%.

# box_size: Define o tamanho de cada "pixel" do QR Code.

# border: Define a largura da borda branca ao redor do código.

# fill_color: A cor dos quadrados do QR Code (cor do preenchimento).

# back_color: A cor do fundo.