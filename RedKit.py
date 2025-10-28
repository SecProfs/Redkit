import os
import sys
import subprocess
from time import sleep
from colorama import init, Fore, Style
import pyfiglet

init(autoreset=True)

TOOLS_DATA = {
    "Information Gathering": [
        {"name": "AstraNmap", "desc_ar": "أداة ماسح أمني لاكتشاف الأجهزة والخدمات على الشبكة.", "desc_en": "A security scanner used to find hosts and services on a computer network.", "url": "https://github.com/Gameye98/AstraNmap"},
        {"name": "EvilURL", "desc_ar": "أداة توليد أسماء نطاقات متشابهة لهجمات التصيد الاحتيالي.", "desc_en": "Generates look-alike URLs using Unicode characters for phishing awareness and testing.", "url": "https://github.com/UndeadSec/EvilURL.git"},
        {"name": "OSIF", "desc_ar": "أداة تحليل طيفي كهربائي لأبحاث الخلايا الوقودية.", "desc_en": "Scientific tool for analyzing electrochemical impedance spectroscopy data.", "url": "https://github.com/ciku370/OSIF"},
        {"name": "Easymap", "desc_ar": "برنامج رسومي لتحليل بيانات الجينوم بسرعة وسهولة.", "desc_en": "User-friendly software for rapid mapping-by-sequencing of genomic data.", "url": "http://genetics.edu.umh.es/resources/easymap/"},
        {"name": "Weeman", "desc_ar": "إطار عمل تصيد احتيالي لتجربة سرقة بيانات الاعتماد.", "desc_en": "Phishing framework running fake web server to capture credentials.", "url": "https://github.com/evait-security/weeman"},
        {"name": "MaxSubdoFinder", "desc_ar": "أداة لاكتشاف النطاقات الفرعية.", "desc_en": "Tool to find subdomains for reconnaissance.", "url": "https://github.com/exlinee/MaxSubdoFinder"},
        {"name": "Trape", "desc_ar": "أداة OSINT للتحليل والتتبع الاجتماعي الذكي.", "desc_en": "OSINT tool for real-time tracking and social engineering attacks.", "url": "https://github.com/jofpin/trape.git"},
        {"name": "Red Hawk", "desc_ar": "ماسح ويب شامل لاكتشاف المعلومات ونقاط الضعف.", "desc_en": "All-in-one web scanner for information and vulnerability gathering.", "url": "https://github.com/Tuhinshubhra/RED_HAWK"},
        {"name": "LittleBrother", "desc_ar": "أداة تحليل وجمع معلومات عن الشبكات الاجتماعية.", "desc_en": "Social media information gathering and analysis tool.", "url": "https://github.com/Lulz3xploit/LittleBrother"},
        {"name": "Seeker", "desc_ar": "إطار تصيد يستهدف بيانات الهاتف المحمول عبر المتصفح.", "desc_en": "Phishing framework targeting mobile info via browser.", "url": "https://github.com/thewhiteh4t/seeker.git"},
        {"name": "ReconDog", "desc_ar": "أداة مسح مبسطة لجمع المعلومات عن الشبكات.", "desc_en": "Simple reconnaissance tool for info gathering.", "url": "https://github.com/s0md3v/ReconDog"},
        {"name": "D-Tech", "desc_ar": "أداة تقارير أمنية لجمع وتحليل المعلومات.", "desc_en": "Intelligence gathering and reporting tool.", "url": "https://github.com/bibortone/D-Tech"},
        {"name": "IpHack", "desc_ar": "أداة تقييم أمان الشبكات عبر فحص IP.", "desc_en": "Network and IP security assessment tool.", "url": "https://github.com/mishakorzik/IpHack"},
        {"name": "Nikto", "desc_ar": "ماسح خوادم ويب لاكتشاف الثغرات.", "desc_en": "Web server scanner for known vulnerabilities.", "url": "https://github.com/sullo/nikto"},
        {"name": "iSMTP", "desc_ar": "أداة إرسال البريد عبر بروتوكول SMTP.", "desc_en": "Python script to send emails via SMTP.", "url": "https://raw.githubusercontent.com/crunchsec/ismtp/master/ismtp.py"},
    ],
    "Exploitation Tools": [
        {"name": "RouterSploit", "desc_ar": "أداة استغلال ثغرات أجهزة الراوتر.", "desc_en": "Framework to exploit vulnerabilities in routers.", "url": "https://www.github.com/threat9/routersploit"},
        {"name": "Commix", "desc_ar": "أداة لاختبار ثغرات حقن الأوامر.", "desc_en": "Automated tool for testing command injection vulnerabilities.", "url": "https://github.com/commixproject/commix.git"},
        {"name": "TxTool", "desc_ar": "أداة متعددة الاستغلالات.", "desc_en": "Multi-purpose exploitation tool.", "url": "https://github.com/kuburan/txtool.git"},
        {"name": "XAttacker", "desc_ar": "أداة تنفيذ هجمات متقدمة.", "desc_en": "Advanced attack execution tool.", "url": "https://github.com/Moham3dRiahi/XAttacker.git"},
        {"name": "Fim", "desc_ar": "أداة لاختبار واختراق.", "desc_en": "Tool for testing and exploitation.", "url": "https://github.com/karjok/fim"},
    ],
    "Sniffing and Spoofing": [
        {"name": "Hack-Gmail", "desc_ar": "أداة لاستهداف حسابات Gmail.", "desc_en": "Tool targeting Gmail accounts.", "url": "https://github.com/d4az/hack-gmail.git"},
        {"name": "KnockMail", "desc_ar": "أداة لفحص البريد الإلكتروني.", "desc_en": "Email scanning and sniffing tool.", "url": "https://github.com/4w4k3/KnockMail.git"},
        {"name": "PwnedOrNot", "desc_ar": "فحص إذا ما تم تسريب بيانات.", "desc_en": "Check if data has been leaked.", "url": "https://github.com/thewhiteh4t/pwnedOrNot.git"},
        {"name": "EmailPySpam", "desc_ar": "إرسال رسائل مزعجة.", "desc_en": "Email spamming tool.", "url": "https://github.com/Curioo/emailpyspam.git"},
        {"name": "Gmail-Hack", "desc_ar": "أداة لاختراق جيميل.", "desc_en": "Gmail hacking tool.", "url": "https://github.com/mishakorzik/Gmail-Hack"},
        {"name": "Email-Spammer", "desc_ar": "أداة لإرسال البريد المزعج.", "desc_en": "Email spammer.", "url": "https://github.com/mishakorzik/Email-Spammer"},
    ],
    "Web Attack Tools": [
        {"name": "AdminHack", "desc_ar": "أداة اختراق صفحات الإدارة.", "desc_en": "Admin panel hacking tool.", "url": "https://github.com/mishakorzik/AdminHack"},
        {"name": "TakeOver", "desc_ar": "أداة للاستحواذ على النطاقات.", "desc_en": "Subdomain takeover tool.", "url": "https://github.com/m4ll0k/takeover.git"},
        {"name": "Blazy", "desc_ar": "أداة اختبار أمان تطبيقات الويب.", "desc_en": "Web vulnerability scanner.", "url": "https://github.com/UltimateHackers/Blazy"},
        {"name": "SqlMap", "desc_ar": "أداة اختبار حقن SQL.", "desc_en": "Automatic SQL injection tool.", "url": "https://github.com/sqlmapproject/sqlmap.git"},
        {"name": "WebSploit", "desc_ar": "إطار عمل لهجمات الويب.", "desc_en": "Web attack framework.", "url": "https://github.com/websploit/websploit.git"},
        {"name": "SH33LL", "desc_ar": "أداة الوصول للويب عبر الshell.", "desc_en": "Web shell tool.", "url": "https://github.com/LOoLzeC/SH33LL"},
        {"name": "SqlMate", "desc_ar": "أداة اختراق قواعد البيانات.", "desc_en": "SQL exploitation tool.", "url": "https://github.com/s0md3v/sqlmate"},
        {"name": "PyDDoser", "desc_ar": "أداة هجمات حجب الخدمة.", "desc_en": "DDOS attack tool.", "url": "https://github.com/mishakorzik/py-ddoser"},
        {"name": "Ultra-DDos", "desc_ar": "أداة هجوم حجب الخدمة المتطورة.", "desc_en": "Advanced DDOS tool.", "url": "https://github.com/mishakorzik/Ultra-DDos"},
        {"name": "WhatWeb", "desc_ar": "أداة فحص مواقع الويب.", "desc_en": "Website fingerprinting tool.", "url": "https://github.com/urbanadventurer/WhatWeb"},
        {"name": "Wfuzz", "desc_ar": "أداة لفحص ثغرات الويب.", "desc_en": "Web application brute forcing tool.", "url": "https://github.com/xmendez/wfuzz"},
    ],
    "Cam Hacking Tools": [
        {"name": "Cam-Hackers", "desc_ar": "أداة اختراق كاميرات.", "desc_en": "Camera hacking tool.", "url": "https://github.com/AngelSecurityTeam/Cam-Hackers"},
        {"name": "Grabcam", "desc_ar": "أداة لالتقاط صور عبر الكاميرا.", "desc_en": "Tool to grab camera images.", "url": "https://github.com/noob-hackers/grabcam"},
        {"name": "CamHack", "desc_ar": "أداة اختراق كاميرات.", "desc_en": "Camera hacking tool.", "url": "https://github.com/Devil-Tigers/CamHack.git"},
    ],
    "Remote Trojan RAT": [
        {"name": "PyShell", "desc_ar": "حصان طروادة للتحكم عن بعد.", "desc_en": "Remote Trojan for control.", "url": "https://github.com/knassar702/pyshell"},
        {"name": "WishFish", "desc_ar": "أداة RAT للتحكم عن بعد.", "desc_en": "Remote Access Trojan tool.", "url": "https://github.com/kinghacker0/WishFish"},
    ],
    "SQL Injection Tools": [
        {"name": "Debinject", "desc_ar": "أداة حقن SQL.", "desc_en": "SQL injection tool.", "url": "https://github.com/UndeadSec/Debinject.git"},
        {"name": "Vitus2.0", "desc_ar": "أداة اختبار حقن SQL.", "desc_en": "SQL injection testing tool.", "url": "https://github.com/Terror696/Vitus2.0"},
        {"name": "Infect", "desc_ar": "أداة تنفيذ هجمات SQL.", "desc_en": "SQL attack tool.", "url": "https://github.com/mishakorzik/Infect"},
    ],
    "SocialMedia Bruteforce": [
        {"name": "Facebook-BruteForce", "desc_ar": "هجوم القوة لكسر حسابات فيسبوك.", "desc_en": "Facebook brute force attack tool.", "url": "https://github.com/IAmBlackHacker/Facebook-BruteForce"},
        {"name": "Sherlock", "desc_ar": "أداة البحث عن الحسابات الاجتماعية.", "desc_en": "Social media username finder.", "url": "https://github.com/sherlock-project/sherlock.git"},
        {"name": "UserFinder", "desc_ar": "أداة للعثور على حسابات المستخدمين.", "desc_en": "Tool to find user accounts.", "url": "https://github.com/mishakorzik/UserFinder"},
    ],
    "SMS spaming tools": [
        {"name": "SMS-Bomber-300-Free", "desc_ar": "أداة إرسال رسائل عشوائية SMS.", "desc_en": "SMS spammer tool.", "url": "https://github.com/3UMOBKA/SMS-Bomber-300-Free"},
        {"name": "AresBomb", "desc_ar": "أداة إرسال رسائل SMS بشكل مزعج.", "desc_en": "SMS bombing tool.", "url": "https://github.com/MaksPV/AresBomb"},
        {"name": "Anon-SMS", "desc_ar": "أداة إرسال رسائل مجهولة.", "desc_en": "Anonymous SMS sender.", "url": "https://github.com/HACK3RY2J/Anon-SMS.git"},
        {"name": "Spymer", "desc_ar": "أداة إرسال رسائل مزعجة.", "desc_en": "Spam SMS sender.", "url": "https://github.com/FSystem88/spymer"},
        {"name": "TBomb", "desc_ar": "أداة إطلاق هجمات SMS.", "desc_en": "SMS bombing tool.", "url": "https://github.com/TheSpeedX/TBomb.git"},
        {"name": "anonymousSMS", "desc_ar": "أداة إرسال SMS مجهولة.", "desc_en": "Anonymous SMS and calls.", "url": "https://github.com/mishakorzik/anonymousSMS"},
    ],
    "Vulnerability Analysis": [
        {"name": "Rang3r", "desc_ar": "أداة تحليل الثغرات الأمنية.", "desc_en": "Vulnerability analysis tool.", "url": "https://github.com/floriankunushevci/rang3r"},
        {"name": "TM-Scanner", "desc_ar": "ماسح ثغرات أمنية.", "desc_en": "Scanner for vulnerabilities.", "url": "https://github.com/TechnicalMujeeb/TM-scanner.git"},
        {"name": "AstraNmap", "desc_ar": "ماسح أمني للكشف عن الأجهزة والخدمات.", "desc_en": "Security scanner for hosts and services.", "url": "https://github.com/Gameye98/AstraNmap"},
    ],
    "DarkSearch Tools": [
        {"name": "DarkDump", "desc_ar": "أداة بحث في الدارك ويب.", "desc_en": "Dark web search tool.", "url": "https://github.com/josh0xA/darkdump"},
    ],
    "Phishing And IpHack": [
        {"name": "Zphisher", "desc_ar": "أداة تصيد احتيالي.", "desc_en": "Phishing tool.", "url": "https://github.com/htr-tech/zphisher.git"},
        {"name": "ShellPhish", "desc_ar": "أداة هجمات التصيد.", "desc_en": "Phishing attack tool.", "url": "https://github.com/AbirHasan2005/ShellPhish"},
        {"name": "Saycheese", "desc_ar": "أداة تصوير كاميرا الضحية.", "desc_en": "Victim camera snapper.", "url": "https://github.com/hangetzzu/saycheese"},
        {"name": "Mask-Phish", "desc_ar": "أداة هجمات تصيد متقدمة.", "desc_en": "Advanced phishing tool.", "url": "https://github.com/mishakorzik/Mask-Phish.Termux"},
        {"name": "Seeker", "desc_ar": "أداة تصيد الاحتيالي لجوال الضحايا.", "desc_en": "Phishing targeting mobile data.", "url": "https://github.com/thewhiteh4t/seeker.git"},
        {"name": "AIOPhish", "desc_ar": "أداة تصيد شاملة.", "desc_en": "All-in-one phishing tool.", "url": "https://github.com/DeepSociety/AIOPhish"},
        {"name": "I See You", "desc_ar": "أداة تصيد مجهولة.", "desc_en": "Anonymous phishing tool.", "url": "https://github.com/Viralmaniar/I-See-You.git"},
        {"name": "HiddenEye", "desc_ar": "أداة تصيد متطورة.", "desc_en": "Advanced phishing tool.", "url": "https://github.com/DarkSecDevelopers/HiddenEye-Legacy"},
        {"name": "BlackEye", "desc_ar": "أداة تصيد بواجهات متعددة.", "desc_en": "Multi-interface phishing tool.", "url": "https://github.com/An0nUD4Y/blackeye"},
        {"name": "NPhish", "desc_ar": "أداة تصيد متنوعة.", "desc_en": "Diverse phishing tool.", "url": "https://github.com/Nishant2009/NPhish/"},
    ],
    "Hash cracking Tools": [
        {"name": "Hasher", "desc_ar": "أداة فك تشفير الهاشات.", "desc_en": "Hash cracking tool.", "url": "https://github.com/ciku370/hasher"},
        {"name": "HasherDoid", "desc_ar": "أداة لفك تشفير الهاش للهواتف.", "desc_en": "Mobile hash cracker.", "url": "https://github.com/thamahaxor/hasherdoid"},
        {"name": "Hash Generator", "desc_ar": "مولد هاشات لأغراض التشفير.", "desc_en": "Hash generation tool.", "url": "https://github.com/ciku370/hash-generator"},
        {"name": "Hash Buster", "desc_ar": "أداة لفك هاشات مختلفة.", "desc_en": "Multiple hash cracking tool.", "url": "https://github.com/s0md3v/Hash-Buster"},
    ],
    "Wordlist generator Tools": [
        {"name": "WlCreator", "desc_ar": "مولد قوائم كلمات.", "desc_en": "Wordlist generator.", "url": "https://github.com/Keshav2136/wlcreator"},
        {"name": "GoblinWordGenerator", "desc_ar": "مولد قوائم كلمات متقدم.", "desc_en": "Advanced wordlist creator.", "url": "https://github.com/UndeadSec/GoblinWordGenerator.git"},
        {"name": "SMWYG-SHOW-ME-WHAT-You-Got", "desc_ar": "مولد قوائم كلمات مخصص.", "desc_en": "Custom wordlist generator.", "url": "https://github.com/Viralmaniar/SMWYG-Show-Me-What-You-Got.git"},
    ],
    "XSS Attack Tools": [
        {"name": "XSSCon", "desc_ar": "أداة هجمات XSS.", "desc_en": "XSS attack tool.", "url": "https://github.com/menkrep1337/XSSCon"},
        {"name": "XanXSS", "desc_ar": "أداة اختبار XSS.", "desc_en": "XSS vulnerability testing tool.", "url": "https://github.com/Ekultek/XanXSS"},
        {"name": "XSStrike", "desc_ar": "أداة هجمات و اختبار XSS ذكية.", "desc_en": "Advanced XSS detection tool.", "url": "https://github.com/s0md3v/XSStrike"},
    ]
}

