#!/usr/bin/env bash

REPO="$HOME/Insync/kumarshan25@gmail.com/Google Drive/KumarsNotes"
LOG="$HOME/.git_sync_notes.log"

cd "$REPO" || exit 1

git pull --rebase >> "$LOG" 2>&1

if ! git diff --quiet || ! git diff --cached --quiet; then
    git add -A
    git commit -m "auto-sync $(date '+%Y-%m-%d %H:%M:%S')" >> "$LOG" 2>&1
    git push >> "$LOG" 2>&1
fi
