
import streamlit as st
import pandas as pd

# Título da página
st.set_page_config(page_title="Finanças", page_icon="💰")

# Texto na página
st.text('Olá, bem vindo ao Streamlit!!')

st.markdown("""
    # Boas vindas!!!
    ## Este é um APP Financeiro!
    ### Seja bem vindo!!
""")

# widget de upload dos dados
file_upload = st.file_uploader(label="📄 Faça upload dos dados aqui:", type=['csv'])

# Verifica se foi feito algum upload
if file_upload:
    # leitura dos dados
    df = pd.read_csv(file_upload)
    df["Data"] = pd.to_datetime(df["Data"], format='%d/%m/%Y').dt.date

    # Exibição dos dados no app
    exp1 = st.expander("Dados Brutos")
    columns_fmt = {"Valor":st.column_config.NumberColumn("Valor", format="R$ %.2f")}
    exp1.dataframe(df, hide_index=True, column_config=columns_fmt)


    # Visão por instituição
    exp2 = st.expander("Instituições")
    df_instituicao = df.pivot_table(index="Data",columns="Instituição", values="Valor")

    # Criando abas
    tab_data, tab_history, tab_share = exp2.tabs(["Dados", "Histórico", "Distribuição"])
    
    # with tab_data:
        # st.dataframe(df_instituicao)
    # OU:
    tab_data.dataframe(df_instituicao)

    with tab_history:
        st.line_chart(df_instituicao)

    with tab_share:
        # usando as datas existentes na planilha como escolha:
        date = st.selectbox("Filtro Data", options=df_instituicao.index)
        st.bar_chart(df_instituicao.loc[date])


        # usando o calendário para opção de escolha:
        # date = st.date_input("Data para Distribuição", 
                  # min_value=df_instituicao.index.min(),
                  # max_value=df_instituicao.index.max())
        
        # if date not in df_instituicao.index:
            # st.warning("Escolha uma data válida!!")
        # else:
            #st.bar_chart(df_instituicao.loc[date])
        

        # Antes de escolher uma data:
        # obtem a última data dos dados instituições
        # last_df = df_instituicao.sort_index().iloc[-1]
        # st.bar_chart(last_df)