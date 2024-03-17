# print('I %f savage' % 94)
# print('I %3d savage' % 94)
# print('I %03d savage' % 94)
#
# print('I %f savage' % 94)
# print('I %.2f savage' % 94)
#
# print('I %s savage' % '94')
# print('I {0:s} savage'.format('94'))
#
# A = input()
# A = int(A)
# print('{0:d}'.format(A))
# print('{0:5d}'.format(A))
# print('{0:05d}'.format(A))

# A = input()
# A = float(A)
# print('{0:f}'.format(A))
# print('{0:.2f}'.format(A))

# ans = eval("1+2")
# print(ans)
# ans = eval("1-2")
# print(ans)
# ans = eval("9*9")
# print(ans)
# ans = eval("99**99")
# print(ans)
# ans = eval("2/1")
# print(ans)

# %d %b %B %Y %y %A %a

# import datetime as d

# Date = d.date.today()
# print(d.date.today())
# print(Date)
# print(Date.year)
# print(Date.month)
# print(Date.day)

from datetime import datetime as d

day = input("What is your birthday?")
print(day)
birth = d.strptime(day, "%m/%d/%Y")
print(birth.date())