# Checks that this Windows machine is ready for the LearnPython course. Safe to run any time:
# it only looks, it never installs or changes anything.
#
#   powershell -ExecutionPolicy Bypass -File 00_setup\check_setup.ps1

$courseDir = Split-Path -Parent $PSScriptRoot
$venv = Join-Path $courseDir ".venv"
$script:problems = 0

function Ok($msg)         { Write-Host "  [ok] " -ForegroundColor Green -NoNewline; Write-Host $msg }
function Bad($msg, $fix)  { Write-Host "  [X]  " -ForegroundColor Red -NoNewline; Write-Host $msg; Write-Host "       -> $fix"; $script:problems++ }
function Warn($msg, $fix) { Write-Host "  [!]  " -ForegroundColor Yellow -NoNewline; Write-Host $msg; Write-Host "       -> $fix" }

# Runs a command and returns its first line of output, or $null if it failed.
function FirstLine($cmd, [string[]]$cmdArgs) {
    try {
        $out = & $cmd @cmdArgs 2>$null
        if ($LASTEXITCODE -eq 0 -and $out) { return ($out | Select-Object -First 1).ToString() }
    } catch {}
    return $null
}

$sync = "cd `"$courseDir`"; uv sync   (Step 2)"

Write-Host "Required"

$v = FirstLine uv @("--version")
if ($v) { Ok $v } else { Bad "uv not installed" "winget install --id=astral-sh.uv -e   (Step 1), then open a new terminal" }

$python = Join-Path $venv "Scripts\python.exe"
if (Test-Path $python) {
    $pv = FirstLine $python @("--version")
    & $python -c "import sys; sys.exit(sys.version_info < (3, 12))" 2>$null
    if ($LASTEXITCODE -eq 0) {
        Ok "course virtual environment: $pv"
    } else {
        Bad "course virtual environment uses $pv (need 3.12+)" "cd `"$courseDir`"; Remove-Item -Recurse -Force .venv; uv sync   (Step 2)"
    }
} else {
    Bad "course virtual environment missing" $sync
}

$pytest = Join-Path $venv "Scripts\pytest.exe"
if (Test-Path $pytest) { Ok (FirstLine $pytest @("--version")) } else { Bad "pytest not installed in the course venv" $sync }

$ruff = Join-Path $venv "Scripts\ruff.exe"
if (Test-Path $ruff) { Ok (FirstLine $ruff @("--version")) } else { Bad "ruff not installed in the course venv" $sync }

Write-Host ""
Write-Host "Recommended"

$toolBin = Join-Path $env:USERPROFILE ".local\bin"
$onPath = ($env:PATH -split ';') | Where-Object { $_.TrimEnd('\') -ieq $toolBin }
if ($onPath) {
    Ok "$toolBin is on PATH"
} else {
    Warn "$toolBin is not on PATH (only matters for 'uv tool install' tools)" "uv tool update-shell   (Step 4), then open a new terminal"
}

Write-Host ""
if ($script:problems -eq 0) {
    Write-Host "All required pieces are installed. Try: cd 00_setup; uv run python examples.py" -ForegroundColor Green
} else {
    Write-Host "$($script:problems) required piece(s) missing - follow the -> hints above, then run this again." -ForegroundColor Red
    exit 1
}
