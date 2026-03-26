from sqlalchemy.orm import Session

from models import AdminUser, ThemeSetting
from security import hash_password


def seed_initial_data(db: Session):
    admin = db.query(AdminUser).filter(AdminUser.email == "admin@doserly.com").first()
    if not admin:
        db.add(
            AdminUser(
                email="admin@doserly.com",
                full_name="Doserly Admin",
                password_hash=hash_password("Admin@123"),
                is_active=True,
            )
        )

    theme = db.query(ThemeSetting).first()
    if not theme:
        db.add(
            ThemeSetting(
                primary_color="#fe9931",
                background_color="#ffffff",
                text_color="#111111",
            )
        )
    db.commit()
