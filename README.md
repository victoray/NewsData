# Date Created
Created on June 3, 2019.

# Project Title
Logs Analysis

# Description
Using Python and SQL to create an internal reporting tool to analyze user activities on the newspaper website and create an informative summary of user activity.

# Files Used
[newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

# Requirements
Python >= 3.6
Postgre v11
[psycopg2 v2.52](https://github.com/psycopg/psycopg2)

# Run
```
  $ psql -d news -f newsdata.sql
  $ python newsdb.py
 ```
