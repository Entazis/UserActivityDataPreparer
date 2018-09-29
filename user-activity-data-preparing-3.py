import pandas as pd


user_activity = pd.read_csv('user-activity.csv', delim_whitespace=True,
                            parse_dates=True, infer_datetime_format=True, usecols=range(0, 250),  # nrows=1000,
                            ).set_index(['userid']).drop(['churn', 'locale'], axis=1)
user_locale = pd.read_csv('user-data.csv', delim_whitespace=True).set_index(['userid']).drop(['churn', '0'], axis=1)

user_activity = user_activity.astype('datetime64')
user_activity_all = user_locale.merge(user_activity, left_index=True, right_index=True)
print(user_activity.columns)
print(user_activity.head())

wA_df = pd.DataFrame()
for i in range(1, 121):
    start_sr = pd.to_datetime(user_activity.iloc[:, 0]) + pd.Timedelta(i-7, unit='D')
    end_sr = pd.to_datetime(user_activity.iloc[:, 0]) + pd.Timedelta(i, unit='D')

    ch_df1 = user_activity.loc[:].ge(start_sr, axis=0)
    ch_df2 = user_activity.loc[:].lt(end_sr, axis=0)

    #wA
    ch_df = ch_df1 & ch_df2
    ch_df = ch_df.any(axis=1).rename(i)

    wA_df = pd.concat([wA_df, ch_df], axis=1, sort=False)
lifeycle_week = wA_df.sum(axis=0).rename('weekly active (all)')

mA_df = pd.DataFrame()
for i in range(1, 121):
    start_sr = pd.to_datetime(user_activity.iloc[:, 0]) + pd.Timedelta(i-28, unit='D')
    end_sr = pd.to_datetime(user_activity.iloc[:, 0]) + pd.Timedelta(i, unit='D')

    ch_df1 = user_activity.loc[:].ge(start_sr, axis=0)
    ch_df2 = user_activity.loc[:].lt(end_sr, axis=0)

    #wA
    ch_df = ch_df1 & ch_df2
    ch_df = ch_df.any(axis=1).rename(i)

    mA_df = pd.concat([mA_df, ch_df], axis=1, sort=False)
lifeycle_month = mA_df.sum(axis=0).rename('monthly active (all)')

...

user_activity_huHU = user_activity_all.loc[user_activity_all['locale'] == 'hu-HU', :].drop(['locale'], axis=1)

wA_df = pd.DataFrame()
for i in range(1, 121):
    start_sr = pd.to_datetime(user_activity_huHU.iloc[:, 0]) + pd.Timedelta(i-7, unit='D')
    end_sr = pd.to_datetime(user_activity_huHU.iloc[:, 0]) + pd.Timedelta(i, unit='D')

    ch_df1 = user_activity_huHU.loc[:].ge(start_sr, axis=0)
    ch_df2 = user_activity_huHU.loc[:].lt(end_sr, axis=0)

    #wA
    ch_df = ch_df1 & ch_df2
    ch_df = ch_df.any(axis=1).rename(i)

    wA_df = pd.concat([wA_df, ch_df], axis=1, sort=False)
lifeycle_week_huHU = wA_df.sum(axis=0)

mA_df = pd.DataFrame()
for i in range(1, 121):
    start_sr = pd.to_datetime(user_activity_huHU.iloc[:, 0]) + pd.Timedelta(i-28, unit='D')
    end_sr = pd.to_datetime(user_activity_huHU.iloc[:, 0]) + pd.Timedelta(i, unit='D')

    ch_df1 = user_activity_huHU.loc[:].ge(start_sr, axis=0)
    ch_df2 = user_activity_huHU.loc[:].lt(end_sr, axis=0)

    #wA
    ch_df = ch_df1 & ch_df2
    ch_df = ch_df.any(axis=1).rename(i)

    mA_df = pd.concat([mA_df, ch_df], axis=1, sort=False)
lifeycle_month_huHU = mA_df.sum(axis=0)

...

user_activity_plPL = user_activity_all.loc[user_activity_all['locale'] == 'pl-PL', :].drop(['locale'], axis=1)

wA_df = pd.DataFrame()
for i in range(1, 121):
    start_sr = pd.to_datetime(user_activity_plPL.iloc[:, 0]) + pd.Timedelta(i-7, unit='D')
    end_sr = pd.to_datetime(user_activity_plPL.iloc[:, 0]) + pd.Timedelta(i, unit='D')

    ch_df1 = user_activity_plPL.loc[:].ge(start_sr, axis=0)
    ch_df2 = user_activity_plPL.loc[:].lt(end_sr, axis=0)

    #wA
    ch_df = ch_df1 & ch_df2
    ch_df = ch_df.any(axis=1).rename(i)

    wA_df = pd.concat([wA_df, ch_df], axis=1, sort=False)
