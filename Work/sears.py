bill_thickness = 0.11 * 0.001 # Meters (0.11 mm)
sears_height = 442 # Height (meters)

bill_count = 1
day = 1

while bill_count * bill_thickness <= sears_height:
    day += 1
    bill_count *= 2

print(f'Number of bills: {bill_count}, overall height: {bill_count*bill_thickness}, days : {day}')
