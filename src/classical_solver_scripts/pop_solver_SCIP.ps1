$FOLDER_NAME = "N64_B0.5_diversified_classical"
$FOLDER_NAME
Get-ChildItem -Path src\lp\$FOLDER_NAME | ForEach-Object -Parallel {scip -f $_.FullName -l results\$($using:FOLDER_NAME)\$($_.Name).out} -ThrottleLimit 7