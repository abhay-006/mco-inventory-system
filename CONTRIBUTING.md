# Git Workflow for Development

This document describes the Git workflow used in the MCO Inventory System repository.

All developers must follow this workflow to avoid conflicts and maintain a stable codebase.

---

# Branch Structure

The repository uses three levels of branches.

```text
main
 └── development
       └── feature branches
```

### main

The **main branch** always contains the stable version of the project.

Rules:

* No direct commits
* Only merged from `development`

---

### development

The **development branch** is used for integrating all active work.

Rules:

* Developers pull updates from this branch
* Feature branches are created from this branch

---

### Feature Branches

Each feature must be implemented in its own branch.

Examples:

```text
feature-gun-model
feature-auth-system
feature-component-crud
feature-inventory-engine
```

---

# Developer Setup

## 1 Clone the Repository

```bash
git clone <repository-url>
cd mco-inventory-system/backend
```

---

## 2 Switch to Development Branch

```bash
git checkout development
```

If the branch does not exist locally:

```bash
git fetch
git checkout development
```

---

## 3 Create a Feature Branch

Create a branch for your task.

Example:

```bash
git checkout -b feature-gun-model
```

---

# Development Workflow

## 1 Work on Your Feature

Make your code changes normally.

---

## 2 Commit Changes

```bash
git add .
git commit -m "Add gun model"
```

---

## 3 Push Your Branch

```bash
git push -u origin feature-gun-model
```

---

## 4 Create Pull Request

On GitHub create a pull request:

```text
feature-gun-model → development
```

The pull request will be reviewed before merging.

---

# Updating Your Branch

Before continuing work, update your branch with the latest changes.

```bash
git checkout development
git pull
```

Then switch back:

```bash
git checkout feature-gun-model
```

---

# Important Rules

1. Never commit directly to `main`.
2. Always create a feature branch.
3. Always pull latest `development` before starting work.
4. All schema changes must use Alembic migrations.
5. Push frequently to avoid losing work.

---

# Summary Workflow

```text
Clone repository
→ checkout development
→ create feature branch
→ implement feature
→ push branch
→ create pull request
→ merge into development
```

---

# Branch Naming Convention

Use the following naming pattern:

```text
feature-<feature-name>
fix-<bug-name>
refactor-<module-name>
```

Example:

```text
feature-auth
feature-component-api
fix-login-error
```
