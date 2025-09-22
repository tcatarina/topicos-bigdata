import streamlit as st
import pandas as pd

# --- Configuração da Página ---
# Usar st.set_page_config como o primeiro comando do Streamlit
st.set_page_config(
    page_title="A Jornada da Datatopia",
    page_icon="🚀",
    layout="wide"
)

# --- Dados da Aplicação ---
# Estes são os dados do seu arquivo storytelling.py
funcionarios = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"]

matriz_projetos = [
    [1, 2, 2],  # Ana
    [2, 1, 1],  # Bruno
    [0, 2, 1],  # Carlos
    [1, 2, 0],  # Diana
    [2, 1, 0],  # Eduardo
]

horas_trabalhadas = [40, 35, 30, 45, 38]
especialidades = {
    "Ana": "Data Science",
    "Bruno": "Engenharia de Dados",
    "Carlos": "Machine Learning",
    "Diana": "Análise de Dados",
    "Eduardo": "Business Intelligence"
}

# --- Início da Storytelling no Streamlit ---

st.title("🚀 A Jornada da Datatopia")
st.markdown("Bem-vindo ao painel da Datatopia! Aqui, contamos a história de nossa incrível equipe e seu desempenho inicial através dos dados.")

st.markdown("---")

# --- Seção 1: Apresentação da Equipe ---
st.header("👥 Nossa Equipe Fundadora")
st.markdown("Tudo começou com um time de 5 especialistas apaixonados por transformar dados em soluções. Conheça nossos pioneiros:")

# Usando colunas para uma melhor visualização
cols = st.columns(len(funcionarios))
for i, funcionario in enumerate(funcionarios):
    with cols[i]:
        st.info(f"**{funcionario}**\n\n*{especialidades[funcionario]}*")

st.markdown("---")

# --- Seção 2: Desempenho nos Projetos ---
st.header("📊 Status dos Projetos")
st.markdown("Acompanhe o andamento dos projetos de cada membro da equipe. Para facilitar a visualização, usamos um sistema de status com cores e emojis:")

# Criando um DataFrame para a matriz de projetos e mapeando os valores para status
df_projetos = pd.DataFrame(
    matriz_projetos,
    index=funcionarios,
    columns=["Projeto A", "Projeto B", "Projeto C"]
)

# Mapeamento de status para uma visualização mais clara
status_map = {0: "🔴 Não Iniciado", 1: "🟡 Em Andamento", 2: "🟢 Concluído"}
df_status = df_projetos.replace(status_map)

st.dataframe(df_status, use_container_width=True)

st.markdown("---")

# --- Seção 3: Esforço e Dedicação ---
st.header("⏰ Horas Trabalhadas na Semana")
st.markdown("O sucesso é fruto de dedicação. Veja a distribuição de horas trabalhadas pela equipe na última semana.")

# Criando um DataFrame para o gráfico de barras
df_horas = pd.DataFrame({
    "Funcionário": funcionarios,
    "Horas Trabalhadas": horas_trabalhadas
}).set_index("Funcionário")

st.bar_chart(df_horas)

st.markdown("---")


# --- Seção 4: Resumo Consolidado ---
st.header("🏆 Resumo de Desempenho")
st.markdown("Para uma visão geral, aqui está um resumo consolidado combinando as informações de especialidade, horas e projetos concluídos por cada funcionário.")

# DataFrame final com o resumo
dados_resumo = {
    "Funcionário": funcionarios,
    "Especialidade": [especialidades[nome] for nome in funcionarios],
    "Horas Trabalhadas": horas_trabalhadas,
    "Projetos Concluídos": [linha.count(2) for linha in matriz_projetos]
}
df_resumo = pd.DataFrame(dados_resumo)

st.dataframe(df_resumo, use_container_width=True)

st.success("A jornada da Datatopia está apenas começando! Este painel mostra o poder e o potencial da nossa equipe.")
