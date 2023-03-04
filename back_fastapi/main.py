"""
# 実行コマンド
$ poetry run uvicorn main:app --reload

# Swagger UI
http://localhost:8000/docs
"""

from fastapi import Depends, FastAPI, Response, status
from fastapi.security import HTTPBearer

from utils import VerifyToken

# Authorizationヘッダのスキーマ
token_auth_scheme = HTTPBearer()

app = FastAPI()


@app.get("/api/public")
def public():
    """アクセストークン不要のエンドポイント"""

    result = {
        "status:": "success",
        "message": "public endpoint",
    }
    return result


@app.get("/api/private")
def private(response: Response, token: str = Depends(token_auth_scheme)):
    """アクセストークンが必要なエンドポイント"""

    print(f"token.credentials = {token.credentials}")

    result = VerifyToken(token.credentials).verify()
    print(f"result = {result}")

    if result.get("status"):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return result

    return result
