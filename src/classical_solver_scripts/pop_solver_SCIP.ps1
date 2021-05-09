$FOLDER_NAME = "N32_B0.5_industry_correlated_classical"
$FOLDER_NAME
Get-ChildItem -Path src\lp\$FOLDER_NAME | ForEach-Object -Parallel {scip -f $_.FullName -l results\$($using:FOLDER_NAME)\$($_.Name).out} -ThrottleLimit 23