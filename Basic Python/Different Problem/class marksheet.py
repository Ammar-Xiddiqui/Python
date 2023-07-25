from random import*
print(f'roll num  \tmid \t       final \t    sessional\t       total\t      grade')
avg_overal=0
mid_avg=0
ses_avg=0
final_avg=0
fail =0
pas=0
max_final=0
max_mid=0
max_ses=0
min_mid=100
min_ses=100
min_fin=100
max_total=0
min_total=100
i=1
while i<31:
    mid=randint(1,35)
    if mid>max_mid:max_mid=mid
    if mid<min_mid:min_mid=mid
    mid_avg=mid_avg+mid
    fin = randint(1, 40)
    if fin<min_fin:min_fin=fin
    if fin>max_final:max_final=fin
    final_avg=final_avg+fin
    ses = randint(1, 25)
    if ses<min_ses:min_ses=ses
    if ses>max_ses:max_ses=ses
    ses_avg=ses_avg+ses
    total=mid+fin+ses
    avg_overal == avg_overal + total

    if total>max_total:max_total=total
    if total<min_total:min_total=total
    if total>=85:grade='A+';pas=pas+1
    elif total>=75:grade='B';pas=pas+1
    elif total>=65:grade='C';pas=pas+1
    elif total>=55:grade='D';pas=pas+1
    else: grade='F';fail=fail+1


    print(f' {i}\t\t{mid}\t\t{fin}\t\t{ses}\t\t{total}\t\t {grade} ')
    i=i+1
overall_average=avg_overal/30
midterm_average=mid_avg/30
sessional_average=ses_avg/30
average_finalterm=final_avg/30
print('total                       =\t100')
print(f'pas                         =\t{pas}')
print(f'fail                        =\t{fail}')
print(f'overall average marks       =\t{overall_average}')
print(f'midterm average             =\t{midterm_average}')
print(f'sessional average           =\t{sessional_average}')
print(f'average final term          =\t{average_finalterm}')
print(f'maximum marks               =\t{max_total}')
print(f'maximum midterm marks       =\t{max_mid}')
print(f'maximum final marks         =\t{max_final}')
print(f'minimum marks               =\t{min_total}')
print(f'minimum midterm marks       =\t{min_mid}')
print(f'minimum sessional marks     =\t{min_ses}')
print(f'minimum final marks         =\t{min_fin}')










