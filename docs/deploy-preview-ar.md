# نشر ومعاينة Admin API على GitHub + Preview

## مهم جدًا: لو ما عندك فولدر اسمه `Doserly`
اسم الريبو على GitHub **لا يفرض** اسم فولدر محلي ثابت.

- ممكن الريبو عندك يكون اسمه المحلي مثل: `my-store` أو `project` عادي جدًا.
- الفكرة الأساسية: تفتح **جذر الريبو المحلي** (المجلد الذي يحتوي `.git`) وتضع الملفات داخله بنفس المسارات.
- يعني مثلًا ملف الـ API لازم يكون داخل:
  - `apps/admin-api/main.py`
- وملف الـ CI داخل:
  - `.github/workflows/admin-api-ci.yml`

للتأكد أنك في المكان الصحيح:
```bash
pwd
git rev-parse --show-toplevel
```
لو الأمر الثاني رجّع نفس المسار، فأنت داخل الريبو الصحيح.

## 1) ارفع المشروع على GitHub
```bash
git remote add origin <YOUR_GITHUB_REPO_URL>
git push -u origin work
```

أو بشكل أسرع بأمر واحد:
```bash
bash scripts/github-sync.sh <YOUR_GITHUB_REPO_URL> work
```

## 2) تفعيل الاختبار التلقائي (CI)
تمت إضافة Workflow جاهز:
- `.github/workflows/admin-api-ci.yml`

عند كل Push/PR على `apps/admin-api` سيتم:
1. تثبيت المتطلبات
2. تشغيل `pytest -q`

## 3) نشر Preview سريع (Render)
1. ادخل Render → New Web Service → اربط GitHub repo.
2. اختر المسار: `apps/admin-api`.
3. Build Command:
   ```bash
   pip install -r requirements.txt
   ```
4. Start Command:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port $PORT
   ```
5. بعد النشر افتح:
   - `/api/admin/health`
   - `/docs`

## 4) اختبار ذاتي منك
- افتح Swagger من `/docs`
- نفذ `/api/admin/auth/login` ببيانات:
  - `admin@doserly.com`
  - `Admin@123`
- انسخ التوكن واعمل Authorize
- اختبر:
  - `POST /api/admin/shipping`
  - `POST /api/admin/discounts/coupons`
  - `GET /api/admin/analytics/overview`

## ملاحظة
قبل الإنتاج:
- غيّر `SECRET_KEY`
- غيّر بيانات الأدمن الافتراضي
- انقل DB من SQLite إلى MySQL/PostgreSQL
