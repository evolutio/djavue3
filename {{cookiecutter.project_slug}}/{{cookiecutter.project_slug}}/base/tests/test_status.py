def test_obter_status(client, db):
    resp = client.get("/api/status")
    assert resp.status_code == 200
    assert resp.json() == {
        "status": "ok",
        "db": "ok",
    }
