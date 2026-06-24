$pythonPath = (Get-Command python).Source
$scriptDir  = "C:\app\res"

$targets = @(
    @{ Name = "1280"; Script = "1280.py" },
    @{ Name = "1080"; Script = "1080.py" }
    @{ Name = "1920"; Script = "1920.py" }
)

foreach ($t in $targets) {
    $shortcutPath = Join-Path $scriptDir ("$($t.Name).lnk")
    $scriptPath   = Join-Path $scriptDir $t.Script

    $WshShell = New-Object -ComObject WScript.Shell
    $Shortcut = $WshShell.CreateShortcut($shortcutPath)
    $Shortcut.TargetPath = $pythonPath
    $Shortcut.Arguments  = "`"$scriptPath`""
    $Shortcut.WorkingDirectory = $scriptDir
    $Shortcut.WindowStyle = 7   # minimized, đỡ giật console
    $Shortcut.Save()

    Write-Host "Đã tạo: $shortcutPath"
}