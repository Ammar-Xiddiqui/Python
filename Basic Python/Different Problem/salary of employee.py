'''
A company decided to give bonus of 5% to employee if his/her year of service is
more than 5 years.
Ask user for their salary and year of service and print the net bonus amount.
'''
salary=int(input('enter salary :'))
years_of_service=int(input('enter years of service :'))
if years_of_service>5:salary=salary+0.05*salary
print(f"salary is {salary}")
