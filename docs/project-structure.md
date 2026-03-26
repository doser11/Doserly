# Doserly - Suggested Phase 1 Project Structure

```text
Doserly/
├─ app/
│  ├─ Http/
│  │  ├─ Controllers/
│  │  │  ├─ Storefront/
│  │  │  ├─ Checkout/
│  │  │  └─ Admin/
│  │  ├─ Middleware/
│  │  └─ Requests/
│  ├─ Models/
│  ├─ Services/
│  │  ├─ Affiliate/
│  │  ├─ Payments/
│  │  ├─ Shipping/
│  │  ├─ Cashback/
│  │  └─ Notifications/
│  ├─ Jobs/
│  │  ├─ AbandonedCarts/
│  │  └─ Emails/
│  └─ Policies/
├─ bootstrap/
├─ config/
├─ database/
│  ├─ migrations/
│  │  └─ 001_initial_schema.sql
│  └─ seeders/
├─ docs/
│  └─ project-structure.md
├─ public/
├─ resources/
│  ├─ views/
│  ├─ js/
│  └─ css/
├─ routes/
│  ├─ web.php
│  ├─ api.php
│  └─ admin.php
├─ storage/
├─ tests/
│  ├─ Feature/
│  └─ Unit/
└─ README.md
```

## Domain modules (high level)
- **Auth & Accounts**: OTP + password + Google login, account/profile/addresses.
- **Catalog**: categories, products (stock/affiliate/digital), variants, SEO metadata.
- **Cart & Checkout**: active cart, abandoned cart reminders, shipping estimator, coupon support.
- **Orders**: partial readiness flow, payment statuses, order timeline logs.
- **Cashback**: wallet, ledger transactions, withdrawal workflow.
- **Admin Settings**: UI theme, SEO defaults, contact info, shipping city rates.
