from pydantic import BaseModel, EmailStr
from typing import Literal


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class ProductCreate(BaseModel):
    name: str
    product_type: Literal["stock", "affiliate", "digital"]
    price: float
    status: Literal["active", "inactive", "draft"] = "draft"
    stock_qty: int = 0


class ProductOut(ProductCreate):
    id: int

    class Config:
        from_attributes = True


class OrderStatusUpdate(BaseModel):
    order_status: Literal["pending_processing", "partially_ready", "ready", "completed", "cancelled"]
    payment_status: Literal["unpaid", "partially_paid", "paid", "refunded"]


class ThemeSettings(BaseModel):
    primary_color: str
    background_color: str
    text_color: str


class CustomerOut(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    phone: str
    city: str
    is_active: bool

    class Config:
        from_attributes = True


class ShippingRateCreate(BaseModel):
    country: str = "Egypt"
    governorate: str
    city: str = ""
    fee: float
    is_active: bool = True


class ShippingRateOut(ShippingRateCreate):
    id: int

    class Config:
        from_attributes = True


class CouponCreate(BaseModel):
    code: str
    discount_type: Literal["percentage", "fixed"]
    discount_value: float
    min_order_total: float = 0
    max_uses: int = 0
    status: Literal["active", "inactive", "scheduled"] = "active"


class CouponUpdate(BaseModel):
    discount_type: Literal["percentage", "fixed"]
    discount_value: float
    min_order_total: float
    max_uses: int
    status: Literal["active", "inactive", "scheduled"]


class CouponOut(CouponCreate):
    id: int
    used_count: int

    class Config:
        from_attributes = True
