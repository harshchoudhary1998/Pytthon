from re import *
matches=fullmatch("hc","hc") #full wala match hona chaiye
if matches:
	print("Match found at",matches.start(),"index")
else:
	print("match not foud")