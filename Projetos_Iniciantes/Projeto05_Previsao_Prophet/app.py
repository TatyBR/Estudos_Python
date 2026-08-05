#%%
import streamlit as st
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go
from datetime import date

#%%
lista_tickers = ["PETR4.SA","ABEV3.SA","MGLU3.SA","BRAS3.SA", "GOOG", "APPLE", "MSFT"]

tickers ={
    "PETR4.SA": "Petrobrás",
    "ABEV3.SA": "Ambev",
    "MGLU3.SA": "Magazine Luiza",
    "BRAS3.SA": "Banco do Brasil",
    "GOOG": "Google",
    "AAPL": "Apple",
    "MSFT": "Microsoft",
}

def carregar_dados(ticker, data_inicial, data_final):
    df_dados = yf.Ticker(ticker).history(start=data_inicial.strftime("%Y-%m-%d"), 
                                         end=data_final.strftime("%Y-%m-%d"))
    return df_dados

def prever_dados(df, periodo):
    df.reset_index(inplace=True)
    df = df.loc[:, ['Date', 'Close']]
    df['Date'] = df['Date'].dt.tz_localize(None)
    # nomes padronizados para serem usados pelo Prophet
    df.rename(columns={"Date": "ds", "Close": "y"}, inplace=True)

    modelo = Prophet()
    modelo.fit(df)

    datas_futuras = modelo.make_future_dataframe(periods=int(periodo * 30))
    previsoes = modelo.predict(datas_futuras)

    return modelo, previsoes

# %%

# col1, col2, col3 = st.columns([1, 2, 1])

# with col2:
    # st.image("logo.jpg", width=400)

st.markdown("""
# 💵 Análise Preditiva de Ações
### Prevendo o valor de ações na Bolsa de Valores com Prophet
""")

with st.sidebar:
     st.image("logo.jpg", width=400)
     ticker = st.selectbox("Selecione a ação:", lista_tickers)
     data_inicial = st.date_input("Data de início:", value=date(2020, 1, 1))
     # em data_final irá trazer sempre a data do dia atual
     data_final = st.date_input("Data de fim:")
     meses = st.number_input("Meses de previsão:", 1, 24, value=6)

dados = carregar_dados(ticker, data_inicial, data_final)

if dados.shape[0] == 0:
    st.warning("Não há dados disponíveis para o período selecionado.")

else:
    st.header(f"{tickers[ticker]}")
    st.subheader(f"Período de {data_inicial} a {data_final}")
    exp1 = st.expander(f"Dados")
    exp1.dataframe(dados)

    exp2 = st.expander("Visualização")

    tab_variacao, tab_previsao = exp2.tabs(["Variação do período", f"Previsão para o(s) próximo(s) {meses} meses(mês)"])
    with tab_variacao:
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=dados.index, y=dados['Close'], name="Close", line_color='blue'))
        st.plotly_chart(fig)

    with tab_previsao:
        modelo, previsoes = prever_dados(dados, meses)
        fig = plot_plotly(modelo, previsoes, xlabel="Período", ylabel="Valor da ação")
        st.plotly_chart(fig)