from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from deps import get_current_admin
from models import ThemeSetting
from schemas import ThemeSettings

router = APIRouter()


@router.get("/theme", response_model=ThemeSettings)
def get_theme_settings(db: Session = Depends(get_db), _admin=Depends(get_current_admin)):
    theme = db.query(ThemeSetting).first()
    if not theme:
        theme = ThemeSetting(primary_color="#fe9931", background_color="#ffffff", text_color="#111111")
        db.add(theme)
        db.commit()
        db.refresh(theme)
    return theme


@router.put("/theme", response_model=ThemeSettings)
def update_theme_settings(
    payload: ThemeSettings,
    db: Session = Depends(get_db),
    _admin=Depends(get_current_admin),
):
    theme = db.query(ThemeSetting).first()
    if not theme:
        theme = ThemeSetting(**payload.model_dump())
        db.add(theme)
    else:
        theme.primary_color = payload.primary_color
        theme.background_color = payload.background_color
        theme.text_color = payload.text_color

    db.commit()
    db.refresh(theme)
    return theme
