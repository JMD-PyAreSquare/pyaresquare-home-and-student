dim = open('config.txt')
wh = dim.read()
w = wh.split('\n', 1)[0]
h = wh.split('\n', 1)[1]
print(f'{w}, {h}')
dim.close()