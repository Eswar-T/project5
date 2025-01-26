import streamlit as lit


lit.set_page_config(layout="wide")
col1, col2 = lit.columns(2)

with col1:
    lit.image("images/photo.png")

with col2:
    lit.title("Eshwar")
    content = "he standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from de Finibus Bonorum et Malorum by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham."
    lit.info(content)

content1 = "he standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from de Finibus Bonorum et Malorum by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham."
lit.write(content1)

