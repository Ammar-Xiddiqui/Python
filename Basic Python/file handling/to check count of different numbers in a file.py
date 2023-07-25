
from random import randint

# Generate random numbers and write them to file
with open('nums.txt', 'w') as f1:
    for i in range(10000):
        f1.write(f'{randint(1, 10)}\n')

# Read the file and calculate sums
with open('nums.txt', 'r') as f:
    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0
    sum5 = 0
    sum6 = 0
    sum7 = 0
    sum8 = 0
    sum9 = 0
    sum10 = 0
    m = f.readline().strip()
    while m:
        n = int(m)
        if n == 1:
            sum1 += 1
        elif n == 2:
            sum2 += 1
        elif n == 3:
            sum3 += 1
        elif n == 4:
            sum4 += 1
        elif n == 5:
            sum5 += 1
        elif n == 6:
            sum6 += 1
        elif n == 7:
            sum7 += 1
        elif n == 8:
            sum8 += 1
        elif n == 9:
            sum9 += 1
        elif n == 10:
            sum10 += 1
        m = f.readline().strip()

# Print the sums for each number
print(f'sum1: {sum1}')
print(f'sum2: {sum2}')
print(f'sum3: {sum3}')
print(f'sum4: {sum4}')
print(f'sum5: {sum5}')
print(f'sum6: {sum6}')
print(f'sum7: {sum7}')
print(f'sum8: {sum8}')
print(f'sum9: {sum9}')
print(f'sum10: {sum10}')

# Calculate and print the overall sum
overall_sum = sum1 + sum2 + sum3 + sum4 + sum5 + sum6 + sum7 + sum8 + sum9 + sum10
print(f'\nOverall sum: {overall_sum}')
