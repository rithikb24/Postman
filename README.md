INstructuins how to run
1. Add the products.csv file in app folder and enure the csv name is 'products.csv'
2. docker-compose up --build (this will insert all rows in the database)

Alternatively - 
1. create a table on your local postgres server using the command in database/create_fixtures.sql
2. Set all the enviourment variables seen in line15-19 in app/app.py accordingly.
3. use the file app/app.py to populate the database


Things Done from points to achieve
1. Code follows concepts of OOPS
2. The file gets processed under a mintue 
4. all details ingested in one table 
5. An aggregated table on above rows with `name` and `no. of products` as the columns can be achieved from this command- """CREATE TABLE agg_name AS SELECT COUNT(DISTINCT name) AS distinct_name FROM postman"""



Things NOt Done from points to achieve
1. couldnt find the workaround for having sku as primary key without data loss as it had duplicate values


If given more time- 
- I would fine a way to make the ingestion as efficient as possible
- I would figure out a workaround the duplicate data in sku column and how to have it as primary keyy
