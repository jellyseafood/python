def rec1 (data1, data2 = 0, data3 = 0):
    if data2 == 0:
        print(1)
    elif data2 > 0:
        orig = data3
        if data3 == 0:
            orig = data1
        rec = data1
        count = data2 - 1
        if count > 0:
            rec = data1 * orig

            rec1(rec, count, orig)
        else:
            print(rec)

    elif data2 < 0:
        orig = data3
        if data3 == 0:
            orig = data1
        rec = data1
        count = data2 + 1
        if count < 0:
            rec = data1 * orig

            rec1(rec, count, orig)
        else:
            print(1/rec)

a = int(input("INPUT EXPONENT"))
b = int(input("INPUT INTEGER"))

rec1(b,a)