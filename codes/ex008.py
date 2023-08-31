from time import sleep
timer = int(input('Digite a comtagem regressiva: '))
for time in range(timer, 0, -1):
    time + 1
    sleep(1)
    print(time)
print('Explosão, explosão ')