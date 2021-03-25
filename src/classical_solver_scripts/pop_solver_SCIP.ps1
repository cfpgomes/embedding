$FOLDER_NAME = "scenario2_B0.2_classical"

Get-ChildItem -Path src\lp\$FOLDER_NAME | ForEach-Object {scip -f $_.FullName -l results\"$FOLDER_NAME"\$_.out}