import pandas as pd

print('user-activity-data-preparing-2 has started...')

user_activity = pd.read_csv('user-activity.csv', delim_whitespace=True,
                            parse_dates=True, infer_datetime_format=True, usecols=range(0, 250),  # nrows=1000,
                            ).set_index(['userid']).drop(['churn', 'locale'], axis=1)
user_locale = pd.read_csv('user-data.csv', delim_whitespace=True).set_index(['userid']).drop(['churn', '0'], axis=1)

user_activity = user_activity.astype('datetime64')

submissionCntWeeks = pd.DataFrame()
for i in range(1, 30):
    start_sr = pd.to_datetime(user_activity.iloc[:, 0]) + pd.Timedelta((i-1)*7, unit='D')
    end_sr = pd.to_datetime(user_activity.iloc[:, 0]) + pd.Timedelta(i*7, unit='D')

    ch_df1 = user_activity.loc[:].ge(start_sr, axis=0)
    ch_df2 = user_activity.loc[:].lt(end_sr, axis=0)

    ch_df = ch_df1 & ch_df2
    ch_sr = ch_df.sum(axis=1).rename(i)
    submissionCntWeeks = pd.concat([submissionCntWeeks, ch_sr], axis=1, sort=False)
submissionCntWeeks = user_locale.merge(submissionCntWeeks, left_index=True, right_index=True)
submissionCntWeeks.iloc[:, :].to_csv('submission-cnt-weeks.csv', index=True, sep='\t')

submissionCntMonths = pd.DataFrame()
for i in range(1, 12):
    start_sr = pd.to_datetime(user_activity.iloc[:, 0]) + pd.Timedelta((i-1)*28, unit='D')
    end_sr = pd.to_datetime(user_activity.iloc[:, 0]) + pd.Timedelta(i*28, unit='D')

    ch_df1 = user_activity.loc[:].ge(start_sr, axis=0)
    ch_df2 = user_activity.loc[:].lt(end_sr, axis=0)

    ch_df = ch_df1 & ch_df2
    ch_sr = ch_df.sum(axis=1).rename(i)
    submissionCntMonths = pd.concat([submissionCntMonths, ch_sr], axis=1, sort=False)
submissionCntMonths = user_locale.merge(submissionCntMonths, left_index=True, right_index=True)
submissionCntMonths.iloc[:, :].to_csv('submission-cnt-months.csv', index=True, sep='\t')

submissionCntDays = pd.DataFrame()
for i in range(1, 31):
    start_sr = pd.to_datetime(user_activity.iloc[:, 0]) + pd.Timedelta((i-1)*1, unit='D')
    end_sr = pd.to_datetime(user_activity.iloc[:, 0]) + pd.Timedelta(i*1, unit='D')

    ch_df1 = user_activity.loc[:].ge(start_sr, axis=0)
    ch_df2 = user_activity.loc[:].lt(end_sr, axis=0)

    ch_df = ch_df1 & ch_df2
    ch_sr = ch_df.sum(axis=1).rename(i)
    submissionCntDays = pd.concat([submissionCntDays, ch_sr], axis=1, sort=False)
submissionCntDays = user_locale.merge(submissionCntDays, left_index=True, right_index=True)
submissionCntDays.iloc[:, :].to_csv('submission-cnt-days.csv', index=True, sep='\t')

print('user-activity-data-preparing-2 has finished!')
