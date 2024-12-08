import streamlit as st
import pandas as pd
from io import BytesIO

# Caminho para o arquivo Excel
file_path = r"C:\python\1- projeto soffia\plantoes2.xlsx"

# Carregar a segunda aba do Excel
data = pd.read_excel(file_path, sheet_name=1)

# Transformar colunas em linhas
transposed_data = data.T  # Usando o método transpose()

# Configuração do Streamlit
st.title("Transformar Coluna em Linha")
st.write("Tabela original:")
st.dataframe(data)

st.write("Tabela com colunas transformadas em linhas:")
st.dataframe(transposed_data)

# Criar um buffer de memória para salvar o arquivo Excel
buffer = BytesIO()
with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
    transposed_data.to_excel(writer, index=False)

# Botão para baixar a tabela transposta
st.download_button(
    label="Baixar tabela transposta em Excel",
    data=buffer.getvalue(),
    file_name="tabela_transposta.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
)
