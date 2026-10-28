import numpy as np
import streamlit as st

def ampliar(imagem, k=20):
    return imagem.repeat(k, axis=0).repeat(k, axis=1)

st.title("Bandeira da França")

altura, largura = 30, 45

bandeira = np.zeros((altura, largura, 3), dtype=np.uint8)

bandeira[:, :15] = (0, 85, 164)# Azul
bandeira[:, 15:30] = (255, 255, 255)# Branco
bandeira[:, 30:] = (239, 65, 53)# Vermelho
st.image(ampliar(bandeira))