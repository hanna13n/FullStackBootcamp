import csv
import psycopg2
import sys


def dump(fname):
    dbconn = psycopg2.connect("dbname=sample")
    c = dbconn.cursor()
    f = open(fname, "w")
    writer = csv.writer(f)

    c.execute("select * from dump")
    for id, name, gender in c.fetchall():
        writer.writerow([id, name, gender])
    dbconn.commit()
    f.close()


def main():
    fname = sys.argv[1]
    dump(fname)


main()
