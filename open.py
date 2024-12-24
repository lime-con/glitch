import ctypes

def open_cd_tray():
    try:
        # استدعاء دالة فتح علبة الـ CD-ROM
        ctypes.windll.WINMM.mciSendStringW("set cdaudio door open")
        print("تم فتح علبة الـ CD-ROM")
    except Exception as e:
        print(f"حدث خطأ: {e}")

# استدعاء الدالة
open_cd_tray()
