
import streamlit as st
import pandas as pd
import requests
import datetime

@st.cache_data(ttl="1day")      # retorna um valor cacheado (não irá buscar sempre que a data for alterada)
def get_selic():
    url = "https://www.bcb.gov.br/api/servico/sitebcb/historicotaxasjuros"
    resp = requests.get(url)
    df_selic = pd.DataFrame(resp.json()["conteudo"])
    df_selic["DataInicioVigencia"] = pd.to_datetime(df_selic["DataInicioVigencia"]).dt.date
    df_selic["DataFimVigencia"] = pd.to_datetime(df_selic["DataFimVigencia"]).dt.date
    df_selic["DataFimVigencia"] = df_selic["DataFimVigencia"].fillna(datetime.datetime.today().date())
    return df_selic

def calc_general_stats(df: pd.DataFrame):
    df_data = df.groupby(by="Data")[["Valor"]].sum()
    # shift(1): avança uma linha e segue com os dados
    df_data["lag_1"] = df_data["Valor"].shift(1)

    df_data["Diferença Mensal Abs."] = df_data["Valor"] - df_data["lag_1"]
    df_data["Media 6M Diferença Mensal Abs."] = round(df_data["Diferença Mensal Abs."].rolling(6).mean(),2)
    df_data["Media 12M Diferença Mensal Abs."] = round(df_data["Diferença Mensal Abs."].rolling(12).mean(),2)
    df_data["Media 24M Diferença Mensal Abs."] = round(df_data["Diferença Mensal Abs."].rolling(24).mean(),2)

    df_data["Diferença Mensal Relat."] = df_data["Valor"] / df_data["lag_1"] - 1

    df_data["Evolução 6M Total"] = df_data["Valor"].rolling(6).apply(lambda x: x.iloc[-1] - x.iloc[0])
    df_data["Evolução 12M Total"] = df_data["Valor"].rolling(12).apply(lambda x: x.iloc[-1] - x.iloc[0])
    df_data["Evolução 24M Total"] = df_data["Valor"].rolling(24).apply(lambda x: x.iloc[-1] - x.iloc[0])

    df_data["Evolução 6M Relativa"] = df_data["Valor"].rolling(6).apply(lambda x: x.iloc[-1] / x.iloc[0] -1)
    df_data["Evolução 12M Relativa"] = df_data["Valor"].rolling(12).apply(lambda x: x.iloc[-1] / x.iloc[0] -1)
    df_data["Evolução 24M Relativa"] = df_data["Valor"].rolling(24).apply(lambda x: x.iloc[-1] / x.iloc[0] -1)

    df_data = df_data.drop("lag_1", axis=1)

    return df_data

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
    columns_inst_format = {
        "Death Star": st.column_config.NumberColumn("Death Star", format='R$ %.2f'),
        "Iron Bank": st.column_config.NumberColumn("Iron Bank", format='R$ %.2f'),
        "Republic Bank": st.column_config.NumberColumn("Republic Bank", format='R$ %.2f'),
        "TMW Bank": st.column_config.NumberColumn("TMW Bank", format='R$ %.2f'),
    }
    df_instituicao = df.pivot_table(index="Data",columns="Instituição", values="Valor")
    
    # Criando abas
    tab_data, tab_history, tab_share = exp2.tabs(["Dados", "Histórico", "Distribuição"])
    
    # with tab_data:
        # st.dataframe(df_instituicao)
    # OU:
    tab_data.dataframe(df_instituicao, column_config=columns_inst_format)

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
    
    # Visão com dados estatísticos
    exp3 = st.expander("Estatísticas Gerais")
    df_stats = calc_general_stats(df)

    columns_config = {
    "Valor": st.column_config.NumberColumn("Valor", format='R$ %.2f'),
    "Diferença Mensal Abs.": st.column_config.NumberColumn("Diferença Mensal Abs.", format='R$ %.2f'),
    "Media 12M Diferença Mensal Abs.": st.column_config.NumberColumn("Media 12M Diferença Mensal Abs.", format='R$ %.2f'),
    "Media 24M Diferença Mensal Abs.": st.column_config.NumberColumn("Media 24M Diferença Mensal Abs.", format='R$ %.2f'),
    "Media 6M Diferença Mensal Abs.": st.column_config.NumberColumn("Media 6M Diferença Mensal Abs.", format='R$ %.2f'),
    "Evolução 6M Total": st.column_config.NumberColumn("Evolução 6M Total", format='R$ %.2f'),
    "Evolução 12M Total": st.column_config.NumberColumn("Evolução 12M Total", format='R$ %.2f'),
    "Evolução 24M Total": st.column_config.NumberColumn("Evolução 24M Total", format='R$ %.2f'),
    "Diferença Mensal Relat." : st.column_config.NumberColumn("Diferença Mensal Relat.", format='percent'),
    "Evolução 6M Relativa": st.column_config.NumberColumn("Evolução 6M Relativa", format='percent'),
    "Evolução 12M Relativa": st.column_config.NumberColumn("Evolução 12M Relativa", format='percent'),
    "Evolução 24M Relativa": st.column_config.NumberColumn("Evolução 24M Relativa", format='percent'),
    }

    tab_stats, tab_abs, tab_rel = exp3.tabs(tabs=["Dados", "Histórico de Evolução", "Crescimento Relatiovo"])

    with tab_stats:
        st.dataframe(df_stats, column_config=columns_config)

    with tab_abs:
        abs_cols = ["Diferença Mensal Abs.",
                "Media 6M Diferença Mensal Abs.", 
                "Media 12M Diferença Mensal Abs.", 
                "Media 24M Diferença Mensal Abs."  ]
        st.line_chart(df_stats[abs_cols])
    
    with tab_rel:
        rel_cols = ["Diferença Mensal Relat.",
                "Evolução 6M Relativa", 
                "Evolução 12M Relativa", 
                "Evolução 24M Relativa"  ]
        st.line_chart(df_stats[rel_cols])
    
    with st.expander("Metas"):
        col1, col2 = st.columns(2)
        data_inicio_meta = col1.date_input("Inicio da Meta", max_value=df_stats.index.max())
        data_filtrada = df_stats.index[df_stats.index <= data_inicio_meta][-1]
        
        custos_fixos = col1.number_input("Custos Fixos", min_value=0., format="%.2f")
        salario_bruto = col2.number_input("Salário Bruto", min_value=0., format="%.2f")
        salario_liquido = col2.number_input("Salário Líquido", min_value=0., format="%.2f")
        
        valor_inicio = df_stats.loc[data_filtrada]["Valor"]
        col1.markdown(f"**Patrimônio no Início da Meta:** R$ {valor_inicio:.2f}")

        selic_gov = get_selic()
        filter_selic_date = (selic_gov["DataInicioVigencia"] < data_inicio_meta) & (selic_gov["DataInicioVigencia"] > data_inicio_meta)
        selic_default = selic_gov[filter_selic_date]["MetaSelic"].iloc[0]

        selic = st.number_input("Selic", min_value=0., value=selic_default, format="%.2f")
        selic_ano = selic / 100
        selic_mes = (selic_ano + 1) ** (1/12) -1

        st.text(f"Selic Ano: {100*selic_ano:.2f}%")
        st.text(f"Selic Mês: {100*selic_mes:.2f}%")


        rendimento_ano = valor_inicio * selic_ano
        rendimento_mes = valor_inicio * selic_mes

        col1_pot, col2_pot = st.columns(2)
        mensal = salario_liquido - custos_fixos + valor_inicio * selic_ano
        anual = 12*(salario_liquido - custos_fixos) + valor_inicio * selic_ano

        with col1_pot.container(border=True):
            st.markdown(f"**Potencial Arrecadação Mês**:\n  R$ {mensal:.2f}", help = (f"{salario_liquido:.2f}-{custos_fixos:.2f}+{rendimento_mes:.2f})"))
        with col2_pot.container(border=True):
            st.markdown(f"**Potencial Arrecadação Ano**:\n  R$ {anual:.2f}", help = (f"12*({salario_liquido:.2f}+(-{custos_fixos:.2f})+{rendimento_ano:.2f})"))
        
        with st.container(border=True):
            col1_meta, col2_meta = st.columns(2)
            with col1_meta:
                meta_estipulada = st.number_input("Meta Estipulada", min_value=-99999999., format="%.2f", value=anual)
            with col2_meta:
                patrimonio_final = meta_estipulada + valor_inicio
                st.markdown(f"Patrimônio Estimado Pós Meta:\n\n R$ {patrimonio_final:.2f}")