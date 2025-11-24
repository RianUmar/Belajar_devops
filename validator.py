# validator.py

def cek_password(password):
    if len(password) < 8:
        return "Lemah"
    
    # Cek apakah ada angka di dalam password
    # any() akan return True jika ada minimal satu digit
    has_digit = any(char.isdigit() for char in password)
    
    if not has_digit:
        return "Sedang"
    
    return "Kuat"

if __name__ == "__main__":
    # Contoh penggunaan manual
    print(cek_password("rahasia"))      # Harusnya Sedang
    print(cek_password("rahasia123"))   # Harusnya Kuat