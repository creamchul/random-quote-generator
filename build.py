import PyInstaller.__main__
import os

# 현재 디렉토리 경로
current_dir = os.path.dirname(os.path.abspath(__file__))

PyInstaller.__main__.run([
    'app.py',
    '--name=랜덤명언생성기',
    '--onefile',
    '--windowed',
    '--add-data=quotes_data.json;.',
    '--icon=icon.ico',  # 아이콘 파일이 있다면 추가
    '--clean',
    '--noconfirm',
    f'--workpath={os.path.join(current_dir, "build")}',
    f'--distpath={os.path.join(current_dir, "dist")}',
]) 