import pytest

@pytest.mark.asyncio
async def test_register(client):
    response = await client.post("/auth/register", params={
        "username": "testuser",
        "password": "123"
    })
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_login(client):
    await client.post("/auth/register", params={
        "username": "loginuser",
        "password": "123"
    })

    response = await client.post("/auth/login", params={
        "username": "loginuser",
        "password": "123"
    })

    assert response.status_code == 200
    assert "access_token" in response.json()