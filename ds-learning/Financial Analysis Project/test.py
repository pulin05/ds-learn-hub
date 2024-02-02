from datetime import datetime
import yfinance as yf
import mplfinance as mpf
start_date = datetime(2019, 1, 1)
end_date = datetime(2019, 12, 31)
data = yf.download('TATASTEEL.NS', start=start_date, end=end_date)
mpf.plot(data,type='candle',mav=(3,6,9),volume=True,show_nontrading=True)