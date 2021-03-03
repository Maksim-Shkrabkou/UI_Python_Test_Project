import requests


def api_create_episode(name):
    data = {"name": name}
    res = requests.post("http://localhost:8087/api/episodes", json=data, headers={
        "Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxIiwiaXNBZG1pbiI6dHJ1ZSwibmFtZSI6ImFkbWluIiwiaWF0IjoxNjE0Mjk0Mzk1LCJleHAiOjE2MTQ4OTkxOTV9.O3N_WD5m8rvBIbOgS6ra4eYYdNHclj5f5B8eYtG8N6lNaiCp1I4cyNgMydkjDLN-89UiBXKfuJQNVMUDCiYCkQ"
    })
    assert res.status_code == 200
