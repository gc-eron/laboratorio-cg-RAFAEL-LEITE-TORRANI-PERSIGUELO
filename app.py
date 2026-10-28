import streamlit as st

paginas = [
    st.Page("src/atv1.py", title="Ativ 1"),
    st.Page("src/atv2.py", title="Ativ 2"),
]
st.navigation(paginas).run()