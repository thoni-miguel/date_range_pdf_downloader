
# How to Use the Script  

## 1. Clone the Repository  
Use Git to clone the repository to your local machine:  

```sh
git clone <repository-url>
cd <repository-folder>
```

## 2. Set Up the Virtual Environment  
Ensure you have **Python** installed on your system. Then, create and activate a virtual environment:  

### On macOS/Linux:  
```sh
python3 -m venv venv
source venv/bin/activate
```

### On Windows (Command Prompt or PowerShell):  
```sh
python -m venv venv
venv\Scripts\activate
```

## 3. Install Dependencies  
With the virtual environment activated, install the required dependencies:  

```sh
pip install -r requirements.txt
```

## 4. Run the Script  
Execute the script with the following command:  

```sh
python3 base.py <end_date>
```

Where `<end_date>` should be a valid date in the format **YYYY.MM.DD**.  

### Example Usage:  
```sh
python3 base.py 2025.2.3
```
