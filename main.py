from flask import Flask
from flask import request
from src.infrastructure.SQLiteConnector import create_connection, getASInformation_by_AS_number, \
    getASInformation_by_IPv4, getASInformation_by_IPv6

app = Flask(__name__)
database = "resources/db/data/autonomous_system_sample_data.db"


@app.route('/as-information', methods=['GET'])
def getASInformation():
    conn = create_connection(database)
    as_number = request.args.get('as_number')
    print(as_number)
    ipv4 = request.args.get('ipv4')
    print(ipv4)
    ipv6 = request.args.get('ipv6')
    print(ipv6)
    if as_number is not None:
        getASInformation_by_AS_number(conn, as_number)
    elif ipv4 is not None:
        getASInformation_by_IPv4(conn, ipv4)
    else:
        getASInformation_by_IPv6(conn, ipv6)


if __name__ == '__main__':
    print("Hello World!")
    app.run(port="8088", host="localhost", threaded=False, debug=True)
