day, night, v = map(int,input().split())
count = 0

if (v-night) % (day-night) == 0:
    print((v-night)//(day-night))
else:
    print((v-night)//(day-night)+1)
