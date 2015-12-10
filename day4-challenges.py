import hashlib

key = 'yzbqklnj'
i = 1000000

challenge_one = '00000'
challenge_two = '000000'

while True:
    if hashlib.md5(key + str(i)).hexdigest()[:5] == challenge_two:
        print i
        break
    i += 1
    if ()
    