import os
import shutil

def find_sqlmap_path():
    # Termux için özel olarak kontrol edilecek yerler
    termux_paths = [
        "/data/data/com.termux/files/usr/bin/sqlmap",  # Örnek bir yol
        "/data/data/com.termux/files/usr/bin/sqlmap.py",  # Örnek bir yol
    ]

    for path in termux_paths:
        if os.path.exists(path):
            return path

    # PATH ortam değişkeninde de sqlmap'in olabileceği yerler aranır
    paths = os.environ.get("PATH", "").split(":")
    for path in paths:
        sqlmap_path = os.path.join(path, "sqlmap")
        if os.path.exists(sqlmap_path):
            return sqlmap_path

    return None

def run_sqlmap():
    sqlmap_path = find_sqlmap_path()
    if sqlmap_path:
        os.system(f"python {sqlmap_path}")
    else:
        print("sqlmap bulunamadı.")

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
