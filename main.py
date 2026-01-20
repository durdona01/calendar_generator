import datetime

def days_in_month(year, month):
    first = datetime.date(year, month, 1)

    if month == 12:
        next_month = datetime.date(year+1, 1, 1)
    else:
        next_month = datetime.date(year, month+1, 1)
    
    return (next_month - first).days

# print(days_in_month(2026, 1))   # 31
# print(days_in_month(2024, 2))   # 29 


def month_to_lines(y, m, name):
    lines = []
    name = str(name).center(20, '-')
    lines.append(f'{name}')
    lines.append('Mo Tu We Th Fr Sa Su')

    first = datetime.date(y, m, 1)
    start = first.weekday()
    total = days_in_month(y, m)

    week = ['  '] * 7
    day = 1

    for i in range(start, 7):
        week[i] = f'{day:2}'
        day += 1
    lines.append(' '.join(week))

    while day <= total:
        week = ['  '] * 7 
        for i in range(7):
            if day > total:
                break
            week[i] = f"{day:2}"
            day += 1
        lines.append(' '.join(week))
    
    return lines

# print(month_to_lines(2026, 1, 'February'))

months = [
    "January", "February", "March",
    "April", "May", "June",
    "July", "August", "September",
    "October", "November", "December"
]


def print_year(year):
    all_months = []
    for i in range(12):
        all_months.append(month_to_lines(year, i+1, months[i]))
    # print(all_months) 

    for row in range(0, 12, 3):
        m1, m2, m3 = all_months[row:row+3]

        max_lines = max(len(m1), len(m2), len(m3))

        for i in range(max_lines):
                line1 = m1[i] if i < len(m1) else " " * 20
                line2 = m2[i] if i < len(m2) else " " * 20
                line3 = m3[i] if i < len(m3) else " " * 20

                print(line1 + "   " + line2 + "   " + line3)
        print()


# ==========================
year = int(input("Input the year: "))
st = f" Calendar for {year}-year ".center(64, '*')
print('\n', st, '\n' )
print_year(year)