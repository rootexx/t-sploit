import os

def run_sqlmap():
    sqlmap_path = r"C:\Users\velie\OneDrive\Masaüstü\t-sploit\sqlinj\sqlmap.py"
    os.system(f"python {sqlmap_path}")

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

if __name__ == "__main__":
    main()
