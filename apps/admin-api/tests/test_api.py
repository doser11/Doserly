from fastapi.testclient import TestClient

from main import app


def login_token(client: TestClient) -> str:
    response = client.post(
        "/api/admin/auth/login",
        json={"email": "admin@doserly.com", "password": "Admin@123"},
    )
    assert response.status_code == 200
    return response.json()["access_token"]


def test_health_check():
    with TestClient(app) as client:
        response = client.get("/api/admin/health")
        assert response.status_code == 200
        body = response.json()
        assert body["status"] == "ok"


def test_admin_login_success():
    with TestClient(app) as client:
        token = login_token(client)
        assert isinstance(token, str)
        assert len(token) > 10


def test_product_crud_minimal():
    with TestClient(app) as client:
        token = login_token(client)
        headers = {"Authorization": f"Bearer {token}"}

        create_response = client.post(
            "/api/admin/products",
            headers=headers,
            json={
                "name": "Doserly Test Product",
                "product_type": "stock",
                "price": 199.99,
                "status": "active",
                "stock_qty": 20,
            },
        )
        assert create_response.status_code == 201

        list_response = client.get("/api/admin/products", headers=headers)
        assert list_response.status_code == 200
        assert isinstance(list_response.json(), list)


def test_coupon_crud_minimal():
    with TestClient(app) as client:
        token = login_token(client)
        headers = {"Authorization": f"Bearer {token}"}

        create_response = client.post(
            "/api/admin/discounts/coupons",
            headers=headers,
            json={
                "code": "DOSER15",
                "discount_type": "percentage",
                "discount_value": 15,
                "min_order_total": 500,
                "max_uses": 100,
                "status": "active",
            },
        )
        assert create_response.status_code in (201, 409)

        list_response = client.get("/api/admin/discounts/coupons", headers=headers)
        assert list_response.status_code == 200


def test_shipping_rate_crud_minimal():
    with TestClient(app) as client:
        token = login_token(client)
        headers = {"Authorization": f"Bearer {token}"}

        create_response = client.post(
            "/api/admin/shipping",
            headers=headers,
            json={
                "country": "Egypt",
                "governorate": "Cairo",
                "city": "Nasr City",
                "fee": 50,
                "is_active": True,
            },
        )
        assert create_response.status_code == 201

        list_response = client.get("/api/admin/shipping", headers=headers)
        assert list_response.status_code == 200
        assert isinstance(list_response.json(), list)
