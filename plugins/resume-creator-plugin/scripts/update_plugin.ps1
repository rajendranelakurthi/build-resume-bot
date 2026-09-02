param(
    [string]$PluginRoot = $(Split-Path -Parent $PSScriptRoot),
    [string]$HomeDir = $HOME
)

$installScript = Join-Path $PSScriptRoot "install_plugin.ps1"
if (-not (Test-Path $installScript)) {
    throw "Missing install script at $installScript"
}

Write-Output "Updating plugin from $PluginRoot"
powershell -ExecutionPolicy Bypass -File $installScript -PluginRoot $PluginRoot -HomeDir $HomeDir
