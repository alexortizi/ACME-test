# ACME-test

The company ACME offers their employees the flexibility to work the hours they want. They will pay for the hours worked based on the day of the week and time of day, according to the following table:

Monday - Friday	Saturday and Sunday
00:01 - 09:00 25 USD	00:01 - 09:00 30 USD
09:01 - 18:00 15 USD	09:01 - 18:00 20 USD
18:01 - 00:00 20 USD	18:01 - 00:00 25 USD
The goal of this exercise is to calculate the total that the company has to pay an employee, based on the hours they worked and the times during which they worked. The following abbreviations will be used for entering data:

Monday	Tuesday	Wednesday	Thursday	Friday	Saturday	Sunday
MO	TU	WE	TH	FR	SA	SU
Input: the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our two examples below.

Output: indicate how much the employee has to be paid

For example:

Case	Case 1	Case 2
Input	RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00	ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
Output	The amount to pay RENE is: 215 USD	The amount to pay ASTRID is: 85 USD

# How did I do it?
I made from arrays and a dictionary with the schedule data and the hourly pay, from there I go through the file and take the in and out hours for the pay calculation, also I verify if it is a weekend to give the additional bonus of 5, everything is done with python own tools

# How to run the code?
In the project directory, python payments.py to run the proyect, the project uses the employeeWorkingHours.txt file to calculate the salaries, in case you want to add/edit new data you must edit the file.
For the test, run python payments-test.py
