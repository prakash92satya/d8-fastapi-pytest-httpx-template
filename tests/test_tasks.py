import pytest

@pytest.mark.asyncio
async def test_create_task(client):
    response = await client.post("/tasks/", params={"title": "Test Task"})
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_get_tasks(client):
    await client.post("/tasks/", params={"title": "Task 1"})
    response = await client.get("/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)