SECTIONS = list(TOOLS_DATA.keys())

def is_installed(cmd):
    return subprocess.call(f"type {cmd}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0

def is_tool_installed(tool):
    tool_path = os.path.expanduser(f"~/tools/{tool['name']}")
    return os.path.isdir(tool_path)

def install_tool(tool, language):
    tool_path = os.path.expanduser(f"~/tools/{tool['name']}")
    if is_tool_installed(tool):
        print(Fore.GREEN + (f"{tool['name']} is already installed." if language == "en" else f"{tool['name']} مثبت بالفعل."))
        return True
    print(Fore.YELLOW + (f"Installing {tool['name']} ..." if language == "en" else f"جاري تثبيت {tool['name']} ..."))
    try:
        os.makedirs(os.path.dirname(tool_path), exist_ok=True)
        res = subprocess.call(f"git clone {tool['url']} {tool_path}", shell=True)
        if res == 0:
            print(Fore.GREEN + (f"{tool['name']} installed successfully." if language == "en" else f"تم تثبيت {tool['name']} بنجاح."))
            sleep(1)
            req_path = os.path.join(tool_path, "requirements.txt")
            if os.path.isfile(req_path):
                check_and_install_python_requirements(req_path, language)
            return True
        else:
            print(Fore.RED + (f"Failed to install {tool['name']}." if language == "en" else f"فشل تثبيت {tool['name']}."))
            sleep(2)
            return False
    except Exception as e:
        print(Fore.RED + str(e))
        return False

def check_and_install_python_requirements(req_path, language):
    import pkg_resources
    try:
        with open(req_path) as file:
            requirements = file.read().strip().split('\n')
        installed = {pkg.key for pkg in pkg_resources.working_set}
        missing_pkgs = [pkg for pkg in requirements if pkg.lower() not in installed]
        if missing_pkgs:
            msg = ("Missing Python packages:\n" + ", ".join(missing_pkgs) + "\nInstall now? (y/n): ") if language == "en" else \
                  ("الحزم التالية غير مثبتة:\n" + ", ".join(missing_pkgs) + "\nهل تريد تثبيتها الآن؟ (y/n): ")
            install = input(Fore.CYAN + msg).strip().lower()
            if install == 'y':
                subprocess.call(f"pip3 install -r {req_path}", shell=True)
                print(Fore.GREEN + ("Dependencies installed.\n" if language == "en" else "تم تثبيت الحزم اللازمة.\n"))
                sleep(2)
            else:
                print(Fore.YELLOW + ("Some features may not work without dependencies." if language == "en" else "بعض المزايا قد لا تعمل بدون تثبيت الحزم."))
                sleep(2)
        else:
            print(Fore.GREEN + ("All Python dependencies are installed." if language == "en" else "جميع الحزم مثبتة."))
            sleep(1)
    except Exception as e:
        print(Fore.RED + str(e))
        sleep(2)

def run_tool(tool, language):
    tool_path = os.path.expanduser(f"~/tools/{tool['name']}")
    if not is_tool_installed(tool):
        print(Fore.RED + (f"{tool['name']} is not installed." if language == "en" else f"{tool['name']} غير مثبتة."))
        sleep(1)
        return
    print(Fore.CYAN + (f"Running {tool['name']}..." if language == "en" else f"تشغيل {tool['name']}..."))
    script_names = ["astranmap.sh", "install.sh", "run.sh", "start.sh"]
    for script in script_names:
        script_path = os.path.join(tool_path, script)
        if os.path.isfile(script_path):
            print(Fore.YELLOW + (f"Executing {script}..." if language == "en" else f"تشغيل {script}..."))
            subprocess.call(f"cd {tool_path} && bash {script}", shell=True)
            input(Fore.YELLOW + (f"Press Enter to return..." if language == "en" else "اضغط Enter للعودة..."))
            return
    py_files = [f for f in os.listdir(tool_path) if f.endswith(".py")]
    if py_files:
        main_py = py_files[0]
        print(Fore.YELLOW + (f"Running python script {main_py}..." if language == "en" else f"تشغيل سكربت بايثون {main_py}..."))
        subprocess.call(f"cd {tool_path} && python3 {main_py}", shell=True)
        input(Fore.YELLOW + (f"Press Enter to return..." if language == "en" else "اضغط Enter للعودة..."))
        return
    print(Fore.YELLOW + (f"No runnable script found. Opening directory..." if language == "en" else "لم يتم العثور على ملف للتشغيل. تم فتح المجلد..."))
    if sys.platform.startswith('linux'):
        subprocess.call(f"gnome-terminal -- bash -c 'cd {tool_path}; exec bash'", shell=True)
    elif sys.platform == 'darwin':
        subprocess.call(f"open -a Terminal {tool_path}", shell=True)
    elif sys.platform == 'win32':
        subprocess.call(f"start cmd /K cd {tool_path}", shell=True)
    else:
        print(Fore.RED + (f"Opening directory is not supported on this OS." if language == "en" else "فتح المجلد غير مدعوم على هذا النظام."))
    input(Fore.YELLOW + (f"Press Enter to return..." if language == "en" else "اضغط Enter للعودة..."))

def splash_screen(language):
    os.system('clear')
    ascii_art = pyfiglet.figlet_format("REDKIT", font="slant")
    print(Fore.RED + ascii_art)
    author_line = "By MASA | Version v1" if language == "en" else "بواسطة MASA | الاصدار v1"
    welcome_line = "Welcome to REDKIT Advanced Tool" if language == "en" else "مرحبا بكم في أداة REDKIT المتقدمة"
    print(Fore.YELLOW + author_line.center(70))
    print(Fore.GREEN + welcome_line.center(70))
    sleep(2)
    os.system('clear')

def choose_language():
    while True:
        os.system('clear')
        print(Fore.MAGENTA + pyfiglet.figlet_format("REDKIT", font="standard"))
        print("1 - English\n2 - العربية")
        choice = input(Fore.CYAN + "Choose Language / اختر اللغة: ").strip()
        if choice == "1":
            return "en"
        elif choice == "2":
            return "ar"
        else:
            print(Fore.RED + "Invalid choice! / اختيار غير صحيح!")
            sleep(1)

def check_essentials(language):
    essentials = [
        {"cmd": "python3", "name_en": "Python 3", "name_ar": "بايثون 3", "check_cmd": "python3 --version"},
        {"cmd": "git", "name_en": "Git", "name_ar": "Git", "check_cmd": "git --version"}
    ]
    print(Fore.BLUE + ("\nChecking essential programs...\n" if language == "en" else "\nجاري فحص البرامج الأساسية...\n"))
    to_install = []
    for item in essentials:
        installed = is_installed(item["cmd"])
        if not installed:
            name = item["name_ar"] if language == "ar" else item["name_en"]
            print(Fore.YELLOW + f"{name} - Not installed")
            to_install.append(item)
        else:
            try:
                ver = subprocess.check_output(item["check_cmd"], shell=True, stderr=subprocess.DEVNULL).decode().strip()
            except:
                ver = "Unknown version"
            name = item["name_ar"] if language == "ar" else item["name_en"]
            print(Fore.GREEN + f"{name} - Installed ({ver})")
    if to_install:
        prompt_install = ("Install missing essentials? (y/n): " if language == "en" else "تثبيت البرامج الناقصة؟ (y/n): ")
        choice = input(Fore.CYAN + prompt_install).strip().lower()
        if choice == "y":
            for item in to_install:
                name = item["name_ar"] if language == "ar" else item["name_en"]
                print(Fore.BLUE + (f"Installing {name}..." if language == "en" else f"جاري تثبيت {name}..."))
                if item["cmd"] == "git":
                    subprocess.call("sudo apt-get install git -y", shell=True)
                elif item["cmd"] == "python3":
                    subprocess.call("sudo apt-get install python3 python3-pip -y", shell=True)
            print(Fore.GREEN + ("Essentials installed.\n" if language == "en" else "تم تثبيت البرامج الأساسية.\n"))
            sleep(2)
        else:
            print(Fore.YELLOW + ("Skipping essentials installation.\n" if language == "en" else "تم تخطي تثبيت البرامج الأساسية.\n"))
            sleep(1)

def translate_section(section):
    translations = {
        "Information Gathering": "جمع المعلومات",
        "Exploitation Tools": "أدوات الاستغلال",
        "Sniffing and Spoofing": "التجسس والتزوير",
        "Web Attack Tools": "أدوات هجمات الويب",
        "Cam Hacking Tools": "أدوات اختراق الكاميرات",
        "Remote Trojan RAT": "أحصنة طروادة عن بعد",
        "SQL Injection Tools": "أدوات حقن قواعد البيانات",
        "SocialMedia Bruteforce": "هجمات القوة على وسائل التواصل",
        "SMS spaming tools": "أدوات إرسال رسائل مزعجة",
        "Vulnerability Analysis": "تحليل الثغرات",
        "DarkSearch Tools": "أدوات البحث في الدارك ويب",
        "Phishing And IpHack": "أدوات التصيد وIP Hack",
        "Hash cracking Tools": "أدوات فك تشفير الهاش",
        "Wordlist generator Tools": "مولد قوائم الكلمات",
        "XSS Attack Tools": "أدوات هجمات XSS",
    }
    return translations.get(section, section)

def section_tools_menu(language, section):
    tools = TOOLS_DATA.get(section, [])
    while True:
        os.system('clear')
        title = translate_section(section) if language == "ar" else section
        print(Fore.GREEN + f"{title} - Tools".center(70))
        print("-" * 70)
        for i, tool in enumerate(tools, start=1):
            status = Fore.GREEN + " - installed" if is_tool_installed(tool) else Fore.RED + " - not installed"
            name = tool["name"]
            print(Fore.CYAN + f"{i}. {name}{status}")
        print(Fore.CYAN + "0. " + ("Back to main menu" if language == "en" else "العودة للقائمة الرئيسية"))
        print(Fore.RED + "99. " + ("Exit" if language == "en" else "خروج"))
        choice = input(Fore.YELLOW + ("> Enter choice: " if language == "en" else "> أدخل اختيار: ")).strip()
        if choice == "99":
            print(Fore.GREEN + ("Thank you for using REDKIT. Goodbye!" if language == "en" else "شكراً لاستخدامك ريدكيت. وداعاً!"))
            sleep(2)
            sys.exit(0)
        elif choice == "0":
            return
        elif choice.isdigit() and 1 <= int(choice) <= len(tools):
            tool_menu(language, tools[int(choice) - 1])
        else:
            print(Fore.RED + ("Invalid choice." if language == "en" else "اختيار غير صالح."))
            sleep(1)

def tool_menu(language, tool):
    while True:
        os.system('clear')
        name = tool["name"]
        desc = tool["desc_ar"] if language == "ar" else tool["desc_en"]
        print(Fore.MAGENTA + pyfiglet.figlet_format(name, font="small"))
        print(Fore.CYAN + desc + "\n")
        installed = is_tool_installed(tool)
        status = Fore.GREEN + "[Installed]" if installed else Fore.RED + "[Not Installed]"
        print(status)
        print(Fore.CYAN + "1. " + ("Install" if language == "en" else "تثبيت"))
        if installed:
            print(Fore.CYAN + "2. " + ("Run" if language == "en" else "تشغيل"))
        print(Fore.CYAN + "0. " + ("Back" if language == "en" else "رجوع"))
        choice = input(Fore.YELLOW + ("> Enter choice: " if language == "en" else "> أدخل اختيار: ")).strip()
        if choice == "0":
            return
        elif choice == "1":
            install_tool(tool, language)
            sleep(1)
        elif choice == "2" and installed:
            run_tool(tool, language)
        else:
            print(Fore.RED + ("Invalid choice." if language == "en" else "اختيار غير صالح."))
            sleep(1)

def about_page(language):
    os.system('clear')
    print(Fore.MAGENTA + pyfiglet.figlet_format("REDKIT"))
    if language == "ar":
        print(Fore.YELLOW + "أداة متكاملة لأمن المعلومات والاختراق")
        print(Fore.CYAN + "صاحب الأداة: MASA")
        print(Fore.CYAN + "الاصدار: v1")
        print(Fore.WHITE + "\nهذه الأداة تساعدك على تثبيت وتشغيل أدوات متعددة لأغراض أمن المعلومات.\n")
        print(Fore.YELLOW + "اضغط Enter للعودة ...")
    else:
        print(Fore.YELLOW + "All-in-one InfoSec and Hacking Tool")
        print(Fore.CYAN + "Author: MASA")
        print(Fore.CYAN + "Version: v1")
        print(Fore.WHITE + "\nThis tool helps you install and run multiple InfoSec tools.\n")
        print(Fore.YELLOW + "Press Enter to return ...")
    input()
    return

def main_menu(language):
    while True:
        os.system('clear')
        header = "REDKIT - Main Menu" if language == "en" else "ريدكيت - القائمة الرئيسية"
        print(Fore.RED + header.center(70))
        print("=" * 70)
        for i, section in enumerate(SECTIONS, start=1):
            sect_name = section if language == "en" else translate_section(section)
            print(Fore.CYAN + f"{i}. {sect_name}")
        print(Fore.CYAN + "0. " + ("About / عن الأداة" if language == "en" else "حول الأداة"))
        print(Fore.CYAN + "99. " + ("Exit / خروج" if language == "en" else "خروج"))
        choice = input(Fore.YELLOW + ("> Enter choice: " if language == "en" else "> أدخل اختيار: ")).strip()
        if choice == "99":
            goodbye_text = "Thank you for using REDKIT. Goodbye!" if language == "en" else "شكراً لاستخدامك ريدكيت. وداعاً!"
            print(Fore.GREEN + goodbye_text)
            sleep(2)
            sys.exit(0)
        elif choice == "0":
            about_page(language)
        elif choice.isdigit() and 1 <= int(choice) <= len(SECTIONS):
            section_tools_menu(language, SECTIONS[int(choice) - 1])
        else:
            print(Fore.RED + ("Invalid choice." if language == "en" else "اختيار غير صالح."))
            sleep(1)

def run_redkit():
    language = choose_language()
    splash_screen(language)
    check_essentials(language)
    main_menu(language)

if __name__ == "__main__":
    try:
        run_redkit()
    except KeyboardInterrupt:
        print("\n" + Fore.RED + ("Exiting REDKIT." if sys.platform != "win32" else "Exiting REDKIT."))
        sys.exit(0)
