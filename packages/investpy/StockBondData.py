import investpy
from dateutil.relativedelta import relativedelta
from datetime import date

'''
メソッドindexDataFromToday
引数bond : 金利（U.S. 10Y）
引数period : データの期間（年）
'''


def stockBondsData(bond, period):
    end = date.today().strftime('%d/%m/%Y')
    start = (date.today() - relativedelta(years=period)).strftime('%d/%m/%Y')
    # print(f"{ticker}・期間：{start}〜{end}")
    df = investpy.bonds.get_bond_historical_data(
        bond=bond,
        from_date=start,
        to_date=end
    )
    return df


'''
メソッドstockBondsDataFromDD(designated day)
引数bond : 金利（U.S. 10Y）
引数period : データの期間（年）
引数d_start : データの最終日
'''


def stockBondsDataFromDD(bond, period, d_start):
    end = d_start.strftime('%d/%m/%Y')
    start = (d_start - relativedelta(years=period)).strftime('%d/%m/%Y')
    # print(f"{ticker}・期間：{start}〜{end}")
    df = investpy.bonds.get_bond_historical_data(
        bond=bond,
        from_date=start,
        to_date=end
    )
    return df
