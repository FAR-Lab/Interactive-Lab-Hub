## Guideline

#### Step1: Setup the hardware environment

#### Step2: Create a virtual environment
```
python -m venv idd_final_env
source idd_final_env/bin/activate
```

#### Step3: Install required packages
```
pip3 install -r requirement.txt
```

#### Step4: Stop running the mini-screen service
```
sudo systemctl stop mini-screen.service
```

#### Step5: Run application
```
python musicPlayer.py 
```