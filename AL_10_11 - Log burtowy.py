import sys

try:
    while True:
        dane = [x for x in input().split()]
        h1,m1,s1 = dane[0].split(':')
        h2,m2,s2 = dane[1].split(':')
        l = float(dane[2])
        h3 = int(h2) - int(h1)
        m3 = int(m2) - int(m1)
        s3 = int(s2) - int(s1)
        diff = 3600 * h3 + 60 * m3 + s3
        result = l * 3.6 / diff
        result2 = l * 3.6 / (diff * 1.852)
        print('{:0.1f} {:0.1f}'.format(result,result2))
except:
    sys.exit(0)