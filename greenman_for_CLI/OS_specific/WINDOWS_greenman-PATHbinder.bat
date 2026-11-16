@echo off
set "MYDIR=%USERPROFILE%\bin"
if not exist "%MYDIR%" mkdir "%MYDIR%"
copy "%~dp0CLIgreenman" "%MYDIR%\CLIgreenman"
echo @echo off > "%MYDIR%\CLIgreenman.bat"
echo python "%~dp0CLIgreenman" %%* >> "%MYDIR%\CLIgreenman.bat"
setx PATH "%PATH%;%MYDIR%"