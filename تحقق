import ctypes

def is_cd_tray_open():
    try:
        # تخزين حالة الـ CD-ROM في متغير
        status = ctypes.create_unicode_buffer(128)
        ctypes.windll.WINMM.mciSendStringW("status cdaudio mode", status, 128, None)
        
        # التحقق من الحالة
        if "open" in status.value:
            print("علبة الـ CD-ROM مفتوحة.")
            return True
        else:
            print("علبة الـ CD-ROM مغلقة.")
            return False
    except Exception as e:
        print(f"حدث خطأ: {e}")
        return None

# استدعاء الدالة
is_cd_tray_open()
