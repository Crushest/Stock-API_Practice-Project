#market data
import yfinance as yf

#panda-datareader takes data from yahoo finance API
yf.pdr_override()

#User inputs to choose specific ticker symbol to view stock
stock=input("Enter a stock symbol:")

#takes stock symbol and gets data for past 3 days at one day intervals
tick = yf.download(tickers=stock,period='3d',interval='1d')
#only gets the the latest close for the past 3 days
close = tick["Close"]
#Shows stock information that was inputed by the user | Shows past 3 days
print("Here is the", stock, "stock for the past three days:\n", (close))

# !Enter a stock symbol:NVDA
# ![*********************100%***********************]  1 of 1 completed
# !Here is the NVDA stock for the past three days:
# !Date
# !2022-08-03    188.929993
# !2022-08-04    192.149994
# !2022-08-05    189.080002
# !Name: Close, dtype: float64
# !PS C:\Users\sebie\OneDrive\Documents\Python> 

# *Enter a stock symbol:TSLA
# *[*********************100%***********************]  1 of 1 completed
# *Here is the TSLA stock for the past three days:
# * Date
# *2022-08-03    922.190002
# *022-08-04    925.900024
# *2022-08-05    873.179993
# *Name: Close, dtype: float64
# *PS C:\Users\sebie\OneDrive\Documents\Python> 

# Enter a stock symbol:GOOGL
# [*********************100%***********************]  1 of 1 completed
# Here is the GOOGL stock for the past three days:
#  Date
# 2022-08-03    118.080002
# 2022-08-04    118.190002
# 2022-08-05    117.440002
# Name: Close, dtype: float64
# PS C:\Users\sebie\OneDrive\Documents\Python> 