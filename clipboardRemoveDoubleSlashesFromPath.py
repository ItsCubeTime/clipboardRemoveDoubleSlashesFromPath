import subprocess
import sys
try:
    import clipboard
except:
    def install(package):
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    install('clipboard')
    import clipboard
clipboard.copy(clipboard.paste().replace('\\', '/').replace('//', '/'))