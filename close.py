import ctypes

def close_cd_tray():
    try:
        # استدعاء دالة إغلاق علبة الـ CD-ROM
        ctypes.windll.WINMM.mciSendStringW("set cdaudio door closed", None, 0, None)
        print("تم إغلاق علبة الـ CD-ROM")
    except Exception as e:
        print(f"حدث خطأ: {e}")

# استدعاء الدالة
close_cd_tray()
