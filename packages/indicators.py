import talib as ta

'''
SMA : 単純移動平均
引数data : DataFrame データフレーム
引数period : 期間
引数column : 終値のカラム 初期値'Close'
'''


def SMA(data, period, column='Close'):
    data.Close = data[column]
    data[f'SMA{period}'] = ta.SMA(data.Close, timeperiod=period)
    return data


'''
EMA : 指数平滑移動平均
引数data : DataFrame データフレーム
引数period : 期間
引数column : 終値のカラム 初期値'Close'
'''


def EMA(data, period, column='Close'):
    data.Close = data[column]
    data[f'EMA{period}'] = ta.EMA(data.Close, timeperiod=period)
    return data


'''
BB : ボリンジャーバンド
引数data : DataFrame データフレーム
引数sd : standard deviation 標準偏差
引数period : 期間 初期値20
引数column : 終値のカラム 初期値'Close'
'''


def BB(data, sd, period=20, column='Close'):
    data.Close = data[column]
    upperband, middleband, lowerband = ta.BBANDS(
        data.Close, timeperiod=period, nbdevup=sd, nbdevdn=sd, matype=0)
    data['STD'] = middleband
    data['Upper'] = upperband
    data['Lower'] = lowerband
    return data


'''
RSI
引数data : DataFrame データフレーム
引数period : 引数period : 期間
引数column : 終値のカラム 初期値'Close'
'''


def RSI(data, period, column='Close'):
    close = data[column]
    data[f'RSI{period}'] = ta.RSI(close, timeperiod=period)
    return data


'''
MACD
引数data : DataFrame データフレーム
引数column : 終値のカラム 初期値'Close'
'''


def MACD(data, column='Close'):
    data.Close = data[column]
    macd, macdsignal, _ = ta.MACD(data.Close, fastperiod=12, slowperiod=26, signalperiod=9)
    data['MACD'] = macd
    data['SignalLine'] = macdsignal
    return data


'''
stochastic
引数data : DataFrame データフレー
引数column : 終値のカラム 初期値'Close'
'''


def STOCH(data, column='Close'):
    data.Close = data[column]
    slowk, slowd = ta.STOCH(
        data.High,
        data.Low,
        data.Close,
        fastk_period=14,  # %K Length
        slowk_period=1,  # %K Smoothing
        slowk_matype=0,
        slowd_period=3,  # %D Smoothing
        slowd_matype=0
    )
    data['%K'] = slowk
    data['%D'] = slowd
    return data
