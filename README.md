# Discord Bot in PY
 playing with discord bot in python


## Setup 

### Installing Python
MacOS already comes with [Python3](https://www.python.org/downloads/)
- To check current python verison open the terminal and type `python --verison`
- returns something like: Python 3.9.6

---
### Setting up Virtual Environment
Because Python installs are system wide, if we were to install say NumPy 1.23 we won't be able to run version 1.26. If we want to installed 1.26 then we have to uninstall 1.23. This could lead to problems as the updated version may have new implementations of functions we used in our project. Ultimately it would cause us to reinstall 1.23 and 1.26 whenever we switch projects. **Virtual Environments** create a separate, isolated instance of the Python runtime for a project each with its own complement of packages.
- Open a terminal at folder path and do command `python3 -m venv ENV_DIR`
  - ENV_DIR is a folder name, we can change this
  - In our folder there should be a folder called `ENV_DIR`
- In VS code we can see which **venv** we are in 
  
[Insert gif]
- if our terminal says (ENV_DIR) CURRENT_PATH % its activated - we type `deactivate` to exit it
  
[Insert gif]
  
#### Why venv
- Running with the system (path) Python and libraries limits you to one specific Python version
- Running all Python applications on one Python installation can lead to version conflicts
- venv is are ways to self-contain Python installs

---
### Dependencies
- Python dependencies are defined in **requirements.txt**
- `pip freeze > requirements.txt` save all your python libraries with current version into requirements.txt
