# CodeBerry User-activity-data Preparing

The scripts create user activity data which can be used for visualization.

## Getting Started

Clone the project to your local computer.

### Prerequisites

You will need the raw data (getAllUserSubmissionsExport.csv). You can get it from here: (see "Get data from Mongo" section)
https://bitbucket.org/borzos6/codeberry-churn-calculator/src/master/

Copy getAllUserSubmissionsExport.csv to codeberry-user-activity-data-preparing folder

### Run the scripts

In this order:

```
python3.6 user-activity-data-preparing.py
python3.6 user-activity-data-preparing-2.py
python3.6 user-activity-data-preparing-3.py
python3.6 user-activity-data-preparing-4.py
```

And you will get the following files:
user-activity.csv, user-data.csv, submission-cnt-weeks.csv, submission-cnt-months.csv, submission-cnt-days.csv, lifecycle-retention.csv, mau-all-locales.csv, dau-all-locales.csv

**Upload them to the following spreadsheets:**

submission-cnt-days.csv, dau-all-locales.csv --> User activity - lifecycle-retention (days)

submission-cnt-weeks.csv, lifecycle-retention.csv --> User activity - lifecycle-retention (weeks)

submission-cnt-months.csv, lifecycle-retention.csv, mau-all-locales.csv --> User activity - lifecycle-retention (months)