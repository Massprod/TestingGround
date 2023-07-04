from sqlalchemy.sql import text
from sqlalchemy.orm import Session
from sqlalchemy.engine import Result
from tasks_database.db import get_session


# Table: Stadium
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | id            | int     |
# | visit_date    | date    |
# | people        | int     |
# +---------------+---------+
# visit_date is the primary key for this table.
# Each row of this table contains the visit date and visit id
#   to the stadium with the number of people during the visit.
# No two rows will have the same visit_date, and as the id increases, the dates increase as well.
# ----------------------------
# Write an SQL query to display the records with three or more rows with consecutive id's,
#   and the number of people is greater than or equal to 100 for each.
# Return the result table ordered by visit_date in ascending order.

# SQL schema:
# DROP TABLE IF EXISTS stadium;
# Create table If Not Exists Stadium (id int, visit_date DATE NULL, people int);
# insert into Stadium (id, visit_date, people) values ('1', '2017-01-01', '10');
# insert into Stadium (id, visit_date, people) values ('2', '2017-01-02', '109');
# insert into Stadium (id, visit_date, people) values ('3', '2017-01-03', '150');
# insert into Stadium (id, visit_date, people) values ('4', '2017-01-04', '99');
# insert into Stadium (id, visit_date, people) values ('5', '2017-01-05', '145');
# insert into Stadium (id, visit_date, people) values ('6', '2017-01-06', '1455');
# insert into Stadium (id, visit_date, people) values ('7', '2017-01-07', '199');
# insert into Stadium (id, visit_date, people) values ('8', '2017-01-09', '188');

