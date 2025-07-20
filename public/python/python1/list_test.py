print('Shri Ganesh')

sq = []
for x in range(10):
    sq.append(x*x)

sq2 = [[e, e*e] for e in range(10)]
for x in sq2:
    print(x[0], x[1])

print('---------------------')
for x in sq:
    print("v", x)

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']

""" Return a copy of the string with leading and trailing whitespace removed. """
strip_fruits = [ s.strip() for s in freshfruit]
for s in strip_fruits:
    print('->',s, '<-')