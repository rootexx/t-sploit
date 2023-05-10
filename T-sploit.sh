#!/bin/bash

run_sqlmap() {
    sqlmap_dir="$(dirname "$0")/sqlinj"
    sqlmap_path="$sqlmap_dir/sqlmap.py"
    
    if [ -f "$sqlmap_path" ]; then
        python "$sqlmap_path"
    else
        echo "sqlmap.py bulunamadı."
    fi
}

perform_ddos_attack() {
    # DDoS saldırısı kodları
    python ddos.py
}

# ANSI renk kodları
RED='\033[0;31m'
CYAN='\033[0;36m'
NC='\033[0m'

while true; do
    echo -e "${RED}[01]${NC} Website IP'sini bul"
    echo -e "${RED}[02]${NC} Admin panelini bul"
    echo -e "${RED}[03]${NC} DDoS saldırısı gerçekleştir"
    echo -e "${RED}[04]${NC} SQL Injection"
    echo -e "${RED}[Q]${NC} Çıkış"

    read -p "Seçim yapın: " choice

    if [ "$choice" = "01" ]; then
        # Website IP'sini bulma işlemleri
        :
    elif [ "$choice" = "02" ]; then
        # Admin panelini bulma işlemleri
        :
    elif [ "$choice" = "03" ]; then
        # DDoS saldırısı gerçekleştirme işlemleri
        perform_ddos_attack
        exit 0
    elif [ "$choice" = "04" ]; then
        run_sqlmap  # SQL Injection işlemini çalıştır
        exit 0
    elif [ "$choice" = "q" ] || [ "$choice" = "Q" ]; then
        exit 0
    else
        echo -e "${RED}Geçersiz bir seçim yaptınız. Tekrar deneyin.${NC}"
    fi
done
