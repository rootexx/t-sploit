import requests
import subprocess

# IP tespiti için fonksiyon
def get_website_ip(url):
    try:
        ip = socket.gethostbyname(url)
        print("Website IP: ", ip)
    except socket.gaierror:
        print("Geçersiz URL.")

# Admin paneli bulma için fonksiyon
def find_admin_panel(url):
    admin_panel_paths = ["admin", "login", "dashboard", "admin-panel"]
    
    for path in admin_panel_paths:
        admin_url = url + "/" + path
        response = requests.get(admin_url)
        if response.status_code == 200:
            print("Admin Panel URL: ", admin_url)
            break

# DDoS saldırısı için fonksiyon
def perform_ddos_attack():
    subprocess.call(["python3", "ddos.py"])

# Ana işlev
def main():
    print("[1] Website IP'sini bul")
    print("[2] Admin panelini bul")
    print("[3] DDoS saldırısı gerçekleştir")
    print("[Q] Çıkış")

    choice = input("Seçiminizi yapın: ")

    if choice == "1":
        url = input("Website URL'sini girin: ")
        get_website_ip(url)
    elif choice == "2":
        url = input("Website URL'sini girin: ")
        find_admin_panel(url)
    elif choice == "3":
        perform_ddos_attack()
    elif choice.lower() == "q":
        return
    else:
        print("Geçersiz bir seçim yaptınız. Tekrar deneyin.")

    main()

if __name__ == "__main__":
    main()
