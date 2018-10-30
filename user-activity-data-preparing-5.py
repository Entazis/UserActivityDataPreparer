import pandas as pd


user_activity = pd.read_csv('user-activity.csv', delim_whitespace=True,
                            parse_dates=True, infer_datetime_format=True, # usecols=range(0, 250),  # nrows=1000,
                            ).set_index(['userid']).drop(['churn'], axis=1)

print(user_activity.columns)
print(user_activity.head())

submissions = user_activity.count(axis=1)

user_submission_count = user_activity.iloc[:, 0:2]
user_submission_count = user_submission_count.assign(submissions=pd.Series(user_activity.count(axis=1)-1).values)
user_submission_count = user_submission_count.reset_index()

user_submission_count.iloc[:, :].to_csv('user-submission-cnt.csv', index=False, sep='\t')

