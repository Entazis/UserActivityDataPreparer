import pandas as pd
import numpy as np


user_activity = pd.read_csv('user-activity.csv', delim_whitespace=True,
                            parse_dates=True, infer_datetime_format=True, usecols=range(0, 250),  # nrows=1000,
                            ).set_index(['userid']).drop(['churn', 'locale'], axis=1)
user_locale = pd.read_csv('user-data.csv', delim_whitespace=True).set_index(['userid']).drop(['churn', '0'], axis=1)

user_activity = user_activity.astype(pd.Timestamp)
user_activity_all = user_locale.merge(user_activity, left_index=True, right_index=True)
user_activity_huHU = user_activity_all.loc[user_activity_all['locale'] == 'hu-HU', :].drop(['locale'], axis=1)
user_activity_plPL = user_activity_all.loc[user_activity_all['locale'] == 'pl-PL', :].drop(['locale'], axis=1)
user_activity_roRO = user_activity_all.loc[user_activity_all['locale'] == 'ro-RO', :].drop(['locale'], axis=1)
user_activity_trTR = user_activity_all.loc[user_activity_all['locale'] == 'tr-TR', :].drop(['locale'], axis=1)
user_activity_hiIN = user_activity_all.loc[user_activity_all['locale'] == 'hi-IN', :].drop(['locale'], axis=1)
user_activity_idID = user_activity_all.loc[user_activity_all['locale'] == 'id-ID', :].drop(['locale'], axis=1)
user_activity_viVN = user_activity_all.loc[user_activity_all['locale'] == 'vi-VN', :].drop(['locale'], axis=1)
user_activity_enNG = user_activity_all.loc[user_activity_all['locale'] == 'en-NG', :].drop(['locale'], axis=1)
user_activity_esAR = user_activity_all.loc[user_activity_all['locale'] == 'es-AR', :].drop(['locale'], axis=1)
user_activity_esMX = user_activity_all.loc[user_activity_all['locale'] == 'es-MX', :].drop(['locale'], axis=1)
user_activity_ptBR = user_activity_all.loc[user_activity_all['locale'] == 'pt-BR', :].drop(['locale'], axis=1)
print(user_activity.columns)
print(user_activity.head())
print(user_activity.shape)

dates_sr = pd.date_range(start='2016-04-01', end='2018-12-31', freq='D')
dau_df = pd.DataFrame(index=dates_sr)
dau_df.index.name = 'date'

months_sr = pd.date_range(start='2016-04-01', end='2018-12-31', freq='MS')
mau_df = pd.DataFrame(index=months_sr)
mau_df.index.name = 'date'

for month in months_sr:
    print(month)
    range = pd.date_range(start=month,
                          end=month + pd.DateOffset(months=1),
                          freq='D', closed='left').strftime(date_format="%Y-%m-%d").tolist()
    activity_cnt = user_activity.isin(range).any(axis='columns').sum()
    mau_df.loc[month, 'all'] = int(activity_cnt)

    # print('hu-HU ' + str(month))
    activity_cnt = user_activity_huHU.isin(range).any(axis='columns').sum()
    mau_df.loc[month, 'hu-HU'] = int(activity_cnt)

    # print('pl-PL ' + str(month))
    activity_cnt = user_activity_plPL.isin(range).any(axis='columns').sum()
    mau_df.loc[month, 'pl-PL'] = int(activity_cnt)

    # print('ro-RO ' + str(month))
    activity_cnt = user_activity_roRO.isin(range).any(axis='columns').sum()
    mau_df.loc[month, 'ro-RO'] = int(activity_cnt)

    # print('tr-TR ' + str(month))
    activity_cnt = user_activity_trTR.isin(range).any(axis='columns').sum()
    mau_df.loc[month, 'tr-TR'] = int(activity_cnt)

    # print('hi-IN ' + str(month))
    activity_cnt = user_activity_hiIN.isin(range).any(axis='columns').sum()
    mau_df.loc[month, 'hi-IN'] = int(activity_cnt)

    # print('id-ID ' + str(month))
    activity_cnt = user_activity_idID.isin(range).any(axis='columns').sum()
    mau_df.loc[month, 'id-ID'] = int(activity_cnt)

    # print('vi-VN ' + str(month))
    activity_cnt = user_activity_viVN.isin(range).any(axis='columns').sum()
    mau_df.loc[month, 'vi-VN'] = int(activity_cnt)

    # print('en-NG ' + str(month))
    activity_cnt = user_activity_enNG.isin(range).any(axis='columns').sum()
    mau_df.loc[month, 'en-NG'] = int(activity_cnt)

    # print('es-AR ' + str(month))
    activity_cnt = user_activity_esAR.isin(range).any(axis='columns').sum()
    mau_df.loc[month, 'es-AR'] = int(activity_cnt)

    # print('es-MX ' + str(month))
    activity_cnt = user_activity_esMX.isin(range).any(axis='columns').sum()
    mau_df.loc[month, 'es-MX'] = int(activity_cnt)

    # print('pt-BR ' + str(month))
    activity_cnt = user_activity_ptBR.isin(range).any(axis='columns').sum()
    mau_df.loc[month, 'pt-BR'] = int(activity_cnt)

