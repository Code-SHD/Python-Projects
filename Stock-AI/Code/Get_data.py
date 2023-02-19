import yfinance as yf

df = yf.download('005930.KS', '2021-10-03', '2022-10-03')
df.to_excel("Samsung_Stock.xlsx")
df.to_csv("Samsung_Stock.csv")
