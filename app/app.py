import psycopg2
import csv
import time
import psycopg2.extras


class DataIngestion():


	def create_connection(self):
		db_name = 'database'
		db_user = 'username'
		db_pass = 'secret'
		db_host = 'db'
		db_port = '5432'
		conn = psycopg2.connect(database=db_name, user=db_user, password=db_pass, host=db_host, port= db_port)
		cur = conn.cursor()
		return conn, cur


	def insert_data(self):
		try:
			PATH = 'products.csv'
			count  = 0
			inner_count = 0
			list_row = []

			conn, cur = self.create_connection()

			start_time = time.time()
			with open(PATH, "r") as fr:
				csv_reader = csv.reader(fr)

				next(csv_reader)
				for line in csv_reader:
					try:
						# print(cells)
						name = line[0]
						sku = line[1]
						description = line[2].replace('\n','')
						row = (sku, name , description)
						list_row.append(row)

						#WHEN IT REACHES END OF DATA
						if name == '':
							break

						query = "insert into postman (sku, name , description) values (%s,%s,%s)"
						count +=1
						if count == 5000:
							# print(list_row)
							print(count)
							inner_count +=1
							psycopg2.extras.execute_batch(cur,query, list_row)
							conn.commit()
							
							list_row = []
							count = 0
							print('ROW INSERTED--------------------')
					except Exception as e:
						print('hallelueigh', e)
						break
			cur.close()
			print('DONE')
			end_time = time.time()
			time_taken = end_time-start_time
			print(time_taken)
		except Exception as e:
			print(e,'error')

	def count_and_rows(self):
		try:
			count = 0
			conn, cur = self.create_connection()
			cur.execute("SELECT * FROM postman")

			rows = cur.fetchall()
			print("The number of rows: ", cur.rowcount)

			print('showing first 10 rows')
			for row in rows:
				print(row)
				count += 1
				if count == 10:
					break
			conn.commit()
			cur.close()
		except Exception as e:
			print(e,'count_and_rows ERROR')


	def create_agg_name(self):

		try:

			conn, cur = self.create_connection()
			cur.execute("""CREATE TABLE agg_name AS SELECT COUNT(DISTINCT name) AS distinct_name FROM postman""")

			print("An aggregated table on above rows with `name` and `no. of products` as the columns created")
			conn.commit()


			cur.execute("SELECT * FROM agg_name")

			rows = cur.fetchall()
			print("The number of rows in agg_name table : ", cur.rowcount)

			print('showing first 10 rows')
			for row in rows:
				print(row)
				count += 1
				if count == 10:
					break
			conn.commit()
			cur.close()
		except Exception as e:
			print('error in agg table')


if __name__ == '__main__':
	di_obj = DataIngestion()
	di_obj.insert_data()
	di_obj.count_and_rows()
	di_obj.create_agg_name()





