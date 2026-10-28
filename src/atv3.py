import numpy as np
import streamlit as st

def ampliar(imagem, k=30):
    return imagem.repeat(k, axis=0).repeat(k, axis=1)

st.title("Atividade 3 - Padrão")

k = st.slider("k", 1, 20, 4)

y, x = np.indices((64, 64))

def padrao(x, y, k):
    return (x + y * k) % 256

imagem = padrao(x, y, k).astype(np.uint8)

st.image(ampliar(imagem, 4))