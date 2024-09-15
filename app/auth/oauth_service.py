from authlib.integrations.starlette_client import OAuth
class OauthService:
    def __init__(self):
        self.oauth = OAuth('config')
    def set_oauth(self) ->int:
        return  self.oauth.register(
        name='google',
        client_id='GOOGLE_CLIENT_ID',
        client_secret='GOOGLE_CLIENT_SECRET',
        authorize_url='https://accounts.google.com/o/oauth2/auth',
        authorize_params=None,
        access_token_url='https://accounts.google.com/o/oauth2/token',
        access_token_params=None,
        refresh_token_url=None,
        redirect_uri='http://localhost:8000/auth/google',
        client_kwargs={'scope': 'openid email profile'},
    )
