import os

# IP tespiti için fonksiyon
def get_website_ip(url):
    # IP tespiti kodları
    pass

# Admin paneli bulma için fonksiyon
def find_admin_panel(url):
    # Admin paneli bulma kodları
    pass

# DDoS saldırısı için fonksiyon
def perform_ddos_attack(url):
    # DDoS saldırısı kodları
    os.system("python3 ddos.py")

# SQL injection için fonksiyon
def perform_sql_injection(url):
    # SQL injection kodları
    os.system("python3 sqlmap.py -u " + url)  # sqlmap.py dosyasını çalıştır

# Ana işlev
def main():
    while True:
        print("[1] Website IP'sini bul")
        print("[2] Admin panelini bul")
        print("[3] DDoS saldırısı gerçekleştir")
        print("[4] SQL injection gerçekleştir")
        print("[Q] Çıkış")

        choice = input("Seçim yapın: ")

        if choice == "1":
            url = input("Website URL'sini girin: ")
            get_website_ip(url)
        elif choice == "2":
            url = input("Website URL'sini girin: ")
            find_admin_panel(url)
        elif choice == "3":
            url = input("Lütfen Enter'a Basın ")
            perform_ddos_attack(url)
        elif choice == "4":
            url = input("Lütfen Enter'a Basın ")
            perform_sql_injection(url)
        elif choice.lower() == "q":
            break
        else:
            print("Geçersiz bir seçim yaptınız. Tekrar deneyin.")

if __name__ == "__main__":
    main()
