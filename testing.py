#!/usr/bin/python

import cgi
import cgitb
import json
import sys
import time
import HTML  
from virus_total_apis import PublicApi as VirusTotalPublicApi

# Print necessary headers.
print("Content-Type: text/html")
print()

form = cgi.FieldStorage()
fileitem = form["myfile"]

API_KEY = '24a29f92dbfc46bdb2bddc635d5ecbc0084f888dde2aaba2e4c47977b11098da'
virustotal = VirusTotalPublicApi(API_KEY)
# ====================================================

# ============== INSERT DATA INTO TABLE =================

HEADER_ROW = [
    'hash_value (MD5 or SHA256)',
    'FORTINET detection names',
    'Number of engines detected',
    'Scan Date'
]
table_data = []

import pymysql
conn = pymysql.connect(
    db='test',
    user='root',
    passwd='zaheena',
    host='localhost')
c = conn.cursor()

lines = fileitem.file.readlines()

for line in lines:
	
	response = virustotal.get_file_report(line)
	json_data = json.loads(json.dumps(response))
	
	if json_data['results']['response_code'] == 1 and \
       'Fortinet' in json_data['results']['scans']:

		c.execute("INSERT INTO output VALUES ('%s', '%s', '%d', '%s' )" % (json_data['results']['md5'], json_data['results']['scans']['Fortinet']['result'], json_data['results']['positives'], json_data['results']['scan_date']))

	elif json_data['results']['response_code'] == 1 and \
            'Fortinet' not in json_data['results']['scans']:
		c.execute("INSERT INTO output VALUES ('%s', '--', '%d', '%s' )" % (json_data['results']['md5'], json_data['results']['positives'], json_data['results']['scan_date']))

	else:
		test_data = str(line, 'utf-8')
		c.execute("INSERT INTO output VALUES ('%s', 'Hash is not in database', '--', '--' )" % (test_data))
		
		time.sleep(15)


# ====================================================

# ============== PRINT AS HTML TABLE =================

c.execute("SELECT * FROM output")
table_data = c.fetchall()
htmltable = HTML.table(table_data, header_row=HEADER_ROW)
conn.commit()
print("<center>")
print("<h4>Analysis Results")
print(htmltable)
print("</center>")
