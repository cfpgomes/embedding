$FOLDER_NAME = "WV_N64_B0.5_correlated"
$FOLDER_NAME
Get-ChildItem -Path src\lp\$FOLDER_NAME | ForEach-Object -Parallel {scip -f $_.FullName -l results\$($using:FOLDER_NAME)\$($_.Name).out} -ThrottleLimit 7