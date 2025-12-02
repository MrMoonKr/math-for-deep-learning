import subprocess
import sys


# python -m pip --version 명령어 실행 
result = subprocess.run( 
    [sys.executable, "-m", "pip", "--version"],
    capture_output=True,
    text=True 
)

# 실행 결과 출력
print( result.stdout )

