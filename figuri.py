while True:
    chek = 0
    with open("tochki.txt", 'r') as t:
        f1 = t.readlines(1)[0].rstrip().split()
        f2 = t.readlines(2)[0].rstrip().split()


    def position(a, b, c):
        return ((b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0]))


    def rast(d, e):
        return (math.sqrt((d[1] - e[1]) ^ 2 + (d[0] - e[0]) ^ 2))


    def translate(f):
        try:
            for i in range(len(f)):
                f[i] = f[i].split(';')
                f[i] = list(map(int, f[i]))
            return (f)
        except:
            print('Вы ввели не правильное значение или не по образцу введите значение снова')
            return (1)

    f1 = translate(f1)
    f2 = translate(f2)
    if f1 == 1 or f2 == 1:
        continue
    buf = 0
    if len(f1) < len(f2):
        buf = f1
        f1 = f2
        f2 = buf
    for i in range(len(f1)):
        if i == len(f1) - 1:
            for j in range(len(f2)):
                if j == (len(f2) - 1):
                    if position(f1[i], f1[0], f2[j]) * position(f1[i], f1[0], f2[j]) <= 0 and position(f2[j], f2[0],
                                                                                                       f1[
                                                                                                           i]) * position(
                        f2[j],
                        f2[0],
                        f1[
                            0]) <= 0:
                        if position(f1[i], f1[0], f2[j]) == 0 and position(f1[i], f1[0], f2[j]) == 0 and position(f2[j],
                                                                                                                  f2[0],
                                                                                                                  f1[
                                                                                                                      i]) == 0 and position(
                            f2[j], f2[0], f1[0]) == 0 and not (
                                        rast(f1[i], f1[0]) >= rast(f1[i], f2[j]) or rast(f1[i],
                                                                                         f1[0] >= rast(f1[i], f2[0]))):
                            break

                        print('Пересекаются')
                        exit()
                    break
                if position(f1[i], f1[0], f2[j]) * position(f1[i], f1[0], f2[j + 1]) <= 0 and position(f2[j], f2[j + 1],
                                                                                                       f1[
                                                                                                           i]) * position(
                    f2[j],
                    f2[j + 1],
                    f1[0]) <= 0:
                    print('Пересекаются')
                    exit()
            break
        for j in range(len(f2)):
            if j == (len(f2) - 1):
                if position(f1[i], f1[i + 1], f2[j]) * position(f1[i], f1[i + 1], f2[0]) <= 0 and position(f2[j], f2[0],
                                                                                                           f1[
                                                                                                               i]) * position(
                    f2[j],
                    f2[0],
                    f1[
                                i + 1]) <= 0:
                    print('Пересекаются')
                    exit()
                break
            if position(f1[i], f1[i + 1], f2[j]) * position(f1[i], f1[i + 1], f2[j + 1]) <= 0 and position(f2[j],
                                                                                                           f2[j + 1],
                                                                                                           f1[
                                                                                                               i]) * position(
                f2[j],
                f2[j + 1],
                f1[i + 1]) <= 0:
                print('Пересекаются')
                exit()
    print('Не пересекаются')
    break
