import re,urllib
from urllib.request import *
sites="yahoo rediff flipkart".split()
print(sites)
for i in sites:
	print("searching",i,"sites........")
	u=urlopen("https://"+i+".com")
	content=u.read()
	title=re.findall(r"<style>.*</style>",str(content),re.I)
	for j in sites:
		print(j)

