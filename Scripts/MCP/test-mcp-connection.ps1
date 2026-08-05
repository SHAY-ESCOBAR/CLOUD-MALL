<#
.SYNOPSIS
    SKELETON — Test connectivity to the Unreal MCP server/plugin.

.DESCRIPTION
    This script is a placeholder. It cannot do anything real yet because no
    Unreal MCP server or plugin has been chosen/installed for this project
    (see Docs/Architecture/MCP_ARCHITECTURE.md, Phase 4 in ROADMAP.md).

    Once an Unreal MCP bridge is installed locally, this script should be
    completed to:
      1. Confirm the MCP server process/plugin is running inside the Unreal
         Editor (or as a companion process).
      2. Confirm Claude Code's MCP client configuration points at it
         (transport: stdio or local socket/HTTP, per whatever the chosen
         MCP server uses).
      3. Send a trivial read-only request (e.g. "list available tools" or
         "get engine version") and print the response.
      4. Exit non-zero with a clear message on failure, zero on success.

.NOTES
    Do not hardcode credentials or tokens here. Do not attempt to install
    or modify Unreal plugins from this script.
#>

[CmdletBinding()]
param()

Write-Host "== Unreal MCP Connection Test (SKELETON) ==" -ForegroundColor Cyan
Write-Host ""
Write-Host "This script is not yet functional." -ForegroundColor Yellow
Write-Host "Remaining work before this can run for real:" -ForegroundColor Yellow
Write-Host " 1. Choose and install an Unreal MCP server/plugin locally."
Write-Host " 2. Record its connection details (transport, host/port or command) in"
Write-Host "    Docs/Architecture/MCP_ARCHITECTURE.md."
Write-Host " 3. Configure Claude Code's MCP settings to register that server."
Write-Host " 4. Implement a real connectivity check here (list tools / ping)."
Write-Host ""
Write-Host "No connection attempt was made." -ForegroundColor Yellow
exit 1
