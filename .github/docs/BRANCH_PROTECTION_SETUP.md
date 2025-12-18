# Branch Protection Setup for PR Merge Blocking

## Overview
This document explains how to configure GitHub branch protection rules to block PR merges when the test workflow fails.


## Manual Setup (via GitHub Web Interface)

### Step 1: Navigate to Branch Protection Settings
1. Go to your repository on GitHub.com
2. Click on "Settings" tab
3. Click on "Branches" in the left sidebar
4. Click "Add rule" next to "Branch protection rules"

### Step 2: Configure Branch Protection Rule
Fill in the following settings:

**Branch name pattern:** `main`

**Protect matching branches:**
- ✅ Require a pull request before merging
  - ✅ Require approvals: 1
  - ✅ Dismiss stale reviews when new commits are pushed
  - ✅ Require review from code owners (if you have CODEOWNERS file)

- ✅ Require status checks to pass before merging
  - ✅ Require branches to be up to date before merging
  - **Required status checks:** Add these check names:
    - `Run Tests (3.9)`
    - `Run Tests (3.10.0)` 
    - `Run Tests (3.11)`
    - `Security Scan`
    - `PR Merge Validation`

- ✅ Require conversation resolution before merging

- ✅ Restrict pushes that create files to this branch
  - Choose "Restrict pushes that create files"

### Step 3: Save Protection Rule
Click "Create" to save the branch protection rule.

