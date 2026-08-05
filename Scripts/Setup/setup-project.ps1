<#
.SYNOPSIS
    Checks the local workstation for the tools this project needs.

.DESCRIPTION
    Read-only environment check for CLOUD-MALL. Reports the presence and
    version of Git, GitHub CLI, Git LFS, Claude Code, and Unreal Engine.
    Does NOT install anything, does NOT modify PATH, and does NOT change any
    system state. If something is missing, it prints clear guidance and lets
    you decide whether to install it.

.NOTES
    Safe to re-run at any time.
#>

[CmdletBinding()]
param()

$ErrorActionPreference = "Continue"

function Write-Section($title) {
    Write-Host ""
    Write-Host "== $title ==" -ForegroundColor Cyan
}

function Test-CommandExists($command) {
    return [bool](Get-Command $command -ErrorAction SilentlyContinue)
}

$results = [ordered]@{}

Write-Section "Operating System"
$os = if ($IsWindows) { "Windows" } elseif ($IsMacOS) { "macOS" } elseif ($IsLinux) { "Linux" } else { "Unknown" }
Write-Host "Detected OS: $os"
$results["OS"] = $os

Write-Section "Git"
if (Test-CommandExists "git") {
    $gitVersion = (git --version)
    Write-Host "Found: $gitVersion" -ForegroundColor Green
    $results["Git"] = $gitVersion
} else {
    Write-Host "Git NOT found. Install from https://git-scm.com/downloads" -ForegroundColor Red
    $results["Git"] = "NOT FOUND"
}

Write-Section "GitHub CLI (gh)"
if (Test-CommandExists "gh") {
    $ghVersion = (gh --version | Select-Object -First 1)
    Write-Host "Found: $ghVersion" -ForegroundColor Green
    $results["GitHubCLI"] = $ghVersion
    Write-Host "Checking auth status..."
    gh auth status
} else {
    Write-Host "GitHub CLI NOT found. Install from https://cli.github.com/" -ForegroundColor Red
    $results["GitHubCLI"] = "NOT FOUND"
}

Write-Section "Git LFS"
if (Test-CommandExists "git-lfs") {
    $lfsVersion = (git lfs version)
    Write-Host "Found: $lfsVersion" -ForegroundColor Green
    $results["GitLFS"] = $lfsVersion
} else {
    Write-Host "Git LFS NOT found. Install from https://git-lfs.com/" -ForegroundColor Red
    $results["GitLFS"] = "NOT FOUND"
}

Write-Section "Claude Code"
if (Test-CommandExists "claude") {
    Write-Host "Found 'claude' on PATH." -ForegroundColor Green
    $results["ClaudeCode"] = "FOUND"
} else {
    Write-Host "Claude Code NOT found on PATH. See https://claude.com/claude-code" -ForegroundColor Red
    $results["ClaudeCode"] = "NOT FOUND"
}

Write-Section "Unreal Engine"
$unrealFound = $false
if ($IsWindows) {
    $candidatePaths = @(
        "C:\Program Files\Epic Games",
        "$env:LOCALAPPDATA\UnrealEngine"
    )
    foreach ($p in $candidatePaths) {
        if (Test-Path $p) {
            Write-Host "Found Epic Games / Unreal Engine folder: $p" -ForegroundColor Green
            Get-ChildItem $p -Directory -ErrorAction SilentlyContinue | ForEach-Object { Write-Host "  - $($_.Name)" }
            $unrealFound = $true
        }
    }
}
if (-not $unrealFound) {
    Write-Host "Unreal Engine installation not detected automatically." -ForegroundColor Yellow
    Write-Host "If it is installed, verify manually via the Epic Games Launcher."
}
$results["UnrealEngine"] = if ($unrealFound) { "DETECTED" } else { "NOT DETECTED (verify manually)" }

Write-Section "Summary"
$results.GetEnumerator() | ForEach-Object { Write-Host ("{0,-15}: {1}" -f $_.Key, $_.Value) }

Write-Host ""
Write-Host "This script does not install or modify anything." -ForegroundColor Cyan
Write-Host "If any tool is missing, install it manually and re-run this script." -ForegroundColor Cyan
