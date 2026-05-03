param(
    [string]$PluginRoot = $(Split-Path -Parent $PSScriptRoot),
    [string]$HomeDir = $HOME
)

$pluginSource = (Resolve-Path $PluginRoot).Path
$pluginName = Split-Path $pluginSource -Leaf
$targetPluginRoot = Join-Path $HomeDir "plugins\$pluginName"
$marketplacePath = Join-Path $HomeDir ".agents\plugins\marketplace.json"

New-Item -ItemType Directory -Force (Split-Path $targetPluginRoot -Parent) | Out-Null
New-Item -ItemType Directory -Force (Split-Path $marketplacePath -Parent) | Out-Null

if (Test-Path $targetPluginRoot) {
    Remove-Item -Recurse -Force $targetPluginRoot
}
Copy-Item -Recurse -Force $pluginSource $targetPluginRoot

$marketplace = if (Test-Path $marketplacePath) {
    Get-Content -Raw -Path $marketplacePath | ConvertFrom-Json
} else {
    [pscustomobject]@{
        name = "local-plugins"
        interface = [pscustomobject]@{ displayName = "Local Plugins" }
        plugins = @()
    }
}

if (-not @($marketplace.plugins | Where-Object { $_.name -eq $pluginName })) {
    $marketplace.plugins += [pscustomobject]@{
        name = $pluginName
        source = [pscustomobject]@{
            source = "local"
            path = "./plugins/$pluginName"
        }
        policy = [pscustomobject]@{
            installation = "AVAILABLE"
            authentication = "ON_INSTALL"
        }
        category = "Productivity"
    }
}

$marketplace | ConvertTo-Json -Depth 8 | Set-Content -Path $marketplacePath -Encoding UTF8
Write-Output "Installed plugin to $targetPluginRoot"
Write-Output "Updated marketplace $marketplacePath"
Write-Output "Restart Codex to pick up the plugin."
