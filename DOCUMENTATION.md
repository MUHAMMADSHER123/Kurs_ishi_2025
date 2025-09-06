# Python Kod Tahrirlagichi - Foydalanish Qo'llanmasi

## Kirish
Ushbu dastur veb-brauzer orqali Python kodlarini yozish va ishga tushirish imkonini beruvchi qulay vositadir. U Django framework'ida yozilgan.

## O'rnatish

1. Python 3.8+ o'rnatilganligiga ishonch hosil qiling
2. Loyiha manbasini yuklab oling yoki klon qiling
3. Virtual muhit yarating va faollashtiring:
   ```
   python -m venv venv
   venv\Scripts\activate  # Windows uchun
   ```
4. Kerakli kutubxonalarni o'rnating:
   ```
   pip install -r requirements.txt
   ```
5. Ma'lumotlar bazasini yarating:
   ```
   python manage.py migrate
   ```
6. Superfoydalanuvchi yarating (agar kerak bo'lsa):
   ```
   python manage.py createsuperuser
   ```
7. Dasturni ishga tushiring:
   ```
   python manage.py runserver
   ```
8. Brauzeringizda oching: http://127.0.0.1:8000/

## Foydalanish

1. **Asosiy oyna** - kod yozish uchun maydon
2. **Kod yozish** - Python kodlarini yozing
3. **Ishga tushirish** - "Kodni Ishga Tushirish" tugmasi yoki `Ctrl+Enter`
4. **Natijani ko'rish** - Pastki oynada kod natijasini ko'ring
5. **Tozalash** - "Tozalash" tugmasi orqali chiqish oynasini tozalang

## Qo'llab-quvvatlanadigan modullar

Quyidagi standart Python modullari qo'llab-quvvatlanadi:

- `os` - Operatsion tizim bilan ishlash
- `sys` - Tizim parametrlari
- `math` - Matematik funksiyalar
- `random` - Tasodifiy sonlar
- `datetime` - Sana va vaqt
- `time` - Vaqt bilan ishlash
- `json` - JSON ma'lumotlar bilan ishlash
- `re` - Muntazam ifodalar
- `collections` - Qo'shimcha ma'lumot tuzilmalari
- `itertools` - Iteratorlar bilan ishlash
- `functools` - Funksiyalar bilan ishlash
- `operator` - Operatorlar
- `string` - Matnlar bilan ishlash
- `array` - Massivlar
- `struct` - Ikkilik ma'lumotlar bilan ishlash
- `copy` - Nusxalash
- `pprint` - Chiroyli chiqarish
- `typing` - Tur an'notatsiyalari

## Klaviatura qisqartmalari

- `Ctrl+Enter` - Kodni ishga tushirish
- `Tab` - 4 ta bo'sh joy qo'shish
- `Shift+Enter` - Yangi qatorga o'tish

## Xavfsizlik

Dasturda quyidagi xavfsizlik choralari mavjud:

1. Kod maxsus muhitda ishlaydi
2. Ba'zi xavfli operatsiyalar cheklangan
3. Har bir so'rov alohida ishlaydi

## Muammolarni bartaraf qilish

Agar kod ishlamasa:
1. Xatolik xabarini diqqat bilan o'qing
2. Kodni qayta tekshiring
3. Brauzer konsolida xatolik bormi tekshiring
4. Agar muammo davom etsa, dastur loglarini tekshiring

## Aloqa

Agar savol yoki taklifingiz bo'lsa, murojaat qilishingiz mumkin:
- Email: [sizning-email@example.com]
- Telegram: @sizning_username

## Litsenziya

Ushbu loyiha MIT litsenziyasi ostida tarqatilgan.
