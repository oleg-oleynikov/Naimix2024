from keycloak import KeycloakOpenID
from app.core.config import settings

keycloak_openid = KeycloakOpenID(
    server_url=settings.KEYCLOAK_URL,
    client_id=settings.KEYCLOAK_CLIENT_ID,
    realm_name=settings.KEYCLOAK_REALM_NAME,
    client_secret_key=settings.KEYCLOAK_SECRET_KEY  # Получите его из настроек клиента в Keycloak
)

def get_keycloak_client():
    return keycloak_openid