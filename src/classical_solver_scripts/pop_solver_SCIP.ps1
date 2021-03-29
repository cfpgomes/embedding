$FOLDER_NAME = "scenario1_N8_classical"
$FOLDER_NAME
Get-ChildItem -Path src\lp\$FOLDER_NAME | ForEach-Object -Parallel {scip -f $_.FullName -l results\$($using:FOLDER_NAME)\$($_.Name).out}