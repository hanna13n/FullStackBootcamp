import sys
import psycopg2
import csv


def insert(fname):
    dbconn = psycopg2.connect("dbname=people")
    c = dbconn.cursor()
    f = open(fname)
    reader = csv.reader(f)
    for Country, Age, Salary, Purchased in reader:
        c.execute("insert into data (country,age,salary,purchased) values (%s, %s, %s, %s)",
                  (Country, Age, Salary, Purchased))
    dbconn.commit()


def main():
    fname = sys.argv[1]
    insert(fname)


main()
