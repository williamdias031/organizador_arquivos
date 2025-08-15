# python3
# coding: utf-8 -*-

"""
Organizador Automático de Arquivos
Este script organiza arquivos de uma pasta em subpastas baseadas na extensão.
Exemplo: imagens em "Imagens", PDFs em "PDFs", vídeos em "Vídeos" etc.
"""

import os
import shutil
from pathlib import Path

# Dicionário com extensões e suas respectivas pastas
PASTAS_DESTINO = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documentos": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Áudios": [".mp3", ".wav", ".aac", ".flac"],
    "Vídeos": [".mp4", ".avi", ".mov", ".mkv"],
    "Compactados": [".zip", ".rar", ".7z", ".tar", ".gz"]
}

def organizar_pasta(caminho: str):
    """
    Organiza os arquivos da pasta informada.
    :param caminho: Caminho da pasta a ser organizada.
    """
    pasta = Path(caminho)

    if not pasta.exists() or not pasta.is_dir():
        print("❌ Caminho inválido ou pasta inexistente.")
        return

    arquivos_movidos = 0

    for item in pasta.iterdir():
        if item.is_file():
            ext = item.suffix.lower()

            # Verifica para qual pasta enviar
            destino = None
            for nome_pasta, extensoes in PASTAS_DESTINO.items():
                if ext in extensoes:
                    destino = pasta / nome_pasta
                    break

            # Se não houver categoria definida, vai para "Outros"
            if destino is None:
                destino = pasta / "Outros"

            # Cria a pasta destino, se não existir
            destino.mkdir(exist_ok=True)

            # Move o arquivo
            try:
                shutil.move(str(item), destino / item.name)
                arquivos_movidos += 1
            except Exception as e:
                print(f"Erro ao mover {item.name}: {e}")

    print(f"✅ Organização concluída! {arquivos_movidos} arquivo(s) movido(s).")

if __name__ == "__main__":
    print("=== ORGANIZADOR AUTOMÁTICO DE ARQUIVOS ===")
    caminho_usuario = input("Digite o caminho da pasta a organizar: ").strip()

    if caminho_usuario:
        organizar_pasta(caminho_usuario)
    else:
        print("❌ Nenhum caminho informado.")
