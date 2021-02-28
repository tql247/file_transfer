set workdir=%~dp0
cd %workdir%
SET PYTHONPATH=.
python file_transfer/main.py
