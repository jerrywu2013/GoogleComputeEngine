GoogleComputeEngine SSL Certificate Installation Tutorial


Step One Install Apache and Openssl：
```
apt-get install apache2
apt-get install openssl
```
How to Find your Server's IP address：
```
ifconfig eth0 | grep inet | awk '{ print $2 }'
```
Create SSL Certificate：
```
dpkg -l | grep openssl
apt-get install openssl
openssl genrsa -out 104.155.192.71.key 1024
openssl req -new -key 104.155.192.71.key -out 104.155.192.71.csr

Country Name (2 letter code) [GB]:TW
State or Province Name (full name) [Berkshire]:Taipei County
Locality Name (eg, city) [Newbury]:Taipei City
Organization Name (eg, company) [My Company Ltd]:jerry
Organizational Unit Name (eg, section) []:jerry
Common Name (eg, your name or your server's hostname) []:104.155.192.71
Email Address []:ripplelbue2002@gmail.com
Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []: 
An optional company name []:
ls -l
```
Creating a Self-Signed SSL Certificate:
```
openssl x509 -req -days 365 -in 104.155.192.71.csr -signkey 104.155.192.71.key -out 104.155.192.71.crt

cp 104.155.192.71.crt /usr/local/etc/pki
cp 104.155.192.71.key /usr/local/etc/pki
cp 104.155.192.71.csr /usr/local/etc/pki

vim /etc/apache2/sites-available/default
```
Create VirtualHost:
```
NameVirtualHost *:443
<VirtualHost *:443>
        SSLEngine on
        SSLCertificateFile /usr/local/etc/pki/104.155.192.71.crt
        SSLCertificateKeyFile /usr/local/etc/pki/104.155.192.71.key
        <Directory />
                Options FollowSymLinks
                AllowOverride None
        </Directory>
                <Directory /var/www/>
                Options Indexes FollowSymLinks MultiViews
                AllowOverride None
                Order allow,deny
                allow from all
        </Directory>
        ScriptAlias /cgi-bin/ /usr/lib/cgi-bin/
        <Directory "/usr/lib/cgi-bin">
                AllowOverride None
                Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch
                Order allow,deny
                Allow from all
        </Directory> 
</VirtualHost>
.
.
.
.
SSLCertificateFile /usr/local/etc/pki/104.155.192.71.crt
SSLCertificateKeyFile /usr/local/etc/pki/104.155.192.71.key
</VirtualHost>
```
```
service apache2 stop
service apache2 startssl

```
Check Apache Port 443:
```

netstat -ntulp | grep 443
```
LoadModule and setting default-ssl (Virtual Host)
```
a2enmod ssl
a2ensite default-ssl
```
