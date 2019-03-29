def vowe(sentence):
	vowels=['a','e','i','o','u']
	vowel_count={}
	for x in vowels:
		vowel_count[x]=0
	for y in sentence.lower():
		if y in vowels:
			vowel_count[y] +=1
	return vowel_count
    
x=vowe("hey its me harsh")
print(x)