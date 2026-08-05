# ADR-001: GitHub-First Approach

## Status

Accepted — 2026-08-05

## Context

Same rationale as `CORE-Unreal-AI`'s ADR-001: Unreal Engine 5 runs locally
and cannot run inside GitHub Actions/CI for Editor work. CLOUD MALL adds a
further constraint on top: it intends to eventually process real purchases,
which raises the bar on auditability, reversibility, and separation between
"safe to automate" (blockout, visuals) and "requires explicit human
approval" (payments going live).

## Decision

Establish the GitHub branch, its documentation, version control
conventions, validation automation, and connection plan **before** creating
any Unreal project, mall layout, or store/payment integration. GitHub is
the system of record; Unreal Engine 5 always runs locally; any real-money
path requires a separate, explicit approval gate (see `CLAUDE.md`).

## Consequences

- Every change — including AI-generated ones — is committed, reviewable,
  and revertible through normal git operations.
- GitHub Actions can validate repository hygiene immediately.
- No payment/checkout code goes live without a distinct approval step,
  documented in the PR that introduces it.
- Large binary assets are tracked via Git LFS from the start.
- No 3D content, mall layout, or purchase flow is created until this
  foundation is in place and reviewed.