lifeycle_week_plPL = wA_df.sum(axis=0)

mA_df = pd.DataFrame()
for i in range(1, 121):
    start_sr = pd.to_datetime(user_activity_plPL.iloc[:, 0]) + pd.Timedelta(i-28, unit='D')
    end_sr = pd.to_datetime(user_activity_plPL.iloc[:, 0]) + pd.Timedelta(i, unit='D')

    ch_df1 = user_activity_plPL.loc[:].ge(start_sr, axis=0)
    ch_df2 = user_activity_plPL.loc[:].lt(end_sr, axis=0)

    #wA
    ch_df = ch_df1 & ch_df2
    ch_df = ch_df.any(axis=1).rename(i)

    mA_df = pd.concat([mA_df, ch_df], axis=1, sort=False)
lifeycle_month_plPL = mA_df.sum(axis=0)

...

user_activity_roRO = user_activity_all.loc[user_activity_all['locale'] == 'ro-RO', :].drop(['locale'], axis=1)

wA_df = pd.DataFrame()
for i in range(1, 121):
    start_sr = pd.to_datetime(user_activity_roRO.iloc[:, 0]) + pd.Timedelta(i-7, unit='D')
    end_sr = pd.to_datetime(user_activity_roRO.iloc[:, 0]) + pd.Timedelta(i, unit='D')

    ch_df1 = user_activity_roRO.loc[:].ge(start_sr, axis=0)
    ch_df2 = user_activity_roRO.loc[:].lt(end_sr, axis=0)

    #wA
    ch_df = ch_df1 & ch_df2
    ch_df = ch_df.any(axis=1).rename(i)

    wA_df = pd.concat([wA_df, ch_df], axis=1, sort=False)
lifeycle_week_roRO = wA_df.sum(axis=0)

mA_df = pd.DataFrame()
for i in range(1, 121):
    start_sr = pd.to_datetime(user_activity_roRO.iloc[:, 0]) + pd.Timedelta(i-28, unit='D')
    end_sr = pd.to_datetime(user_activity_roRO.iloc[:, 0]) + pd.Timedelta(i, unit='D')

    ch_df1 = user_activity_roRO.loc[:].ge(start_sr, axis=0)
    ch_df2 = user_activity_roRO.loc[:].lt(end_sr, axis=0)

    #wA
    ch_df = ch_df1 & ch_df2
    ch_df = ch_df.any(axis=1).rename(i)

    mA_df = pd.concat([mA_df, ch_df], axis=1, sort=False)
lifeycle_month_roRO = mA_df.sum(axis=0)

...

user_activity_trTR = user_activity_all.loc[user_activity_all['locale'] == 'tr-TR', :].drop(['locale'], axis=1)

wA_df = pd.DataFrame()
for i in range(1, 121):
    start_sr = pd.to_datetime(user_activity_trTR.iloc[:, 0]) + pd.Timedelta(i-7, unit='D')
    end_sr = pd.to_datetime(user_activity_trTR.iloc[:, 0]) + pd.Timedelta(i, unit='D')

    ch_df1 = user_activity_trTR.loc[:].ge(start_sr, axis=0)
    ch_df2 = user_activity_trTR.loc[:].lt(end_sr, axis=0)

    #wA
    ch_df = ch_df1 & ch_df2
    ch_df = ch_df.any(axis=1).rename(i)

    wA_df = pd.concat([wA_df, ch_df], axis=1, sort=False)
lifeycle_week_trTR = wA_df.sum(axis=0)

mA_df = pd.DataFrame()
for i in range(1, 121):
    start_sr = pd.to_datetime(user_activity_trTR.iloc[:, 0]) + pd.Timedelta(i-28, unit='D')
    end_sr = pd.to_datetime(user_activity_trTR.iloc[:, 0]) + pd.Timedelta(i, unit='D')

    ch_df1 = user_activity_trTR.loc[:].ge(start_sr, axis=0)
    ch_df2 = user_activity_trTR.loc[:].lt(end_sr, axis=0)

    #wA
    ch_df = ch_df1 & ch_df2
    ch_df = ch_df.any(axis=1).rename(i)

    mA_df = pd.concat([mA_df, ch_df], axis=1, sort=False)
lifeycle_month_trTR = mA_df.sum(axis=0)

...

