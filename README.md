# 🔐 Authentication Tests (Login & Register)

Ushbu loyiha foydalanuvchilar uchun **Login** va **Register** jarayonlarini avtomatik test qilishga mo‘ljallangan.  
Testlar orqali autentifikatsiya jarayonlari to‘liq tekshiriladi va xatoliklar tezda aniqlanadi. 🚀

---

## 🛠 Texnologiyalar
- 🐍 Python 3.12+
- ⚡ Pytest – test framework
- 🌐 Requests / httpx – API so‘rovlarini yuborish
- 🏗 Django REST Framework (backend uchun)

---

## 📂 Loyiha strukturasi
tests/
├── test_register.py # Ro‘yxatdan o‘tish testlari
├── test_login.py # Login testlari
└── conftest.py # Umumiy fixture va sozlamalar

---

## 🧪 Test qamrovi
### 📝 Register
- ✅ To‘g‘ri ma’lumot bilan muvaffaqiyatli ro‘yxatdan o‘tish  
- ❌ Parollar mos kelmaganda xato chiqishi  
- ❌ Username yoki email band bo‘lsa rad etilishi  
- ✅ Foydalanuvchi yaratildimi tekshirish  

### 🔑 Login
- ✅ To‘g‘ri login va parol bilan tizimga kirish  
- ❌ Noto‘g‘ri parol yoki username kiritilganda rad etilishi  
- ✅ JWT / Token qaytarilishini tekshirish  

---

## ⚡ Ishga tushirish
1️⃣ Kerakli kutubxonalarni o‘rnatish:
```bash
pip install -r requirements.txt
pytest -v
==================== 6 passed, 2 failed in 1.23s ====================
