from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from deps import get_current_admin
from models import ShippingRate
from schemas import ShippingRateCreate, ShippingRateOut

router = APIRouter()


@router.get("", response_model=list[ShippingRateOut])
def list_shipping_rates(db: Session = Depends(get_db), _admin=Depends(get_current_admin)):
    return db.query(ShippingRate).order_by(ShippingRate.id.desc()).all()


@router.post("", response_model=ShippingRateOut, status_code=201)
def create_shipping_rate(
    payload: ShippingRateCreate,
    db: Session = Depends(get_db),
    _admin=Depends(get_current_admin),
):
    rate = ShippingRate(**payload.model_dump())
    db.add(rate)
    db.commit()
    db.refresh(rate)
    return rate


@router.put("/{rate_id}", response_model=ShippingRateOut)
def update_shipping_rate(
    rate_id: int,
    payload: ShippingRateCreate,
    db: Session = Depends(get_db),
    _admin=Depends(get_current_admin),
):
    rate = db.query(ShippingRate).filter(ShippingRate.id == rate_id).first()
    if not rate:
        raise HTTPException(status_code=404, detail="Shipping rate not found")

    for key, value in payload.model_dump().items():
        setattr(rate, key, value)

    db.commit()
    db.refresh(rate)
    return rate


@router.delete("/{rate_id}", status_code=204)
def delete_shipping_rate(rate_id: int, db: Session = Depends(get_db), _admin=Depends(get_current_admin)):
    rate = db.query(ShippingRate).filter(ShippingRate.id == rate_id).first()
    if not rate:
        raise HTTPException(status_code=404, detail="Shipping rate not found")
    db.delete(rate)
    db.commit()
    return None
