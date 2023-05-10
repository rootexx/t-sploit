import os

def run_sqlmap():
    sqlmap_dir = os.path.join(os.path.dirname(__file__), "sqlinj")
    sqlmap_path = os.path.join(sqlmap_dir, "sqlmap.py")
    
    if os.path.exists(sqlmap_path):
        os.system(f"python {sqlmap_path}")
    else:
        print("sqlmap.py bulunamadı.")

# Ana işlev
def main():
    while True:
        print("[1] Website IP'sini bul")
        print("[2] Admin panelini bul")
        print("[3] DDoS saldırısı gerçekleştir")
        print("[4] SQL Injection")
        print("[Q] Çıkış")

        choice = input("Seçim yapın: ")

        if choice == "1":
            # Website IP'sini bulma işlemleri
            pass
        elif choice == "2":
            # Admin panelini bulma işlemleri
            pass
        elif choice == "3":
            # DDoS saldırısı gerçekleştirme işlemleri
            os.system("python3 ddos.py")
        elif choice == "4":
            run_sqlmap()  # SQL Injection işlemini çalıştır
        elif choice.lower() == "q":
            break
        else:
            print("Geçersiz bir seçim yaptınız. Tekrar deneyin.")
            continue  # Yanlış seçenek seçildiğinde döngünün başına dön ve ana menüyü tekrar aç

if __name__ == "__main__":
    main()
