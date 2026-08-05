<#
.SYNOPSIS
    Validates the local repository state before commit/push.

.DESCRIPTION
    Read-only checks: required folder structure, missing required files,
    large files that are not tracked by Git LFS, likely secrets, temp files,
    problematic asset names (NewBlueprint, Cube1, Material2, etc.), and
    uncommitted changes. Prints a report; does not modify any files.

.NOTES
    Run from the repository root, or pass -RepoRoot.
#>

[CmdletBinding()]
param(
    [string]$RepoRoot = ".",
    [int]$LargeFileThresholdMB = 5
)

$ErrorActionPreference = "Continue"
Push-Location $RepoRoot

$issues = New-Object System.Collections.Generic.List[string]

function Write-Section($title) {
    Write-Host ""
    Write-Host "== $title ==" -ForegroundColor Cyan
}

$requiredPaths = @(
    ".github/workflows", ".github/ISSUE_TEMPLATE", "Config", "Content/CORE_AI",
    "Plugins", "Scripts/Setup", "Scripts/Validation", "Scripts/Unreal", "Scripts/MCP",
    "Source", "Tests", "Tools", "Docs/Architecture", "Docs/Setup", "Docs/Workflows", "Docs/Decisions",
    ".gitignore", ".gitattributes", "LICENSE", "README.md", "ROADMAP.md",
    "CONTRIBUTING.md", "SECURITY.md", "CHANGELOG.md", "CLAUDE.md"
)

Write-Section "Folder / required file structure"
foreach ($p in $requiredPaths) {
    if (-not (Test-Path $p)) {
        $msg = "Missing required path: $p"
        Write-Host $msg -ForegroundColor Red
        $issues.Add($msg)
    }
}
if ($issues.Count -eq 0) { Write-Host "All required paths present." -ForegroundColor Green }

Write-Section "Large files not tracked by Git LFS"
$lfsPatterns = @("*.uasset","*.umap","*.fbx","*.obj","*.blend","*.wav","*.mp3","*.png","*.jpg","*.jpeg","*.tga","*.exr","*.hdr","*.mp4","*.mov","*.psd","*.zip")
$trackedFiles = git ls-files
foreach ($f in $trackedFiles) {
    if (-not (Test-Path $f)) { continue }
    $size = (Get-Item $f).Length / 1MB
    if ($size -ge $LargeFileThresholdMB) {
        $isLfsExt = $false
        foreach ($pat in $lfsPatterns) { if ($f -like $pat) { $isLfsExt = $true } }
        if ($isLfsExt) {
            $head = Get-Content $f -TotalCount 1 -ErrorAction SilentlyContinue
            if ($head -notmatch "git-lfs") {
                $msg = "Large file NOT in LFS: $f ($([math]::Round($size,2)) MB)"
                Write-Host $msg -ForegroundColor Red
                $issues.Add($msg)
            }
        } else {
            $msg = "Large file of un-tracked type (consider LFS or excluding): $f ($([math]::Round($size,2)) MB)"
            Write-Host $msg -ForegroundColor Yellow
        }
    }
}

Write-Section "Secrets scan"
$secretPatterns = @("AKIA[0-9A-Z]{16}", "ghp_[A-Za-z0-9]{36}", "-----BEGIN (RSA|EC|OPENSSH|PGP) PRIVATE KEY-----", "xox[baprs]-[A-Za-z0-9-]{10,}")
foreach ($f in $trackedFiles) {
    if (-not (Test-Path $f)) { continue }
    if ($f -match '\.(uasset|umap|fbx|obj|blend|wav|mp3|png|jpg|jpeg|tga|exr|hdr|mp4|mov|psd|zip)$') { continue }
    $content = Get-Content $f -Raw -ErrorAction SilentlyContinue
    if (-not $content) { continue }
    foreach ($pat in $secretPatterns) {
        if ($content -match $pat) {
            $msg = "Possible secret in $f (pattern: $pat)"
            Write-Host $msg -ForegroundColor Red
            $issues.Add($msg)
        }
    }
}
if (Test-Path ".env") {
    $msg = ".env file exists and may be tracked - verify it is gitignored"
    Write-Host $msg -ForegroundColor Red
    $issues.Add($msg)
}

Write-Section "Temporary / forbidden folders tracked in git"
foreach ($pattern in @("Saved","Intermediate","DerivedDataCache","Binaries")) {
    $matches = $trackedFiles | Where-Object { $_ -match "(^|/)$pattern/" }
    if ($matches) {
        foreach ($m in $matches) {
            $msg = "Tracked file inside forbidden folder '$pattern': $m"
            Write-Host $msg -ForegroundColor Red
            $issues.Add($msg)
        }
    }
}

Write-Section "Problematic asset names"
$badNamePatterns = @('^NewBlueprint', '^Cube\d*$', '^Material\d+$', '^Untitled', '^Copy_of_')
$assetFiles = $trackedFiles | Where-Object { $_ -match '\.(uasset|umap)$' }
foreach ($f in $assetFiles) {
    $base = [System.IO.Path]::GetFileNameWithoutExtension($f)
    foreach ($pat in $badNamePatterns) {
        if ($base -match $pat) {
            $msg = "Non-descriptive asset name: $f"
            Write-Host $msg -ForegroundColor Yellow
        }
    }
}

Write-Section "Uncommitted changes"
$status = git status --porcelain
if ($status) {
    Write-Host "There are uncommitted changes:" -ForegroundColor Yellow
    Write-Host $status
} else {
    Write-Host "Working tree clean." -ForegroundColor Green
}

Write-Section "Result"
if ($issues.Count -eq 0) {
    Write-Host "No blocking issues found." -ForegroundColor Green
} else {
    Write-Host "$($issues.Count) issue(s) found:" -ForegroundColor Red
    $issues | ForEach-Object { Write-Host " - $_" }
}

Pop-Location
