import os
import google.generativeai as genai
import json
from dotenv import load_dotenv
from PIL import Image

load_dotenv()

def reduzir_tamanho(pasta_origem, pasta_destino, largura_max=800):
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    for nome_arquivo in os.listdir(pasta_origem):
        if nome_arquivo.lower().endswith(('.jpg', '.jpeg', '.png')):
            caminho_original = os.path.join(pasta_origem, nome_arquivo)
            caminho_novo = os.path.join(pasta_destino, nome_arquivo)

            img = Image.open(caminho_original)

            # Redimensiona mantendo a proporção
            proporcao = largura_max / float(img.size[0])
            altura_nova = int((float(img.size[1]) * float(proporcao)))

            img = img.resize((largura_max, altura_nova), Image.Resampling.LANCZOS)

            img = img.convert('RGB')  # garante compatibilidade JPEG
            img.save(caminho_novo, format='JPEG', optimize=True, quality=85)

            print(f"Imagem {nome_arquivo} redimensionada e salva em {pasta_destino}")

genai.configure(api_key=os.getenv("API_KEY-GEMINI"))
model = genai.GenerativeModel('gemini-2.0-flash')

def listar_imagens(pasta):
    imagens = []
    for nome_arquivo in sorted(os.listdir(pasta)):
        if nome_arquivo.lower().endswith(('.jpg', '.jpeg', '.png')):
            imagens.append(os.path.join(pasta, nome_arquivo))
        else:
            print(f"Modelo de imagem não reconhecido: {nome_arquivo}")
    return imagens

def reconhecer_numeros_lote(imagens):
    numeros = []
    for i in range(0, len(imagens), 10):
        lote = imagens[i:i+10]
        
        gemini_imgs = []
        for img in lote:
            with open(img, "rb") as f:
                data = f.read()
            gemini_imgs.append({
                "mime_type": "image/jpeg",
                "data": data
            })

        prompt = (
            """As imagens enviadas a seguir são de um contador de água ou de um contador de energia.
            Para cada uma delas, extraia e informe apenas o número visível, mantendo a ordem de envio.
            Responda com uma lista numérica JSON, exemplo: [123, 456, 789].
            Não adicione explicações ou textos extras, apenas a lista."""
        )

        response = model.generate_content([prompt] + gemini_imgs)
        texto = response.text.strip()

        try:
            lista = json.loads(texto)
        except:

            lista = [int(s) for s in texto.split() if s.isdigit()]

        numeros.extend(lista)
    
    return numeros

def montar_json(numeros_agua, numeros_energia):
    resultado = {}
    for dia in range(7):
        inicio = dia * 3
        fim = inicio + 3
        resultado[f"dia{dia+1}"] = {
            "agua": numeros_agua[inicio:fim],
            "energia": numeros_energia[inicio:fim]
        }
    return resultado

def ai():

    # Diretórios base
    base_dir = os.path.dirname(__file__)

    pasta_origem_agua = os.path.join(base_dir, '..', 'data', 'fotos_Agua')
    pasta_destino_agua = os.path.join(base_dir, '..', 'data', 'fotos_Agua_Reduzidas')
    reduzir_tamanho(pasta_origem_agua, pasta_destino_agua, largura_max=800)

    pasta_origem_energia = os.path.join(base_dir, '..', 'data', 'fotos_Energia')
    pasta_destino_energia = os.path.join(base_dir, '..', 'data', 'fotos_Energia_Reduzidas')
    reduzir_tamanho(pasta_origem_energia, pasta_destino_energia, largura_max=800)

    imagens_agua = listar_imagens(pasta_destino_agua)
    imagens_energia = listar_imagens(pasta_destino_energia)

    assert len(imagens_agua) == 21, f"Deve haver exatamente 21 imagens de água, mas há {len(imagens_agua)}."
    assert len(imagens_energia) == 21, f"Deve haver exatamente 21 imagens de energia, mas há {len(imagens_energia)}."

    print("Processando imagens de água...")
    numeros_agua = reconhecer_numeros_lote(imagens_agua)

    print("Processando imagens de energia...")
    numeros_energia = reconhecer_numeros_lote(imagens_energia)

    resultado = montar_json(numeros_agua, numeros_energia)
    
    return resultado
