🔐 Auth Tests (Login & Register)

Ushbu loyiha login va register endpointlari uchun avtomatik testlarni o‘z ichiga oladi.
Testlar orqali foydalanuvchi autentifikatsiya jarayonlari to‘liq tekshiriladi.

🚀 Texnologiyalar

Python 3.12+

Pytest – test framework

Requests / httpx – API so‘rovlarini yuborish

Django REST Framework (backend misol sifatida)

📂 Strukturasi
tests/
 ├── test_register.py   # Ro‘yxatdan o‘tish testlari
 ├── test_login.py      # Login testlari
 └── conftest.py        # Umumiy fixture va sozlamalar

🧪 Test qamrovi
🔑 Register

✅ To‘g‘ri ma’lumot bilan muvaffaqiyatli ro‘yxatdan o‘tish

❌ Parollar mos kelmasa xato qaytarishi

❌ Username yoki email band bo‘lsa rad etilishi

✅ Foydalanuvchi yaratildimi tekshirish

🔓 Login

✅ To‘g‘ri login va parol bilan tizimga kirish

❌ Xato parol yoki username kiritilganda rad etilishi

✅ JWT / Token qaytarilishini tekshirish

⚡ Ishga tushirish

Virtual muhit yaratish va kerakli paketlarni o‘rnatish:

pip install -r requirements.txt


Testlarni ishga tushirish:

pytest -v


Muayyan testni ishlatish:

pytest tests/test_register.py::test_success_register

📊 Natija

Testlar yakunida pytest natijalarni ko‘rsatadi, masalan:

==================== 6 passed, 2 failed in 1.23s ====================
