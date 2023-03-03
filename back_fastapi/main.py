"""
# 実行コマンド
$ poetry run uvicorn main:app --reload

# Swagger UI
http://localhost:8000/docs
"""

from fastapi import FastAPI, Depends
from fastapi.security import HTTPBearer

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
def private(token: str = Depends(token_auth_scheme)):
    """アクセストークンが必要なエンドポイント"""

    result = token.credentials

    return result
