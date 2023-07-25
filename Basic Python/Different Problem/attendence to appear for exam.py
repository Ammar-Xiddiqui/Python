'''
A student will not allowed to sit in exam if his/her attendance is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not.
'''
num_of_clas_held=int(input('enter number held :'))
num_of_clas_attend=int(input('enter number attended :'))
per=num_of_clas_attend/num_of_clas_held*100
print(f'percentage is {per}')
if per>=75: print('student allowed to take exams')
else:print('student is not allowed to take exams')
