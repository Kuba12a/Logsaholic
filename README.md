# Logsaholic


## Usage 

### 1. Events detection using rules from detection-rules
```
python3 main.py event-detection 
--path [path to file/folder] *can be multiple   
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
--path [path to file/folder] *can be multiple 
--regex [regular expression] 
```