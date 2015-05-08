##Install Shiny Server on Ubuntu 14.04

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
```
sudo apt-get install gdebi-core
wget http://download3.rstudio.org/ubuntu-12.04/x86_64/shiny-server-1.3.0.403-amd64.deb
sudo gdebi shiny-server-1.3.0.403-amd64.deb
```
#### http://IP:3838/
#### Install R packages
```
sudo apt-get install libcurl4-openssl-dev 
sudo apt-get install openjdk-7-jdk
export LD_LIBRARY_PATH=/usr/lib/jvm/java-7-openjdk-amd64/jre/lib/amd64/server
R CMD javareconf 
```
####Install the following R package
```
install.packages(c('GGally', 'geosphere', 'ggmap', 'reshape2', 'xlsx', 'gdata', 'foreign', 'RSQLite', 'XML', 'jsonlite', 'dplyr', 'ggplot2', 'rmarkdown', 'knitr', 'shiny' )) 
```
