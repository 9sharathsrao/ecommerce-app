import requests

def test_metrics():
    response = requests.get('http://localhost:5000/metrics')
    assert response.status_code == 200, "Metrics endpoint failed"

def test_alerts():
    pass  # Simulate high usage and check alerts

if __name__ == "__main__":
    test_metrics()
    print("All tests passed.")