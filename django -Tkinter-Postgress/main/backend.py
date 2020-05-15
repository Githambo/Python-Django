import sqlite3
import psycopg2

class Database:
	def __init__(self,db):		
		self.conn=psycopg2.connect(host="localhost",user="postgres",database="student",password="kenneth123")
		self.cur=self.conn.cursor()

	def insert(self,first_name,second_name,ref_number,course):
		self.cur.execute("INSERT INTO main_student (first_name,second_name,ref_number,course) VALUES (%s,%s,%s,%s)",(first_name,second_name,ref_number,course))
		self.conn.commit()

	def __del__(self):
		self.conn.close()