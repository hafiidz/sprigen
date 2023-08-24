@echo off

set requirements_txt="%~dp0requirements.txt"
set python_exec="..\..\..\python_embeded\python.exe"

echo Installing SpriGen ...

if exist "%python_exec%" (
    echo Installing with ComfyUI Portable
    for /f "delims=" %%i in (%requirements_txt%) do (
        %python_exec% -s -m pip install -r "%%i"
    )
) else (
    echo Installing with system Python
    for /f "delims=" %%i in (%requirements_txt%) do (
        pip install -r "%%i"
    )
)

pause