mau_df = mau_df.reset_index()
mau_df.iloc[:, :].to_csv('mau-all-locales.csv', index=False, sep='\t')

for date in dates_sr:
    print(date)
    range = pd.date_range(start=date,
                         end=date).strftime(date_format="%Y-%m-%d").tolist()
    activity_cnt = user_activity.isin(range).any(axis='columns').sum()
    dau_df.loc[date, 'all'] = int(activity_cnt)

    # print('hu-HU ' + str(date))
    activity_cnt = user_activity_huHU.isin(range).any(axis='columns').sum()
    dau_df.loc[date, 'hu-HU'] = int(activity_cnt)

    # print('pl-PL ' + str(date))
    activity_cnt = user_activity_plPL.isin(range).any(axis='columns').sum()
    dau_df.loc[date, 'pl-PL'] = int(activity_cnt)

    # print('ro-RO ' + str(date))
    activity_cnt = user_activity_roRO.isin(range).any(axis='columns').sum()
    dau_df.loc[date, 'ro-RO'] = int(activity_cnt)

    # print('tr-TR ' + str(date))
    activity_cnt = user_activity_trTR.isin(range).any(axis='columns').sum()
    dau_df.loc[date, 'tr-TR'] = int(activity_cnt)

    # print('hi-IN ' + str(date))
    activity_cnt = user_activity_hiIN.isin(range).any(axis='columns').sum()
    dau_df.loc[date, 'hi-IN'] = int(activity_cnt)

    # print('id-ID ' + str(date))
    activity_cnt = user_activity_idID.isin(range).any(axis='columns').sum()
    dau_df.loc[date, 'id-ID'] = int(activity_cnt)

    # print('vi-VN ' + str(date))
    activity_cnt = user_activity_viVN.isin(range).any(axis='columns').sum()
    dau_df.loc[date, 'vi-VN'] = int(activity_cnt)

    # print('en-NG ' + str(date))
    activity_cnt = user_activity_enNG.isin(range).any(axis='columns').sum()
    dau_df.loc[date, 'en-NG'] = int(activity_cnt)

    # print('es-AR ' + str(date))
    activity_cnt = user_activity_esAR.isin(range).any(axis='columns').sum()
    dau_df.loc[date, 'es-AR'] = int(activity_cnt)

    # print('es-MX ' + str(date))
    activity_cnt = user_activity_esMX.isin(range).any(axis='columns').sum()
    dau_df.loc[date, 'es-MX'] = int(activity_cnt)

    # print('pt-BR ' + str(date))
    activity_cnt = user_activity_ptBR.isin(range).any(axis='columns').sum()
    dau_df.loc[date, 'pt-BR'] = int(activity_cnt)

dau_df = dau_df.reset_index()
dau_df.iloc[:, :].to_csv('dau-all-locales.csv', index=False, sep='\t')


