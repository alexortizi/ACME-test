from datetime import datetime
hourlyPayments = [25, 15, 20]
workSchedules = [
    "00:01-09:00",
    "09:01-18:00",
    "18:01-23:59"
]
aditionalPaymentWeekend = 5


def getTime(time):
    times = time.split("-")
    entryTime, departureTime = datetime.strptime(
        times[0], '%H:%M').time(), datetime.strptime(times[1], '%H:%M').time()
    return (entryTime, departureTime)


def readFile(filePath):
    file = open(filePath).readlines()
    return [employee.strip().replace(" ", "").split('=') for employee in file]


def getPayHours(times, hours, paymentDict):
    entryTime, departureTime = getTime(times)
    hoursWorked = departureTime.hour-entryTime.hour
    for i in range(len(hours)):
        if entryTime >= hours[i][0] and departureTime <= hours[i][1]:
            hourlyRate = float(paymentDict[workSchedules[i]])
            return (hoursWorked, hourlyRate)
    return None


def getSalary(filePath):
    hours = [getTime(x) for x in workSchedules]
    for data in readFile(filePath):
        name = data[0]
        dataEmployee = data[1].split(",")
        paymentDict = dict(zip(workSchedules, hourlyPayments))
        salary = 0
        for data in dataEmployee:
            hoursWorked, hourlyRate = getPayHours(
                data[2::], hours, paymentDict)
            salary += (hourlyRate + aditionalPaymentWeekend) * \
                hoursWorked if data[0:2] in [
                    "SA", "SU"] else hourlyRate*hoursWorked
        print("The amount to pay {0} is: {1} USD".format(
            name, salary))


if __name__ == '__main__':
    getSalary('employeeWorkingHours.txt')
