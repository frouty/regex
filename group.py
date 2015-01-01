"""
pour les heures
00:
01:
02:
03:
.
09
10
11
12
.
19
20
21
22
23

pattern: ^([0-1]?[0-9]|[2][0-3]):([0-5][0-9])$
pour les minutes: 00..59
"""

import re

pattern=re.compile(r'(?P<heure>[0-1]?[0-9]|[2][0-3]):(?P<minute>[0-5][0-9])$')
m=pattern.match('08:10')
m.groupdict()
print m.groupdict()


def check_groupdict(matchobject):
    """
    check group and format
    8 ---> 08
    matchobject is a dictionnary
    """
    if len(match.object['heure'])==1:
        return '0'+matchobject['heure']
    return 

    
    
    return True

entree1=['8h00','09h','8:0','19H00','20-00']

pattern=re.compile(r'(\d{,2})(\D?)(\d{,2})')
pattern

for i in entree1:
    match=pattern.match(i)
    check_format(match)
    for idx in [1,2,3]:
        print "string:%s ---> match.group(%s):%s - type(match.group:%s -len(match.group):%s" %(i,idx,match.group(idx),type(match.group(idx)),len(match.group(idx)),)
       
        

    
    


