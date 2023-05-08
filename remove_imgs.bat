@echo off
setlocal enabledelayedexpansion

set "dirPath=%~dp0"

for /r "%dirPath%" %%f in (*.jpg, *.jpeg, *.png, *.bmp, *.gif, *.zip, *.csv, *.mp4, *.pdf) do (
    if /i not "!filePath!" == "%dirPath%.git\" (
        echo Deleting "%%f"
        del "%%f"
    )
)

echo All image files have been deleted.
pause>nul