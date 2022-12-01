import random
password = list('abcdefghijklmnopqrstuvwxyz')
password = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
random.shuffle(password)
password = ''.join([random.choice(password) for x in range(11)])
print (password)
