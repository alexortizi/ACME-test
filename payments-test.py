import unittest
import datetime
import payments


class TestCases(unittest.TestCase):
    def testGetTime(self):
        self.assertEqual(payments.getTime("10:00-12:00"),
                         (datetime.datetime.strptime("10:00", '%H:%M').time(),
                          datetime.datetime.strptime("12:00", '%H:%M').time()))

    def testPayHours(self):
        times = "20:00-22:00"
        hours = [(datetime.time(0, 1), datetime.time(9, 0)), (datetime.time(
            9, 1), datetime.time(18, 0)), (datetime.time(18, 1), datetime.time(23, 59))]
        paymentDict = {
            "00:01-09:00": 25,
            "09:01-18:00": 15,
            "18:01-23:59": 20
        }
        self.assertEqual(payments.getPayHours(times, hours, paymentDict),(2, 20.0))


if __name__ == '__main__':
    unittest.main()
