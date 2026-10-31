from scripts.analysis_common import *
from scripts.fetch_data import ensure_data
PROJECT='Bitcoin-Price-Timeforecasting'

def run(mode='full'):
    data=ensure_data(ROOT/'dataset')
    if PROJECT=='Bitcoin-Price-Timeforecasting':
        df=pd.read_csv(data/'BTC_USD_2013-10-01_2021-05-18-CoinDesk.csv',parse_dates=['Date']).set_index('Date').sort_index()
        assert df.index.is_unique
        df['target']=pd.to_numeric(df['Closing Price (USD)'])
        for lag in range(1,31):df[f'lag_{lag}']=df.target.shift(lag)
        return temporal_regression(df,[f'lag_{i}' for i in range(1,31)],'target',
            'Forecast the next daily Bitcoin close from closes already observed at the forecast origin; compare with the last-close baseline.')
    df=pd.read_csv(data/'mediacompany.csv',parse_dates=['Date']).set_index('Date').sort_index()
    assert df.index.is_unique
    df['target']=df.Views_show;df['lag_1']=df.target.shift(1)
    for c in ['Visitors','Ad_impression','Views_platform']:df['previous_'+c]=df[c].shift(1)
    df['trend_day']=(df.index-df.index.min()).days;df['weekday']=df.index.dayofweek
    return temporal_regression(df,['lag_1','previous_Visitors','previous_Ad_impression','previous_Views_platform','trend_day','weekday'],'target',
        'Forecast next-day show views from previous-day observations and known calendar features. Current-day audience/ad totals are unavailable at forecast time and are excluded.')
