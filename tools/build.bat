@echo off
echo ===== �������� Python �ű����������б� =====
python build.py
if %errorlevel% neq 0 (
    echo ? Python �ű�ִ��ʧ�ܡ����� tools\build.py �Ƿ����﷨�����ȱʧ�ļ���
    pause
    exit /b %errorlevel%
)
echo ? Python �ű�ִ�гɹ�,����ɺϲ���

pause
