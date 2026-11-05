import streamlit as st

paginas = [
    st.Page("src/atv1.py", title="Ativ 1"),
    st.Page("src/atv2.py", title="Ativ 2"),
    st.Page("src/atv3.py", title="Ativ 3"),
    st.Page("src/atv4.py", title="Ativ 4"),
]
st.navigation(paginas).run()