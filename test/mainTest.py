import unittest
from src.infrastructure.SQLiteConnector import create_connection, getASInformation_by_AS_number, \
    getASInformation_by_IPv4, getASInformation_by_IPv6


class ApplicationTests(unittest.TestCase):
    def test_connectivity(self):
        conn = create_connection("resources/db/data/autonomous_system_sample_data.db")
        self.assertIsNotNone(conn, "Connection failed.")

    def test_get_by_AS_Number(self):
        conn = create_connection("resources/db/data/autonomous_system_sample_data.db")
        self.assertIsNotNone(conn, "Connection failed.")
        getASInformation_by_AS_number(conn, "58519")

    def test_get_by_IPv4(self):
        conn = create_connection("resources/db/data/autonomous_system_sample_data.db")
        self.assertIsNotNone(conn, "Connection failed.")
        getASInformation_by_IPv4(conn, "223.255.254.0")

    def test_get_by_IPv6(self):
        conn = create_connection("resources/db/data/autonomous_system_sample_data.db")
        self.assertIsNotNone(conn, "Connection failed.")
        getASInformation_by_IPv6(conn, "::")


if __name__ == '__main__':
    unittest.main()
