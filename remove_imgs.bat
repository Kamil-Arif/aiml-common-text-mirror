@echo off
setlocal enabledelayedexpansion

set "dirPath=%~dp0"

for /r "%dirPath%" %%f in (*.jpg, *.jpeg, *.png, *.bmp, *.gif) do (
    echo Deleting "%%f"
    del "%%f"
)

echo All image files have been deleted.
pause>nul