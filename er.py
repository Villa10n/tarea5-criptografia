import re

#Check if the string starts with "The" and ends with "Spain":

txt = "rfc822msgid:1597843756828.86743d3d-cda5-48cb-bdb1-9fcf1a33cd31@bf08x.hubspotemail.net"
er = "^rfc822msgid:[0-9]{13}\.[0-9a-z]{8}\-[0-9a-z]{4}\-[0-9a-z]{4}\-[0-9a-z]{4}\-[0-9a-z]{12}@bf08x.hubspotemail.net"
x = re.search(er, txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")