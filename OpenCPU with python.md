# OpenCPU with python

#### Install opencpu (go with suggested defaults)
```
sudo add-apt-repository ppa:opencpu/opencpu-1.4
sudo apt-get install opencpu
```
#####Problem: apt-get-repository Command is Missing
#####sudo: add-apt-repository: command not found)
```
sudo apt-get install software-properties-common python-software-properties
```
#### Install R
```
sudo apt-get update
sudo apt-get install r-base
sudo apt-get install r-base-dev
```
#### Setting External IP(Static)
##### http://IP/ocpu
#### Python Code 
```
import json
import requests
x_data = json.dumps([100,101,102,103,104])
x_mean = requests.post("http://104.155.203.136/ocpu/library/base/R/mean", data={"x":x_data})
print x_mean.content
x_data_result = requests.get("http://104.155.203.136/ocpu/tmp/x0eed0077da/R/.val")
print x_data_result.content
x_data_result_json = requests.post("http://104.155.203.136/ocpu/library/base/R/mean/json", data={"x":x_data})
print x_data_result_json.content
x_data_lm = requests.post("http://104.155.203.136/ocpu/library/stats/R/lm", data={"formula":"speed~dist","data":"cars"})
print x_data_lm.content
x_data_lm_result = requests.get("http://104.155.203.136/ocpu/tmp/x0bbf802ddd/R/.val")
print x_data_lm_result.content
```




