import pandas as pd
import numpy as np


def f(x):
    if x.last_valid_index() is None:
        return np.nan
    else:
        return x[x.last_valid_index()]


data = pd.read_csv('getAllUserSubmissionsExport.csv', delim_whitespace=True, header=None,
                   names=['date', 'userid', 'locale', 'lessonid', 'zero']
                   ).sort_values(by='date', ascending=True).reset_index()
print(data.head())
print(data.shape)
data = data.loc[data['lessonid'] != 'quinin', :]
print(data.shape)

user_submissions = data.loc[:, ['userid', 'locale', 'date']].set_index(['userid', 'locale']).groupby(
    ['userid', 'locale'])['date'].apply(list).apply(pd.Series)

user_submissions['churn'] = user_submissions.apply(f, axis=1)
cols = user_submissions.columns.tolist()
cols = cols[-1:] + cols[:-1]
user_submissions = user_submissions[cols]
user_submissions = user_submissions.reset_index()

print(user_submissions.head())
print(user_submissions.columns)
print(user_submissions.shape)

user_submissions.iloc[:, :].to_csv('user-activity.csv', index=False, sep='\t')
user_submissions.iloc[:, 0:4].to_csv('user-data.csv', index=False, sep='\t')

...






