import pandas as pd
from pandas_datareader import data
from dateutil.relativedelta import relativedelta
from datetime import date

'''
メソッドVIXDataFromToday
引数period : データの期間（年）
'''

def VIXData(period):
	end = pd.to_datetime(date.today(), format='%d/%m/%Y', infer_datetime_format=True)
	start = pd.to_datetime((date.today() - relativedelta(years=period)), format='%d/%m/%Y', infer_datetime_format=True)
	df = data.DataReader("^VIX", "yahoo", start, end)
	return df


'''
メソッドVIXDataFromDD(designated day)
引数period : データの期間（年）
引数d_start : データの最終日
'''


def VIXDataFromDD(period, d_start):
	d_start = pd.to_datetime(d_start, format='%d/%m/%Y', infer_datetime_format=True)
	end = pd.to_datetime(d_start, format='%d/%m/%Y', infer_datetime_format=True)
	start = pd.to_datetime((d_start - relativedelta(years=period)), format='%d/%m/%Y', infer_datetime_format=True)
	df = data.DataReader("^VIX", "yahoo", start, end)
	return df
