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


==============================DEPENDENCIES======================================

Install virustotal-api using pip

sudo pip install virustotal-api

Install HTML.py module from (https://www.decalage.info/python/html#attachments)

=================================================================================