user_activity_hiIN = user_activity_all.loc[user_activity_all['locale'] == 'hi-IN', :].drop(['locale'], axis=1)

wA_df = pd.DataFrame()
for i in range(1, 121):
    start_sr = pd.to_datetime(user_activity_hiIN.iloc[:, 0]) + pd.Timedelta(i-7, unit='D')
    end_sr = pd.to_datetime(user_activity_hiIN.iloc[:, 0]) + pd.Timedelta(i, unit='D')

    ch_df1 = user_activity_hiIN.loc[:].ge(start_sr, axis=0)
    ch_df2 = user_activity_hiIN.loc[:].lt(end_sr, axis=0)

    #wA
    ch_df = ch_df1 & ch_df2
    ch_df = ch_df.any(axis=1).rename(i)

    wA_df = pd.concat([wA_df, ch_df], axis=1, sort=False)
lifeycle_week_hiIN = wA_df.sum(axis=0)

mA_df = pd.DataFrame()
for i in range(1, 121):
    start_sr = pd.to_datetime(user_activity_hiIN.iloc[:, 0]) + pd.Timedelta(i-28, unit='D')
    end_sr = pd.to_datetime(user_activity_hiIN.iloc[:, 0]) + pd.Timedelta(i, unit='D')

    ch_df1 = user_activity_hiIN.loc[:].ge(start_sr, axis=0)
    ch_df2 = user_activity_hiIN.loc[:].lt(end_sr, axis=0)

    #wA
    ch_df = ch_df1 & ch_df2
    ch_df = ch_df.any(axis=1).rename(i)

    mA_df = pd.concat([mA_df, ch_df], axis=1, sort=False)
lifeycle_month_hiIN = mA_df.sum(axis=0)

...

user_activity_idID = user_activity_all.loc[user_activity_all['locale'] == 'id-ID', :].drop(['locale'], axis=1)

wA_df = pd.DataFrame()
for i in range(1, 121):
    start_sr = pd.to_datetime(user_activity_idID.iloc[:, 0]) + pd.Timedelta(i-7, unit='D')
    end_sr = pd.to_datetime(user_activity_idID.iloc[:, 0]) + pd.Timedelta(i, unit='D')

    ch_df1 = user_activity_idID.loc[:].ge(start_sr, axis=0)
    ch_df2 = user_activity_idID.loc[:].lt(end_sr, axis=0)

    #wA
    ch_df = ch_df1 & ch_df2
    ch_df = ch_df.any(axis=1).rename(i)

    wA_df = pd.concat([wA_df, ch_df], axis=1, sort=False)
lifeycle_week_idID = wA_df.sum(axis=0)

mA_df = pd.DataFrame()
for i in range(1, 121):
    start_sr = pd.to_datetime(user_activity_idID.iloc[:, 0]) + pd.Timedelta(i-28, unit='D')
    end_sr = pd.to_datetime(user_activity_idID.iloc[:, 0]) + pd.Timedelta(i, unit='D')

    ch_df1 = user_activity_idID.loc[:].ge(start_sr, axis=0)
    ch_df2 = user_activity_idID.loc[:].lt(end_sr, axis=0)

    #wA
    ch_df = ch_df1 & ch_df2
    ch_df = ch_df.any(axis=1).rename(i)

    mA_df = pd.concat([mA_df, ch_df], axis=1, sort=False)
lifeycle_month_idID = mA_df.sum(axis=0)

...

user_activity_viVN = user_activity_all.loc[user_activity_all['locale'] == 'vi-VN', :].drop(['locale'], axis=1)

wA_df = pd.DataFrame()
for i in range(1, 121):
    start_sr = pd.to_datetime(user_activity_viVN.iloc[:, 0]) + pd.Timedelta(i-7, unit='D')
    end_sr = pd.to_datetime(user_activity_viVN.iloc[:, 0]) + pd.Timedelta(i, unit='D')

    ch_df1 = user_activity_viVN.loc[:].ge(start_sr, axis=0)
    ch_df2 = user_activity_viVN.loc[:].lt(end_sr, axis=0)

    #wA
    ch_df = ch_df1 & ch_df2
    ch_df = ch_df.any(axis=1).rename(i)

    wA_df = pd.concat([wA_df, ch_df], axis=1, sort=False)
lifeycle_week_viVN = wA_df.sum(axis=0)

