from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from database import get_db
from deps import get_current_admin
from models import Product
from schemas import ProductCreate, ProductOut

router = APIRouter()


@router.get("", response_model=list[ProductOut])
def list_products(
    page: int = 1,
    page_size: int = Query(default=20, le=100),
    db: Session = Depends(get_db),
    _admin=Depends(get_current_admin),
):
    offset = (page - 1) * page_size
    return db.query(Product).order_by(Product.id.desc()).offset(offset).limit(page_size).all()


@router.post("", response_model=ProductOut, status_code=201)
def create_product(
    payload: ProductCreate,
    db: Session = Depends(get_db),
    _admin=Depends(get_current_admin),
):
    product = Product(**payload.model_dump())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product
