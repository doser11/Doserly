from fastapi import APIRouter, Depends
from sqlalchemy import func
from sqlalchemy.orm import Session

from database import get_db
from deps import get_current_admin
from models import Customer, Order, Product

router = APIRouter()


@router.get("/overview")
def analytics_overview(db: Session = Depends(get_db), _admin=Depends(get_current_admin)):
    orders_count = db.query(func.count(Order.id)).scalar() or 0
    sales_total = db.query(func.coalesce(func.sum(Order.grand_total), 0.0)).scalar() or 0.0
    products_count = db.query(func.count(Product.id)).scalar() or 0
    customers_count = db.query(func.count(Customer.id)).scalar() or 0
    average_order_value = (sales_total / orders_count) if orders_count else 0

    return {
        "sales_total": round(float(sales_total), 2),
        "orders_count": int(orders_count),
        "average_order_value": round(float(average_order_value), 2),
        "products_count": int(products_count),
        "customers_count": int(customers_count),
    }
