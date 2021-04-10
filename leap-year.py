year = int(input("Please Enter The 4-Digit Year To See If It Is A Leap Year : "))
leap_y1 =bool(int(year) % 4 == 0)
leap_y2 = bool(int (year) % 100 !=0)
leap_y3 =bool(int(year) % 400 == 0)
leap_y = (leap_y1 and leap_y2) or leap_y3
print(f'Is {year} A Leap_Year : ', leap_y)
