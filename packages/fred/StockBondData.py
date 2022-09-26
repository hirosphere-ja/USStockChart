import pandas as pd
from pandas_datareader import data
from dateutil.relativedelta import relativedelta
from datetime import date

'''
メソッドBondsDataFromToday
引数bond : 米国債利回り年数（年）
引数period : データの期間（年）
'''

def stockBondsData(bond, period):
	end = pd.to_datetime(date.today(), format='%d/%m/%Y', infer_datetime_format=True)
	start = pd.to_datetime((date.today() - relativedelta(years=period)), format='%d/%m/%Y', infer_datetime_format=True)
	df = data.DataReader(f"DGS{bond}", "fred", start, end)
	return df


'''
メソッドBondsDataFromDD(designated day)
引数bond : 米国債利回り年数（年）
引数period : データの期間（年）
引数d_start : データの最終日
'''


def stockBondsDataFromDD(bond, period, d_start):
	d_start = pd.to_datetime(d_start, format='%d/%m/%Y', infer_datetime_format=True)
	end = pd.to_datetime(d_start, format='%d/%m/%Y', infer_datetime_format=True)
	start = pd.to_datetime((d_start - relativedelta(years=period)), format='%d/%m/%Y', infer_datetime_format=True)
	df = data.DataReader(f"DGS{bond}", "fred", start, end)
	return df
