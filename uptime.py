import datetime, calendar

dob = datetime.date(2007, 6, 20)
now = datetime.date.today()
y = now.year - dob.year
m = now.month - dob.month
d = now.day - dob.day

if d < 0:
    m -= 1
    p_m = (now.month - 2) % 12 + 1
    p_y = now.year if p_m != 12 else now.year - 1
    d += calendar.monthrange(p_y, p_m)[1]

if m < 0:
    y -= 1
    m += 12

pts = []
if y > 0:
    pts.append(f"{y} year{'s' if y > 1 else ''}")
if m > 0:
    pts.append(f"{m} month{'s' if m > 1 else ''}")
if d > 0 or not pts:
    pts.append(f"{d} day{'s' if d > 1 else ''}")

print(', '.join(pts))
