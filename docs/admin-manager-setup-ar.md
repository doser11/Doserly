# Doserly Admin Manager - المرحلة التالية (مفعلة)

## الذي تم في هذه الخطوة
تم تنفيذ **الخطوة الجاية** بإضافة Modules جديدة مطلوبة للإدارة:

1. **إدارة الشحن (Shipping Rates CRUD)**
   - إضافة / عرض / تعديل / حذف أسعار الشحن حسب الدولة/المحافظة/المدينة.

2. **إدارة الخصومات (Coupons CRUD)**
   - إضافة / عرض / تعديل / حذف كوبونات الخصم.
   - منع تكرار الكود (Coupon Code) بإرجاع 409 عند التكرار.

3. **تحديث API الرئيسي**
   - إضافة راوترات `shipping` و `discounts` داخل التطبيق.
   - رفع نسخة الـ API إلى `1.2.0`.

4. **تحديث الاختبارات**
   - إضافة اختبارات أساسية لمسارات الشحن والخصومات.

## المسارات الجديدة
- `GET /api/admin/shipping`
- `POST /api/admin/shipping`
- `PUT /api/admin/shipping/{rate_id}`
- `DELETE /api/admin/shipping/{rate_id}`
- `GET /api/admin/discounts/coupons`
- `POST /api/admin/discounts/coupons`
- `PUT /api/admin/discounts/coupons/{coupon_id}`
- `DELETE /api/admin/discounts/coupons/{coupon_id}`

## الخطوة القادمة بعد هذه
- ربط `Shipping Rates` مع Checkout Calculator مباشرة.
- إضافة Special Offers (Buy X Get Y / Free Shipping Rule).
- استكمال CRUD للصفحات القانونية + Redirects + Reviews Moderation.
