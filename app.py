import streamlit as st

paginas = [
    st.Page("src/laboratorio_cg/ativ1.py", title="Ativ 1"),
    st.Page("src/laboratorio_cg/ativ2.py", title="Ativ 2"),
]
st.navigation(paginas).run()