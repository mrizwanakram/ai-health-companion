# fitbit_integration.py
import requests
from urllib.parse import urlencode

CLIENT_ID = 'your-client-id'
CLIENT_SECRET = 'your-client-secret'
REDIRECT_URI = 'http://localhost:8080'
AUTHORIZATION_URL = 'https://www.fitbit.com/oauth2/authorize'
TOKEN_URL = 'https://api.fitbit.com/oauth2/token'


def get_authorization_url():
    auth_params = {
        'response_type': 'code',
        'client_id': CLIENT_ID,
        'redirect_uri': REDIRECT_URI,
        'scope': 'activity sleep heartrate'
    }
    auth_url = f"{AUTHORIZATION_URL}?{urlencode(auth_params)}"
    return auth_url


def get_access_token(authorization_code):
    data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'code': authorization_code,
        'grant_type': 'authorization_code',
        'redirect_uri': REDIRECT_URI
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post(TOKEN_URL, data=data, headers=headers)
    return response.json().get('access_token')


def get_steps_data(access_token):
    url = 'https://api.fitbit.com/1/user/-/activities/steps/date/today/1d.json'
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else None
