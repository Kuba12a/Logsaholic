# Logsaholic


## Usage 

### 1. Events detection using rules from detection-rules
```
python main.py event-detection --file-name [file name]        
python main.py event-detection --folder-name [folder name]	
```

### 2. Read and display PCAPs using BPF filter
```
python main.py display-captures --file-name [file name] --filter [BPF filter]
python main.py display-captures --folder-name [folder name]  --filer [BPF filter]
```

### 3. Display from text files with grep and regular expressions
```
python main.py grep --file-name [file name] --regular-expression [regular expression] 
python main.py grep --folder-name [folder name] --regular-expression [regular expression] 
```

### 4. Run FastApi
To run fastApi you need to have hypercorn server installed
```
pip install "hypercorn[trio]"
```
Run fastApi using hypercorn
```
hypercorn Api:app --worker-class trio
```