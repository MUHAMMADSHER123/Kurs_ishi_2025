# Python Kod Tahrirlagichi

Bu loyiha veb-brauzer orqali Python kodlarini yozish va ishga tushirish imkonini beruvchi oddiy va qulay veb-ilovadir.

## Asosiy Xususiyatlar

- **Qulay interfeys** - Zamonaviy va foydalanuvchiga qulay interfeys
- **Tezkor ishlash** - Kodlarni tezda ishga tushirish imkoniyati
- **Xatolarni aniqlash** - Koddagi xatolarni tushunarli tarzda ko'rsatish
- **Tekshirish imkoniyati** - Kod natijalarini darhol ko'rish imkoniyati
- **Responsiv dizayn** - Har qanday qurilmalarda ishlaydi

## O'rnatish

1. Dastlab, loyihani klonlang yoki yuklab oling:
   ```
   git clone [loyiha-manzili]
   ```

2. Loyiha papkasiga o'ting:
   ```
   cd kurs-ishi
   ```

3. Kerakli paketlarni o'rnating:
   ```
   pip install -r requirements.txt
   ```

4. Ma'lumotlar bazasini yangilang:
   ```
   python manage.py migrate
   ```

5. Superfoydalanuvchi yarating (agar kerak bo'lsa):
   ```
   python manage.py createsuperuser
   ```

## Ishga tushirish

Loyihani ishga tushirish uchun quyidagi buyruqni ishga tushiring:

```
python manage.py runserver
```

So'ngra brauzeringizda quyidagi manzilni oching:
```
http://127.0.0.1:8000/
```

## Foydalanish qo'llanmasi

1. **Kod yozish** - Asosiy oynaga Python kodlaringizni yozing
2. **Ishga tushirish** - "Kodni Ishga Tushirish" tugmasini bosing yoki `Ctrl+Enter` tugmalarini bosing
3. **Natijani ko'rish** - Pastki oynada kod natijasini ko'ring
4. **Tozalash** - "Tozalash" tugmasi orqali chiqish oynasini tozalang

## Klaviatura qisqartmalari

- `Ctrl+Enter` - Kodni ishga tushirish
- `Tab` - Kodga bo'sh joy qo'shish
- `Shift+Enter` - Yangi qatorga o'tish

## Xavfsizlik

- Tizimda xavfsizlik choralari ko'rilgan
- Xavfli importlar (os, sys, subprocess) bloklangan
- Foydalanuvchi kodi maxsus muhitda ishlaydi

## Muallif

[Ismingiz]

## Litsenziya

Bu loyiha [MIT litsenziyasi](https://opensource.org/licenses/MIT) ostida taqdim etilgan.
