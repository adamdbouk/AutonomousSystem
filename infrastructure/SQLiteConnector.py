import sqlite3
from sqlite3 import Error


def getASInformation_by_IPv4(conn, ipv4):

    cur = conn.cursor()
    cur.execute("SELECT AS_description "
                "FROM IPv4_to_ASN_table "
                "WHERE range_start=? OR range_end=?", (ipv4, ipv4,))

    rows = cur.fetchall()

    for row in rows:
        print(row)


def getASInformation_by_AS_number(conn, AS_number):

    cur = conn.cursor()
    cur.execute("SELECT AS_description "
                "FROM IPv4_to_ASN_table "
                "WHERE AS_number=? ", (AS_number,))

    rows = cur.fetchall()

    for row in rows:
        print(row)


def getASInformation_by_IPv6(conn, ipv6):

    cur = conn.cursor()
    cur.execute("SELECT AS_description "
                "FROM IPv6_to_ASN_table "
                "WHERE range_start=? OR range_end=?", (ipv6, ipv6, ))

    rows = cur.fetchall()

    for row in rows:
        print(row)


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    print(conn)
    return conn


class SQLiteConnector:
    pass
