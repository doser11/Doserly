from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from deps import get_current_admin
from models import Order
from schemas import OrderStatusUpdate

router = APIRouter()


@router.get("")
def list_orders(db: Session = Depends(get_db), _admin=Depends(get_current_admin)):
    items = db.query(Order).order_by(Order.id.desc()).all()
    return {"items": items, "count": len(items)}


@router.patch("/{order_id}/status")
def update_order_status(
    order_id: int,
    payload: OrderStatusUpdate,
    db: Session = Depends(get_db),
    _admin=Depends(get_current_admin),
):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    order.order_status = payload.order_status
    order.payment_status = payload.payment_status
    db.commit()
    db.refresh(order)
    return {
        "message": "Order status updated",
        "order_id": order.id,
        "order_status": order.order_status,
        "payment_status": order.payment_status,
    }
