Send-MailMessage -To "isaacleganik@gmail.com" -From "ileganik9181@gmail.com" -Subject "IT3038C Windows SysInfo" -Body $BODY -SmtpServer smtp.gmail.com -port 587 -UseSSL -Credential (Get-Credential)
$BODY = "This machine's IP is $IPv4. User is $User. Hostname is $HostName. PowerShell Version $Version. Today's Date is $Date."
$IPv4 = (Get-NetIPAddress).ipv4address | Select-String "192*"
$User = (Get-ChildItem Env:USERNAME).Value
$HostName = $env:COMPUTERNAME
$Version = $PSVersionTable.PSVersion.ToString()
$Date = (Get-Date).ToString("dddd, MMMM dd, yyyy") 

Write-Host($BODY)