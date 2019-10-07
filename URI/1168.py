num = (6, 2, 5, 5, 4, 5, 6, 3, 7, 6)

vzs = int(input())
while vzs > 0:
    leds = 0
    n = list(input())
    n = [int(i) for i in n]
    for i in n:
        leds += num[i]

    vzs -= 1
    print('{} leds'.format(leds))  