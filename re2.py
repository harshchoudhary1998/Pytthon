from re import *
matches=match("hc","hc student of skit") #first wala match hona chaiye
if matches:
	print("Match found at",matches.start(),"index")
else:
	print("match not foud")