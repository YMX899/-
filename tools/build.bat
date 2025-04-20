@echo off
echo ===== 正在运行 Python 脚本生成论文列表 =====
python build.py
if %errorlevel% neq 0 (
    echo ? Python 脚本执行失败。请检查 tools\build.py 是否有语法错误或缺失文件。
    pause
    exit /b %errorlevel%
)
echo ? Python 脚本执行成功,已完成合并！

pause
