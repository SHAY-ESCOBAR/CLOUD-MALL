# GitHub Setup

## Repository

- Name: `CLOUD-MALL`
- Visibility: Private by default. Only make public with explicit owner
  approval.

## Branch protection (recommended, to configure on GitHub)

- Protect `main`: require PR review, require the `Repository Validation`
  check to pass, disallow force-push, disallow deletion.
- Protect `develop` similarly if it is used as a shared integration branch.

## Access

- Do not add collaborators or change repository visibility without explicit
  owner approval.
- Do not connect a different GitHub account without explicit approval.

## GitHub CLI

```bash
gh auth status                      # confirm login
gh repo create CLOUD-MALL --private --source=. --remote=origin
git push -u origin <branch-name>
```

Never use `--force` with `git push` against a shared branch, and never push
directly to `main`.

## Secrets

No secrets belong in this repository. If GitHub Actions ever needs a
credential (e.g. for a future self-hosted runner registration), store it in
**GitHub Actions Secrets**, never in tracked files.
