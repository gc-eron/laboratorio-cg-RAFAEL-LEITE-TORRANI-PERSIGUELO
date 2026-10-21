import numpy as np
import streamlit as st

def ampliar(imagem, k=20):
    return imagem.repeat(k, axis=0).repeat(k, axis=1)

st.title("Bandeira do Japão")

altura, largura = 60, 90

bandeira = np.zeros((altura, largura, 3), dtype=np.uint8)
bandeira[:, :] = (255, 255, 255)  # Branco

# Círculo de vermelho
y, x = np.mgrid[0:altura, 0:largura]
cx, cy = largura // 2, altura // 2
raio = 18
circulo = (x - cx)**2 + (y - cy)**2 <= raio**2
bandeira[circulo] = (188, 0, 45)

st.image(ampliar(bandeira), use_container_width=True)