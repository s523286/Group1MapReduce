#Referenced Dr. Case's slides on MapReduce in python
#sort.py will sort our key/value pairs alphabetically
o = open( "o.txt", "r")
s = open("s.txt", "w")

lines = o.readlines()
lines.sort()

for line in lines:
    s.write(line)

o.close()
s.close()