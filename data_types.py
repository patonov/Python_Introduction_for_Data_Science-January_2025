import math
from math import pi

#print('Hello Python!')

#side_a = int(input())
#side_b = int(input())

#print(side_a * side_b)

#print(isinstance('eho', str))

#print(2**3)

#print(60/8)
#print(60//8)
#print(60%8)

#inches = float(input())
#print(inches * 2.54)

#name = input()
#print(f'Hello, {name}!')

#num = 12.999911
#print(f'{num:.3f}')

#print(math.floor(num))

#RATE_USD_TO_BGN = 1.78991
#bgn_amount = float(input())
#usd_amount = bgn_amount * RATE_USD_TO_BGN
#print(usd_amount)

#radians = float(input())
#degrees = radians * 180 / pi
#print(degrees)

#deposit_amount = float(input())
#term_in_months = int(input())
#annual_interest_rate = float(input()) / 100

#total_amount = deposit_amount + term_in_months * (deposit_amount * annual_interest_rate) / 12

#print(total_amount)

book_pages = int(input())
pages_per_hour = int(input())
days = int(input())

time_needed = book_pages // pages_per_hour
needed_time_per_day = time_needed // days

print(needed_time_per_day)

