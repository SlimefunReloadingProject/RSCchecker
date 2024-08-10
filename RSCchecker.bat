cd /d %~dp0
echo off
pip install pyyaml
:loop
python main.py
goto loop
pause