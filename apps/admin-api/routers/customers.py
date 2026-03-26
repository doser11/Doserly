from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from deps import get_current_admin
from models import Customer
from schemas import CustomerOut

router = APIRouter()


@router.get("", response_model=list[CustomerOut])
def list_customers(db: Session = Depends(get_db), _admin=Depends(get_current_admin)):
    return db.query(Customer).order_by(Customer.id.desc()).all()
