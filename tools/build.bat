@echo off
echo ===== Pulling latest changes =====
git pull origin main
if %errorlevel% neq 0 (
    echo ❌ Git pull failed. Please check your network connection or remote repository.
    pause
    exit /b %errorlevel%
)

echo ===== Running Python script to build paper list =====
python tools\build.py
if %errorlevel% neq 0 (
    echo ❌ Python script failed. Please check tools\build.py for syntax errors or missing files.
    pause
    exit /b %errorlevel%
)

echo ===== Committing changes =====
git add ..\paper_list.md
git commit -m "Weekly auto-update of paper list"
if %errorlevel% neq 0 (
    echo ⚠️ Git commit may have failed (e.g., no changes to commit). Please check manually.
)

echo ===== Pushing to remote =====
git push origin main
if %errorlevel% neq 0 (
    echo ❌ Git push failed. Check your permissions or network status.
    pause
    exit /b %errorlevel%
)

echo ✅ All tasks completed successfully!
pause
