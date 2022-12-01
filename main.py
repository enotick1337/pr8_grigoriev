import random
password = list('abcdefghijklmnopqrstuvwxyz')
password = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
password = list('1234567890')
random.shuffle(password)
password = ''.join([random.choice(password) for x in range(11)])
print (password)
