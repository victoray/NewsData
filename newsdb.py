import psycopg2

dbname = "news"

db = psycopg2.connect(database=dbname)

c = db.cursor()

print("What are the most popular three articles of all time?\n")
query = '''
SELECT a.title, COUNT(*) 
FROM authors 
JOIN articles a ON authors.id = a.author 
JOIN log ON log.path = ('/article/' || a.slug) 
GROUP BY 1 
ORDER BY 2 
DESC LIMIT 3
'''
c.execute(query)

result = [list(item) for item in c.fetchall()]
for item in result:
    print("{} - {} views".format(item[0], item[1]))

print("-" * 60)

query = '''
SELECT authors.name, COUNT(*) 
FROM authors 
JOIN articles a ON authors.id = a.author 
JOIN log ON log.path = ('/article/' || a.slug) 
GROUP BY 1 
ORDER BY 2 DESC
'''

c.execute(query)


print("\nWho are the most popular article authors of all time?\n")
result = [list(item) for item in c.fetchall()]
for item in result:
    print("{} - {} views".format(item[0], item[1]))

print("-" * 60)

print('\nOn which days did more than 1% of requests lead to errors?\n')

query = '''
WITH tb1 as (
    SELECT DATE_TRUNC('day', time) as day, COUNT(*)
    FROM log
    WHERE path != '/'
    GROUP BY 1
     ),

     tb2 as (
    SELECT DATE_TRUNC('day', time) as day, COUNT(*)
    FROM log
    WHERE status != '200 OK'
    GROUP BY 1
     )
SELECT tb1.day, tb2.count, tb1.count, ((tb2.count * 1./ tb1.count) * 100) as percentage
FROM tb1,tb2
WHERE tb1.day = tb2.day
GROUP BY 1, 2, 3
HAVING ((tb2.count * 1./ tb1.count) * 100) > 1
ORDER BY 2 DESC
'''

c.execute(query)
result = [list(item) for item in c.fetchall()]

for item in result:
    print("{} - {:.2f}% errors".format(item[0].strftime('%B %d, %Y'), float(item[3])))


db.close()
