pyinstaller --onefile --uac-admin --icon=icon.ico main.py
del main.spec 
rmdir /s /q build
move dist\main.exe portable.exe
rmdir /s /q dist