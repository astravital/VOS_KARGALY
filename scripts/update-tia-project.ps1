# Script to update TIA Portal V20 project on GitHub
# Usage: .\scripts\update-tia-project.ps1 [commit-message]

param(
    [string]$CommitMessage = "Update TIA Portal V20 project"
)

# Переход в корень проекта (родительская директория от scripts)
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = Split-Path -Parent $scriptPath
Set-Location $projectRoot

Write-Host "Updating TA_PORTAL_V20_PROJECT on GitHub..." -ForegroundColor Cyan

# Force add the TIA Portal project folder
git add -f TA_PORTAL_V20_PROJECT/

# Check if there are changes to commit
$status = git status --porcelain TA_PORTAL_V20_PROJECT/
if ($status) {
    git commit -m $CommitMessage
    Write-Host "Project updated and committed successfully!" -ForegroundColor Green
    Write-Host "Don't forget to push: git push" -ForegroundColor Yellow
} else {
    Write-Host "No changes detected in TA_PORTAL_V20_PROJECT/" -ForegroundColor Yellow
}

