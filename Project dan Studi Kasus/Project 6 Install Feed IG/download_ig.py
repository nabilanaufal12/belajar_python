import instaloader

# 1. Masukkan Username & Password IG Kamu
# (Wajib login karena targetnya akun Private)
MY_USERNAME = "username_ig_kamu" 
MY_PASSWORD = "password_ig_kamu"

# 2. Masukkan Link atau Shortcode Postingan Target
# Contoh link: https://www.instagram.com/p/Cfv4_xRv0/ -> Shortcodenya: Cfv4_xRv0
POST_SHORTCODE = "MASUKKAN_KODE_LINK_DISINI" 

def download_private_post():
    # Inisialisasi Instaloader
    L = instaloader.Instaloader(
        download_pictures=True,
        download_videos=False, # Ubah True jika mau video juga
        download_video_thumbnails=False,
        download_geotags=False,
        download_comments=False,
        save_metadata=False,
        compress_json=False
    )

    try:
        print(f"🔐 Mencoba login sebagai {MY_USERNAME}...")
        L.login(MY_USERNAME, MY_PASSWORD)
        print("✅ Login berhasil!")

        print(f"📥 Sedang mengambil data postingan: {POST_SHORTCODE}...")
        post = instaloader.Post.from_shortcode(L.context, POST_SHORTCODE)

        print("⬇️  Sedang mendownload...")
        L.download_post(post, target="hasil_download")
        
        print("\n🎉 Selesai! Cek folder 'hasil_download'.")

    except Exception as e:
        print(f"\n❌ Gagal: {e}")
        print("Tips: Pastikan username/password benar dan matikan 2FA sementara jika perlu.")

if __name__ == "__main__":
    download_private_post()