@echo off
echo Pulling from repo
git pull
echo Activating venv
python -m venv .venv
call .venv\Scripts\activate.bat
echo Installing modules
pip install -r requirements.txt
echo Building application
pyinstaller --onedir --noconsole --noconfirm --add-data "src\templates;templates" --add-data "src\static;static" --icon "echo-icon-point-bow.ico" src\desktop_wrapper.py
pause