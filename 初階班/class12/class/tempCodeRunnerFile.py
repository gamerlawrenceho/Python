print('I %f savage' % 94)
print('I %3d savage' % 94)
print('I %03d savage' % 94)

print('I %f savage' % 94)
print('I %.2f savage' % 94)

print('I %s savage' % '94')
print('I {0:s} savage'.format('94'))

A = input()
A = int(A)
print('{0:d}'.format(A))
print('{0:5d}'.format(A))
print('{0:05d}'.format(A))