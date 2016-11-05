import requests 
import unicodedata
import json
import urllib3 
import datetime
import dateutil.parser

# Step 1 
step1 = requests.post('http://challenge.code2040.org/api/register', data = {'token': '0af6a2c9391eb006b710202cfc443cbb', 'github':'https://github.com/Chukwuemelie/CODE2040.git'})

# Step 2
step2 = requests.post('http://challenge.code2040.org/api/reverse', data = {'token': '0af6a2c9391eb006b710202cfc443cbb'})

word = step2.text
print(word)

def rev(exp):
	start = len(exp)-1
	end = 0

	ans = ""
	
	for i in exp:
		ans = i + ans

	return ans

res = rev(word)
print(res)
step2_complete = requests.post('http://challenge.code2040.org/api/reverse/validate', data = {'token': '0af6a2c9391eb006b710202cfc443cbb', 'string': res })


#Step 3 
step3 = requests.post('http://challenge.code2040.org/api/haystack', data = {'token': '0af6a2c9391eb006b710202cfc443cbb'})
parsed_json = json.loads(step3.text)
needle = parsed_json["needle"]
haystack = parsed_json["haystack"]

index = 0
for hay in haystack:
	if(hay == needle):
		break
	index = index + 1

step3_complete = requests.post('http://challenge.code2040.org/api/haystack/validate', data = {'token': '0af6a2c9391eb006b710202cfc443cbb', 'needle': index})


#Step 4
http = urllib3.PoolManager()
step4 = http.request('POST','http://challenge.code2040.org/api/prefix', fields = {'token' : '0af6a2c9391eb006b710202cfc443cbb'})
parsed_data_step_4 = json.loads(step4.data.decode('ascii'))
prefix_word = parsed_data_step_4["prefix"]
count = 0
word_array = parsed_data_step_4["array"]
step4_ans = []

for word in word_array:
	if word.startswith(prefix_word) == False:
		step4_ans.append(word)

step4_complete = requests.post('http://challenge.code2040.org/api/prefix/validate', json = {'token': '0af6a2c9391eb006b710202cfc443cbb', 'array' : step4_ans })


#Step 5
step5 = requests.post('http://challenge.code2040.org/api/dating', data = {'token':'0af6a2c9391eb006b710202cfc443cbb' })
parsed_json_step5 = json.loads(step5.text)
datestamp_string = parsed_json_step5["datestamp"]
interval = parsed_json_step5["interval"]
datestamp = dateutil.parser.parse(datestamp_string)
datestamp = datestamp + datetime.timedelta(0, interval)
datestamp = datestamp.isoformat()

#Converting datetime object to string
step5_ans = str(datestamp)

step5_ans = step5_ans[:-6]
step5_ans = step5_ans + 'Z'
step5_complete = requests.post('http://challenge.code2040.org/api/dating/validate', json = {'token': '0af6a2c9391eb006b710202cfc443cbb' , 'datestamp': step5_ans})


