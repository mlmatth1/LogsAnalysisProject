Fullstack-nanodegree-vm
=============

Common code for the Relational Databases and Full Stack Fundamentals courses



### Running code

Copy the following files into the /vagrant directory within the 

FSND-Virtual-Machine:

* top_three_articles.py
* author_views.py
* top_error_date.py



To run do the following at git bash console:

python top_three_articles
python author_views.py
python top_error_date.py


### Views

There are the following 3 views:

create view view_top_three_articles AS  select articles.slug as article,
 count(log.path) as views from articles JOIN log on log.path LIKE CONCAT('%', a
rticles.slug, '%') group by articles.slug order by views desc limit 3;
create view view_author_views AS  select authors.name, count(log.path) f
rom authors join articles on articles.author = authors.id join log on log.path
LIKE CONCAT('%', articles.slug, '%') group by authors.name order by count desc;

create view view_top_error AS select cast(time as date) as date, (Count(
status) * 100 / (select count(*) from log where status LIKE '%4%')) as percent
from log where status LIKE '%4%' group by date order by percent desc limit 1;

## Authors

*Mark Matthews*
