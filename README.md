# Discord Bot in PY
 playing with discord bot in python


## Setup 
### Installing Python
MacOS already comes with Python3 (system python, don't mess with it)
- To check current python verison open the terminal and type `python --verison`
- returns something like: `Python 3.9.6` 
  
We want a fresh install, of the latest verison of Python3 as 3.9's support is ending this year
- This project will use [Python 3.12.4 64-bit](https://www.python.org/downloads/)
- The version should change by itself, we can check by typing `python --verison`
- We can also look at the path by using command `which python3`
- returns: **/Library/Frameworks/Python.framework/Versions/3.12/bin/python3**
- Make sure at the end of the install to get the **certificate file** with (Install Certificates.command) in folder

---
### Virtual Environments (venv)
Because Python installs are system wide, if we were to install say NumPy 1.23 we won't be able to run version 1.26. If we want to installed 1.26 then we have to uninstall 1.23. This could lead to problems as the updated version may have new implementations of functions we used in our project. Ultimately it would cause us to reinstall 1.23 and 1.26 whenever we switch projects. **Virtual Environments** create a separate, isolated instance of the Python runtime for a project each with its own complement of packages.

#### Why venv
- Running with the system (path) Python and libraries limits you to one specific Python version
- Running all Python applications on one Python installation can lead to version conflicts
- venv is are ways to self-contain Python installs

---
#### Setting up Virtual Environment
1. In the folder make a file called `main.py`
2. Set the Python Interpreter to 3.12.4
3. Open a terminal at folder path and do command
```
python3 -m venv .ENV_DIR
```
   - .ENV_DIR is the folder name (don't forget to add to .gitignore)
   - In our project folder there should be a folder called `.ENV_DIR`
4. A prompt: **We noticed a new environment has been created. Do you want to select it for the workspace folder?**
   - Click **Yes**

![steps.png](https://github.com/dongaCS/discord-py/blob/main/step%20.png?raw=true)
- Open a new terminal and if you see (.ENV_DIR) CURRENT_PATH % its activated
  
![active.png](https://github.com/dongaCS/discord-py/blob/main/active.png?raw=true)

- To exit out of the venv do command `deactivate` and (.ENV_DIR) should disappear
- To reactivate, open a new terminal at folder

---
### Dependencies

#### (.ENV_DIR) CURRENT_PATH % Installs
1. [discord.py 2.4.0](https://pypi.org/project/discord.py/)
```
python3 -m pip install -U discord.py
```
2. [python-dotenv 1.0.1](https://pypi.org/project/python-dotenv/)
```
pip3 install python-dotenv
```

---
#### Python dependencies are defined in: requirements.txt
```
pip3 freeze > requirements.txt
``` 
- will create txt file and saves all your python libraries