mA_df = pd.DataFrame()
for i in range(1, 121):
    start_sr = pd.to_datetime(user_activity_viVN.iloc[:, 0]) + pd.Timedelta(i-28, unit='D')
    end_sr = pd.to_datetime(user_activity_viVN.iloc[:, 0]) + pd.Timedelta(i, unit='D')

    ch_df1 = user_activity_viVN.loc[:].ge(start_sr, axis=0)
    ch_df2 = user_activity_viVN.loc[:].lt(end_sr, axis=0)

    #wA
    ch_df = ch_df1 & ch_df2
    ch_df = ch_df.any(axis=1).rename(i)

    mA_df = pd.concat([mA_df, ch_df], axis=1, sort=False)
lifeycle_month_viVN = mA_df.sum(axis=0)

...

user_activity_enNG = user_activity_all.loc[user_activity_all['locale'] == 'en-NG', :].drop(['locale'], axis=1)

wA_df = pd.DataFrame()
for i in range(1, 121):
    start_sr = pd.to_datetime(user_activity_enNG.iloc[:, 0]) + pd.Timedelta(i-7, unit='D')
    end_sr = pd.to_datetime(user_activity_enNG.iloc[:, 0]) + pd.Timedelta(i, unit='D')

    ch_df1 = user_activity_enNG.loc[:].ge(start_sr, axis=0)
    ch_df2 = user_activity_enNG.loc[:].lt(end_sr, axis=0)

    #wA
    ch_df = ch_df1 & ch_df2
    ch_df = ch_df.any(axis=1).rename(i)

    wA_df = pd.concat([wA_df, ch_df], axis=1, sort=False)
lifeycle_week_enNG = wA_df.sum(axis=0)

mA_df = pd.DataFrame()
for i in range(1, 121):
    start_sr = pd.to_datetime(user_activity_enNG.iloc[:, 0]) + pd.Timedelta(i-28, unit='D')
    end_sr = pd.to_datetime(user_activity_enNG.iloc[:, 0]) + pd.Timedelta(i, unit='D')

    ch_df1 = user_activity_enNG.loc[:].ge(start_sr, axis=0)
    ch_df2 = user_activity_enNG.loc[:].lt(end_sr, axis=0)

    #wA
    ch_df = ch_df1 & ch_df2
    ch_df = ch_df.any(axis=1).rename(i)

    mA_df = pd.concat([mA_df, ch_df], axis=1, sort=False)
lifeycle_month_enNG = mA_df.sum(axis=0)

...

user_activity_esAR = user_activity_all.loc[user_activity_all['locale'] == 'es-AR', :].drop(['locale'], axis=1)

wA_df = pd.DataFrame()
for i in range(1, 121):
    start_sr = pd.to_datetime(user_activity_esAR.iloc[:, 0]) + pd.Timedelta(i-7, unit='D')
    end_sr = pd.to_datetime(user_activity_esAR.iloc[:, 0]) + pd.Timedelta(i, unit='D')

    ch_df1 = user_activity_esAR.loc[:].ge(start_sr, axis=0)
    ch_df2 = user_activity_esAR.loc[:].lt(end_sr, axis=0)

    #wA
    ch_df = ch_df1 & ch_df2
    ch_df = ch_df.any(axis=1).rename(i)

    wA_df = pd.concat([wA_df, ch_df], axis=1, sort=False)
lifeycle_week_esAR = wA_df.sum(axis=0)

mA_df = pd.DataFrame()
for i in range(1, 121):
    start_sr = pd.to_datetime(user_activity_esAR.iloc[:, 0]) + pd.Timedelta(i-28, unit='D')
    end_sr = pd.to_datetime(user_activity_esAR.iloc[:, 0]) + pd.Timedelta(i, unit='D')

    ch_df1 = user_activity_esAR.loc[:].ge(start_sr, axis=0)
    ch_df2 = user_activity_esAR.loc[:].lt(end_sr, axis=0)

    #wA
    ch_df = ch_df1 & ch_df2
    ch_df = ch_df.any(axis=1).rename(i)

    mA_df = pd.concat([mA_df, ch_df], axis=1, sort=False)
lifeycle_month_esAR = mA_df.sum(axis=0)

...

user_activity_esMX = user_activity_all.loc[user_activity_all['locale'] == 'es-MX', :].drop(['locale'], axis=1)

wA_df = pd.DataFrame()
for i in range(1, 121):
    start_sr = pd.to_datetime(user_activity_esMX.iloc[:, 0]) + pd.Timedelta(i-7, unit='D')
    end_sr = pd.to_datetime(user_activity_esMX.iloc[:, 0]) + pd.Timedelta(i, unit='D')

    ch_df1 = user_activity_esMX.loc[:].ge(start_sr, axis=0)
    ch_df2 = user_activity_esMX.loc[:].lt(end_sr, axis=0)

    #wA
    ch_df = ch_df1 & ch_df2
    ch_df = ch_df.any(axis=1).rename(i)

    wA_df = pd.concat([wA_df, ch_df], axis=1, sort=False)
