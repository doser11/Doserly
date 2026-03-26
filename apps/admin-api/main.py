from fastapi import FastAPI

from database import Base, SessionLocal, engine
from routers import analytics, auth, customers, discounts, orders, products, settings, shipping
from seed import seed_initial_data

app = FastAPI(title="Doserly Admin Manager API", version="1.2.0")


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        seed_initial_data(db)
    finally:
        db.close()


app.include_router(auth.router, prefix="/api/admin/auth", tags=["auth"])
app.include_router(products.router, prefix="/api/admin/products", tags=["products"])
app.include_router(orders.router, prefix="/api/admin/orders", tags=["orders"])
app.include_router(customers.router, prefix="/api/admin/customers", tags=["customers"])
app.include_router(settings.router, prefix="/api/admin/settings", tags=["settings"])
app.include_router(analytics.router, prefix="/api/admin/analytics", tags=["analytics"])
app.include_router(shipping.router, prefix="/api/admin/shipping", tags=["shipping"])
app.include_router(discounts.router, prefix="/api/admin/discounts", tags=["discounts"])


@app.get("/api/admin/health")
def health_check():
    return {
        "status": "ok",
        "service": "doserly-admin-manager",
        "version": "1.2.0",
        "default_admin": "admin@doserly.com",
    }
