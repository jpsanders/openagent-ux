# openagent-ux installation script for Windows (PowerShell)

Write-Host "Installing openagent-ux skills..." -ForegroundColor Cyan

# Create Claude config directory if it doesn't exist
$claudeDir = "$env:USERPROFILE\.claude"
if (!(Test-Path $claudeDir)) {
    New-Item -ItemType Directory -Path $claudeDir -Force | Out-Null
}

# Copy the agents folder to Claude config
if (Test-Path ".agents") {
    Copy-Item -Path ".agents\*" -Destination "$claudeDir\" -Recurse -Force
    Write-Host "✅ Skills copied to $claudeDir\" -ForegroundColor Green
} else {
    Write-Host "⚠️ .agents directory not found. Are you in the right directory?" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host "  INSTALLATION COMPLETE" -ForegroundColor Green
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next steps:" -ForegroundColor White
Write-Host "1. Restart your AI agent" -ForegroundColor White
Write-Host "2. Run /brand to establish your brand identity" -ForegroundColor White
Write-Host "3. Run /build to create your website" -ForegroundColor White
Write-Host ""
Write-Host "Demo app:" -ForegroundColor White
Write-Host "  cd example-app" -ForegroundColor White
Write-Host "  npm install" -ForegroundColor White
Write-Host "  npm run dev" -ForegroundColor White
Write-Host ""
Write-Host "For installation help, see README.md" -ForegroundColor Gray