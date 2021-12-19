# Logsaholic


## Usage 

### 1. Events detection using rules from detection-rules
```
python3 main.py event-detection 
--paths [path to file/folder] *can be multiple   
--rule *prompt pops up, enter rules >
```

### 2. Read and display PCAPs using BPF filter
```
python3 main.py display-captures
--path [file path] *required
--filter [BPF filter] default='tcp'
```

### 3. Display from text files with grep and regular expressions
```
python3 main.py text search
--paths [path to file/folder] *can be multiple 
--regex [regular expression] 

```

### 4. Run FastApi
To run fastApi you need to have hypercorn server installed
```
pip install "hypercorn[trio]"
```
Run fastApi using hypercorn
```
hypercorn Api/[AlertApi]:app --bind ip_address:port
or
hypercorn Api/[FirewallApi]:app --bind ip_address:port

```


### 5. Updating from requirements
To update libraries from requirements.txt type
```
pip install -r requirements.txt
```
To update requirements.txt 
```
pip freeze > requirements.txt
```

### 6. Specify Dictionaries
Specify dictionaries of 
**malicious_names**, **malicious_IPs**, **malicious_URLs** in Config.py.   
By default its specified to collect data from default dictionaries stored in Dictionaries folder.
