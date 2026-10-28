def tanya(pertanyaan):
    """Mengembalikan True jika jawaban 'ya', False jika 'tidak'."""
    jawab = input(f"{pertanyaan} (ya/tidak): ").strip().lower()
    if jawab == "ya":
        return True
    elif jawab == "tidak":
        return False
    else:
        print("Masukkan 'ya' atau 'tidak'.")
        return tanya(pertanyaan)


def pilih(pertanyaan, pilihan):
    """Menampilkan daftar pilihan dan mengembalikan pilihan yang dipilih."""
    print(pertanyaan)
    for i, opsi in enumerate(pilihan, start=1):
        print(f"  {i}. {opsi}")
    jawab = input("Pilih nomor: ").strip()
    if jawab.isdigit() and 1 <= int(jawab) <= len(pilihan):
        return pilihan[int(jawab) - 1]
    else:
        print(f"Masukkan angka 1 sampai {len(pilihan)}.")
        return pilih(pertanyaan, pilihan)


def langkah(teks):
    print(f"-> {teks}")


def tahap_santan():
    """Keputusan: apakah santan diperoleh?"""
    if tanya("Apakah santan diperoleh?"):
        langkah("Pemanasan santan (metode basah)")
    else:
        langkah("Pemarutan daging kelapa (ulang)")
        tahap_santan()


def tahap_pemisahan():
    """Keputusan: apakah minyak terpisah dari blondo?"""
    if tanya("Apakah minyak terpisah dari blondo?"):
        langkah("Penyaringan minyak")
    else:
        langkah("Lanjutkan pemanasan")
        tahap_pemisahan()


def uji_kualitas():
    """Uji warna, aroma, dan kejernihan. Mengembalikan True jika lolos."""
    print("\n--- Uji Kualitas ---")
    warna = pilih("Warna minyak:", ["putih kekuningan", "coklat"])
    aroma = pilih("Aroma minyak:", ["harum", "tidak harum"])
    jernih = tanya("Apakah minyak jernih?")

    print("\nHasil uji:")
    print(f"  Warna      : {warna}")
    print(f"  Aroma      : {aroma}")
    if jernih:
        print("  Kejernihan : jernih")
    else:
        print("  Kejernihan : tidak jernih")

    if warna == "putih kekuningan" and aroma == "harum" and jernih:
        print("  Status     : LOLOS\n")
        return True
    else:
        print("  Status     : TIDAK LOLOS\n")
        return False


def tahap_pengemasan():
    """Pengemasan lalu uji kualitas; jika tidak lolos, reproses."""
    langkah("Pengemasan ke botol steril")
    if uji_kualitas():
        langkah("Penyimpanan dan pendistribusian")
    else:
        langkah("Reproses")
        tahap_pengemasan()


def main():
    print("=== START ===")

    # Input
    langkah("Pemilihan kelapa tua")
    langkah("Pengupasan sabut dan pembelahan tempurung")
    langkah("Pemarutan daging kelapa")

    tahap_santan()      
    tahap_pemisahan()   

    print("--- lanjut ke bagian pengemasan ---")
    tahap_pengemasan()  

    print("=== END ===")


if __name__ == "__main__":
    main()