lifeycle_week_esMX = wA_df.sum(axis=0)

mA_df = pd.DataFrame()
for i in range(1, 121):
    start_sr = pd.to_datetime(user_activity_esMX.iloc[:, 0]) + pd.Timedelta(i-28, unit='D')
    end_sr = pd.to_datetime(user_activity_esMX.iloc[:, 0]) + pd.Timedelta(i, unit='D')

    ch_df1 = user_activity_esMX.loc[:].ge(start_sr, axis=0)
    ch_df2 = user_activity_esMX.loc[:].lt(end_sr, axis=0)

    #wA
    ch_df = ch_df1 & ch_df2
    ch_df = ch_df.any(axis=1).rename(i)

    mA_df = pd.concat([mA_df, ch_df], axis=1, sort=False)
lifeycle_month_esMX = mA_df.sum(axis=0)

...

user_activity_ptBR = user_activity_all.loc[user_activity_all['locale'] == 'pt-BR', :].drop(['locale'], axis=1)

wA_df = pd.DataFrame()
for i in range(1, 121):
    start_sr = pd.to_datetime(user_activity_ptBR.iloc[:, 0]) + pd.Timedelta(i-7, unit='D')
    end_sr = pd.to_datetime(user_activity_ptBR.iloc[:, 0]) + pd.Timedelta(i, unit='D')

    ch_df1 = user_activity_ptBR.loc[:].ge(start_sr, axis=0)
    ch_df2 = user_activity_ptBR.loc[:].lt(end_sr, axis=0)

    #wA
    ch_df = ch_df1 & ch_df2
    ch_df = ch_df.any(axis=1).rename(i)

    wA_df = pd.concat([wA_df, ch_df], axis=1, sort=False)
lifeycle_week_ptBR = wA_df.sum(axis=0)

mA_df = pd.DataFrame()
for i in range(1, 121):
    start_sr = pd.to_datetime(user_activity_ptBR.iloc[:, 0]) + pd.Timedelta(i-28, unit='D')
    end_sr = pd.to_datetime(user_activity_ptBR.iloc[:, 0]) + pd.Timedelta(i, unit='D')

    ch_df1 = user_activity_ptBR.loc[:].ge(start_sr, axis=0)
    ch_df2 = user_activity_ptBR.loc[:].lt(end_sr, axis=0)

    #wA
    ch_df = ch_df1 & ch_df2
    ch_df = ch_df.any(axis=1).rename(i)

    mA_df = pd.concat([mA_df, ch_df], axis=1, sort=False)
lifeycle_month_ptBR = mA_df.sum(axis=0)

...

lifecycle_retention = pd.concat((lifeycle_week.rename('weekly (all)'), lifeycle_month.rename('monthly (all)'),
           lifeycle_week_huHU.rename('weekly (hu-HU)'), lifeycle_month_huHU.rename('monthly (hu-HU)'),
           lifeycle_week_plPL.rename('weekly (pl-PL)'), lifeycle_month_plPL.rename('monthly (pl-PL)'),
           lifeycle_week_roRO.rename('weekly (ro-RO)'), lifeycle_month_roRO.rename('monthly (ro-RO)'),
           lifeycle_week_trTR.rename('weekly (tr-TR)'), lifeycle_month_trTR.rename('monthly (tr-TR)'),
           lifeycle_week_hiIN.rename('weekly (hi-IN)'), lifeycle_month_hiIN.rename('monthly (hi-IN)'),
           lifeycle_week_idID.rename('weekly (id-ID)'), lifeycle_month_idID.rename('monthly (id-ID)'),
           lifeycle_week_viVN.rename('weekly (vi-VN)'), lifeycle_month_viVN.rename('monthly (vi-VN)'),
           lifeycle_week_enNG.rename('weekly (en-NG)'), lifeycle_month_enNG.rename('monthly (en-NG)'),
           lifeycle_week_esAR.rename('weekly (es-AR)'), lifeycle_month_esAR.rename('monthly (es-AR)'),
           lifeycle_week_esMX.rename('weekly (es-MX)'), lifeycle_month_esMX.rename('monthly (es-MX)'),
           lifeycle_week_ptBR.rename('weekly (pt-BR)'), lifeycle_month_ptBR.rename('monthly (pt-BR)')), axis=1)

lifecycle_retention.iloc[:, :].to_csv('lifecycle-retention.csv', index=True, sep='\t')
...
