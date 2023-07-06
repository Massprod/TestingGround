
# Table: Activity
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | user_id       | int     |
# | session_id    | int     |
# | activity_date | date    |
# | activity_type | enum    |
# +---------------+---------+
# There is no primary key for this table, it may have duplicate rows.
# The activity_type column is an ENUM of type ('open_session', 'end_session', 'scroll_down', 'send_message').
# The table shows the user activities for a social media website.
# Note that each session belongs to exactly one user.
# --------------------------
# Write an SQL query to find the daily active user count for a period of 30 days ending 2019-07-27 inclusively.
# A user was active on someday if they made at least one activity on that day.
# Return the result table in any order.

# SQL schema:
# DROP TYPE activity_enum;
# CREATE TYPE activity_enum AS ENUM('open_session', 'end_session', 'scroll_down', 'send_message';
# DROP TABLE IF EXISTS activity;
# Create table If Not Exists Activity (user_id int, session_id int, activity_date date, activity_type activity_enum);
# insert into Activity (user_id, session_id, activity_date, activity_type)
# values
# ('1', '1', '2019-07-20', 'open_session'),
# ('1', '1', '2019-07-20', 'scroll_down'),
# ('1', '1', '2019-07-20', 'end_session'),
# ('2', '4', '2019-07-20', 'open_session'),
# ('2', '4', '2019-07-21', 'send_message'),
# ('2', '4', '2019-07-21', 'end_session'),
# ('3', '2', '2019-07-21', 'open_session'),
# ('3', '2', '2019-07-21', 'send_message'),
# ('3', '2', '2019-07-21', 'end_session'),
# ('4', '3', '2019-06-25', 'open_session'),
# ('4', '3', '2019-06-25', 'end_session');

# PostgreSQL query:
# SELECT activity_date AS "day", COUNT(DISTINCT user_id) AS "active_users"
# FROM activity
# GROUP BY activity_date
# HAVING activity_date
# BETWEEN
# (DATE '2019-07-27' - INTERVAL '29 day')
# AND
# '2019-07-27';

# MySQL query;
# SELECT activity_date AS "day", COUNT(DISTINCT user_id) AS "active_users"
# FROM activity
# GROUP BY activity_date
# HAVING activity_date
# BETWEEN
# DATE_SUB('2019-07-27', INTERVAL 29 day)
# AND
# '2019-07-27';

# Failed commit, because didn't understand correctly DAY_LIMITS it's actually 29 days AND +1 day at 2019-07-27.
# Guess thing with double_quotes is about GROUP BY, inside it we can't name columns with single_quotes.
