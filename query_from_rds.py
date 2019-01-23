#!/usr/bin/python
import mysql.connector #import module named :pip install mysql-connector

def lambda_handler(event,context):

	mydb = mysql.connector.connect(
  	host="dbinstance.cziqlfxu6jua.us-east-1.rds.amazonaws.com",
  	user="master",
  	passwd="mastermaster",
  	database="mydatabase"
	)
	cursor = mydb.cursor()
	query = ("SELECT * FROM person")
	cursor.execute(query)
	print cursor.fetchall()
	return {
        'statusCode': 200,
        'body': json.dumps(cursor.fetchall())
    	}


	print(mydb)

