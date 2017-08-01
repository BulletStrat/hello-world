import xreadlines, sys

f = open('b.txt', 'r')
dict = {}
next(f)
i = 0
for line in f:
    i += 1
    line = line.split(',')
    line = (line[2].replace('\n', '') + ',' + line[1] + ";" + line[0]).strip()
    if line.startswith(",") == 1:
        line = str("Blank") + str(i) + line
    else:
        line = line

    k, v = line.strip().split(',')
    dict[k.strip()] = v.strip()
f.close()

f = open('a.txt', 'r')
next(f)
with open('result.txt', 'w') as s:
    for lines in f.xreadlines():
        lines = lines.split(',')
        zone = lines[0]
        ali1 = lines[1]
        ali2 = lines[2].replace('\n', '')

        ##I think below line make same line and no need line


        for eachkey in dict.keys():
            if eachkey in ali1:
                result = zone + ";" + ali1 + ";" + dict[eachkey] + ";" + ali2 + ";"

            elif eachkey not in ali1:
                result = zone + ";" + ali1 + ";" + "N/A" + ";" + ali2 + ";"

                s.write(result + '\n')

s.close()
