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

#book_pages = int(input())
#pages_per_hour = int(input())
#days = int(input())

#time_needed = book_pages // pages_per_hour
#needed_time_per_day = time_needed // days

#print(needed_time_per_day)

price_of_pens = 5.80
price_of_markers = 7.20
price_of_board_cleaner = 1.20

number_of_pens = int(input())
number_of_markers = int(input())
number_of_cleaners = int(input())
discount_rate = int(input())

total_price = number_of_pens * price_of_pens + number_of_markers * price_of_markers + number_of_cleaners * price_of_board_cleaner
total_price = total_price - total_price * (discount_rate / 100)

print(total_price)

