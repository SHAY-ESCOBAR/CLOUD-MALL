# Security Policy

## Reporting a vulnerability

If you discover a security issue (leaked credential, exposed secret, unsafe
script behavior), open a private report to the repository owner rather than
a public issue. Do not include the sensitive material itself in the report.

## Rules enforced in this repository

- No secrets, tokens, API keys, `.env` files, or credentials may be
  committed. `.gitignore` blocks common patterns, and
  `.github/workflows/repository-validation.yml` scans for common secret
  patterns on every push/PR.
- No force-pushes to `main`.
- No history rewrites without explicit owner approval.
- No unfamiliar/unverified third-party Unreal plugins.
- No commercial/licensed assets without a verified license.

## If a secret is accidentally committed

1. Rotate/revoke the credential immediately at the source (GitHub, cloud
   provider, etc.) — removing it from git history does not undo exposure.
2. Remove it from the working tree in a new commit.
3. Coordinate with the repository owner before rewriting history, since
   that affects everyone with a clone.
