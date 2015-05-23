##Install Shiny Server and RStudio on Ubuntu 14.04

####Install R 
```
sudo apt-get install r-base
sudo apt-get install r-base-core
```
####Install the Shiny R package
```
sudo su - -c "R -e \"install.packages('shiny', repos='http://cran.rstudio.com/')\""
```
####Install Shiny Server
###### shiny-server-1.2.2.367-amd64.deb
```
sudo apt-get install gdebi-core
wget http://download3.rstudio.org/ubuntu-12.04/x86_64/shiny-server-1.3.0.403-amd64.deb

sudo gdebi shiny-server-1.3.0.403-amd64.deb
```
```
sudo reload shiny-server
sudo start shiny-server
```

#### http://IP:3838/
#### Install R packages
```
sudo apt-get install libcurl4-openssl-dev 
sudo apt-get install openjdk-7-jdk
export LD_LIBRARY_PATH=/usr/lib/jvm/java-7-openjdk-amd64/jre/lib/amd64/server
R CMD javareconf 
```
####Install RStudio Server
```
wget http://download2.rstudio.org/rstudio-server-0.98.1103-amd64.deb
sudo gdebi rstudio-server-0.98.1103-amd64.deb
sudo chmod -R 777 /usr/local/lib/R
```

#####
http://chrisrzhou.datanaut.io/blog/tutorials/2015/01/19/r-shiny-ec2-bootstrap-guide/#install-shiny-server
