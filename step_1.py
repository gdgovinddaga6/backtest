import pyodbc
import datetime
from datetime import time
import pandas as pd

# ip_date = input('Enter a date in DD-MM-YYYY format \n')
# day, month, year = map(int, ip_date.split('-'))
# ip_date = datetime.date(year, month, day)
# ip_start_time = input("Enter a START time in the format HH:MM \n")
# h, m = map(int, ip_start_time.split(':'))
# ip_start_time = time(hour=h, minute=m)
# ip_end_time = input("Enter a END time in the format HH:MM \n")
# h, m = map(int, ip_start_time.split(':'))
# ip_start_time = time(hour=h, minute=m)
# dvalue_code1 = float(input("Dvalue for Code1"))
# dvalue_code2 = float(input("Dvalue for Code2"))
# dvalue_code3 = float(input("Dvalue for Code3"))
# dvalue_code4 = float(input("Dvalue for Code4"))
# dvalue_code5 = float(input("Dvalue for Code5"))
# dvalue_code6 = float(input("Dvalue for Code6"))

ip_date = "04-01-2022"
day, month, year = map(int, ip_date.split('-'))
ip_date = datetime.date(year, month, day)
print(ip_date)
ip_start_time = "08:32:00"
h, m, s = map(int, ip_start_time.split(':'))
ip_start_time = time(hour=h, minute=m, second=s)
ip_end_time = "11:04:00"
h, m, s = map(int, ip_end_time.split(':'))
ip_end_time = time(hour=h, minute=m, second=s)
dvalue_code1 = 0.92
print(dvalue_code1)
dvalue_code2 = 0.97
dvalue_code3 = 1
dvalue_code4 = 0.89
dvalue_code5 = 0.8
dvalue_code6 = 0.95
print(ip_start_time)
print(ip_end_time)
connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=GOVIND\MSSQLSERVER01;DATABASE=backtest;Trusted_Connection=yes;')
query = """select * from dbo.Day2 where Time between '8:30:00' and '9:32:00';"""
df = pd.read_sql(query, connection)
print(df.head())
print("done")


