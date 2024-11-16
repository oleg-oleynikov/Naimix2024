from keycloak import KeycloakOpenID, KeycloakAdmin
from fastapi import HTTPException, status
from app.core.config import settings
from app.auth.keycloak import get_keycloak_client


class AuthService:
    def get_access_token(self, username: str, password: str):
        try:
            token = get_keycloak_client().token(username, password)
            return token
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid username or password"
            )

    def refresh_token(self, refresh_token: str):
        try:
            new_token = get_keycloak_client().refresh_token(refresh_token)
            return new_token
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Unable to refresh token"
            )

    # Выход из аккаунта (отзыв токенов)
    def logout(self, refresh_token: str):
        try:
            get_keycloak_client().logout(refresh_token)
            return {"message": "Logged out successfully"}
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Unable to logout"
            )

    def create_user(self, username: str, email: str, password: str, roles: list):
        return
        # try:
        #     user_id = get_keycloak_client().register_client({
        #         "username": username,
        #         "email": email,
        #         "enabled": True,
        #         "credentials": [{"type": "password", "value": password}],
        #     })

        #     get_keycloak_client((user_id, roles)
        #     return {"message": f"User {username} created successfully"}
        # except Exception as e:
        #     raise HTTPException(
        #         status_code=status.HTTP_400_BAD_REQUEST,
        #         detail=f"Unable to create user: {str(e)}"
        #     )

    # Удаление пользователя
    def delete_user(self, user_id: str):
        return
        # try:
        #     self.keycloak_admin.delete_user(user_id)
        #     return {"message": f"User with ID {user_id} deleted successfully"}
        # except Exception as e:
        #     raise HTTPException(
        #         status_code=status.HTTP_400_BAD_REQUEST,
        #         detail=f"Unable to delete user: {str(e)}"
        #     )

    # Получение информации о пользователе
    def get_user(self, user_id: str):
        return
        # try:
        #     user = self.keycloak_admin.get_user(user_id)
        #     return user
        # except Exception as e:
        #     raise HTTPException(
        #         status_code=status.HTTP_404_NOT_FOUND,
        #         detail="User not found"
        #     )

    # Проверка токена
    def decode_token(self, token: str):
        return 
        # try:
        #     return self.keycloak_openid.decode_token(token)
        # except Exception as e:
        #     raise HTTPException(
        #         status_code=status.HTTP_401_UNAUTHORIZED,
        #         detail="Invalid token"
        #     )
