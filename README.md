-The technology stack used is Linux, Apache2, MySQL and Python 3.4.3


===================INSTRUCTIONS===================================
-Install Apache, mysql, python on linux

-Register Python with Apache.
Disable multithreading.

    sudo a2dismod mpm_event

Give permissions to run script.

    sudo a2enmod mpm_prefork cgi

-Enable cgi-script for a directory by navigating 
$sudo nano /etc/apache2/sites-enabled/000-default.conf

Insert this line below <VirtualHost *:80\>.
<Directory /var/www/dirname>
    Options +ExecCGI
    AddHandler cgi-script .py
</Directory>

And replace dir name in line 
DocumentRoot /var/www/dirname

-Run mysql: mysql -u root -p

-Create Database:db 
-CREATE TABLE output (hash VARCHAR(50), detection_names VARCHAR(50), engines_detected INT, scan_date DATE)


-Run Apache server

-Place index.html and index.py in /var/www/html folder

Navigate to http://localhost on webbrowser.
Browse and select file.
===============================================================================


===============================PROJECT FILES====================================

index.html - Creates an html website that allows to upload a file.
index.py - python script that is invoked on index.html submit button. It analyses the hash values using the API and stores the result in SQL database. It views the output in HTML TABLE format.

================================================================================


==============================DEPENDENCIES======================================

Install virustotal-api using pip

sudo pip install virustotal-api

Install HTML.py module from (https://www.decalage.info/python/html#attachments)

=================================================================================


=============================ISSUES==============================================

Intially I had an issue to invoke the python script from the html form.
Using cgi-script I was able to solve that issue.

I was having trouble displaying the results as and html table.
I found a module HTML.py that can build htmltable in python.

(NOT SOLVED)
In order to retrieve the existing record from the file I tried to check the database(hash field) for the text file values.
If it returns true than than it is displayed otherwise fetched from api.

==================================================================================


