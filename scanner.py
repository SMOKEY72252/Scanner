import requests
import socket
import random

RED     = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
BLUE    = '\033[34m'
MAGENTA = '\033[35m'
CYAN    = '\033[36m'
WHITE   = '\033[37m'
RESET   = '\033[39m'

def gethip():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    print(hostname)
    print(IPAddr)
def uch():
    ld = '\033[1;32m'

print('''
\033[33m
 _____ _____  _____ _       _____ _   _ ______ _____ 
|_   _|  _  ||  _  | |     |_   _| \ | ||  ___|  _  |
\033[34m  | | | | | || | | | |       | | |  \| || |_  | | | |
  | | | | | || | | | |       | | | . ` ||  _| | | | |
\033[32m  | | \ \_/ /\ \_/ / |____  _| |_| |\  || |   \ \_/ /
  \_/  \___/  \___/\_____/  \___/\_| \_/\_|    \___/                                                                                                                                                                                             
                   tiktok  :   
       \033[33m                                                    
        ☆ https://ly.wicl.repl.co/ENrFFSQ ☆
\033[32m
                 telegram  :
  	 \033[33m
  	♡ https://t.me/Cyber218_group  ♡
  '\033[32m	
♤from tool_info♤
\033[36m
''')

def get_my_ip():
    response = requests.get('https://api64.ipify.org?format=json')
    ip_data = response.json()
    return ip_data['ip']

def get_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return "Unable to resolve domain name."

def get_location(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    data = response.json()
    
    if data["status"] == "success":
        lat = data["lat"]
        lon = data["lon"]
        maps_url = f"https://www.google.com/maps/search/?api=1&query={lat},{lon}"
        return maps_url
    else:
        return None

# الجزء الرئيسي للبرنامج
while True:
    print("1. MY IP")
    print('''
    
    ''')
    print("2. URL IP PAGE")
    print('''
    
    ''')
    print("3. ip scan")
    print('''
    
    ''')
    print("4. insta shic account")
    print('''
    
    ''')
    print("\033[31m5. exit")
    print('''
    
    ''')
    
    choice = input("\033[37mselect number: ")
    
    if choice == '1':
        my_ip = get_my_ip()
        print("your IP ADDRESS is:", my_ip)
        
    elif choice == '2':
        domain = input("url scan: ")
        ip_address = get_ip_address(domain)
        print("url name", domain, "هو:", ip_address)
        
    elif choice == '3':
        ip_address = input("enter the url you want to scan: ")
        location = get_location(ip_address)

        if location is not None:
            print("رابط الموقع:", location)
        else:
            print("تعذر العثور على الموقع لعنوان IP المحدد.")
            
    elif choice == '4':
        def check_user(username):
            url = f"https://www.instagram.com/{username}/?__a=1"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                user_id = data["graphql"]["user"]["id"]
                full_name = data["graphql"]["user"]["full_name"]
                followers = data["graphql"]["user"]["edge_followed_by"]["count"]
                following = data["graphql"]["user"]["edge_follow"]["count"]
                bio = data["graphql"]["user"]["biography"]
                is_private = data["graphql"]["user"]["is_private"]

                print(f"اسم المستخدم: {username}")
                print(f"المعرف: {user_id}")
                print(f"الاسم الكامل: {full_name}")
                print(f"المتابعون: {followers}")
                print(f"المتابعة: {following}")
                print(f"السيرة الذاتية: {bio}")
                if is_private:
                    print("هذا الحساب خاص")
                else:
                    print("هذا الحساب عام")
            else:
                print("لم يتم العثور على المستخدم")

        username = input("أدخل اسم مستخدم انستقرام: ")
        check_user(username)
        
    elif choice == '5':
        break
    else:
        print("الرجاء اختيار خيار صحيح.")