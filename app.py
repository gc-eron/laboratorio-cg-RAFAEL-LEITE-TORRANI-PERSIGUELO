import streamlit as st
import numpy as np

st.title("Computação Gráfica")
st.write("Meu nome é Rafael Leite Torrani Persiguelo.")
n = st.slider("Tamanho", 2, 64, 8)
img = np.random.randint(0, 256, (n, n), dtype=np.uint8)
st.image(img, caption=f"Imagem {n}x{n}", width=300)
st.write(img)