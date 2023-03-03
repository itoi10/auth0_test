import os
import jwt
from configparser import ConfigParser


def setup():
    """.configファイルの設定読込"""

    config = ConfigParser()
    config.read(".config")
    config = config["AUTH0"]

    return config


class VerifyToken:
    """PyJWTを使用してトークン検証"""

    def __init__(self, token):
        self.token = token
        self.config = setup()

        # JWKはJWTの発行元から取得する
        jwks_url = f"https://{self.config['DOMAIN']}/.well-known/jwks.json"
        self.jwks_client = jwt.PyJWKClient(jwks_url)

    def verify(self):
        """トークン検証
        成功時はトークンのpayloadを返す
        失敗時はエラーメッセージを返す
        """

        # トークン署名を検証するためのキーを取得
        try:
            self.signing_key = self.jwks_client.get_signing_key_from_jwt(self.token).key

        except jwt.exceptions.PyJWKClienError as e:
            return {"status": "error", "message": e.__str__()}

        except jwt.exceptions.DecodeError as e:
            return {"status": "error", "message": e.__str__()}

        # JWTをデコードしてトークンのpayloadを取得
        try:
            payload = jwt.decode(
                self.token,
                self.signing_key,
                algorithms=self.config["ALGORITHM"],
                audience=self.config["AUDIENCE"],
                issuer=self.config["ISSUER"],
            )

        except Exception as e:
            return {"status": "error", "message": e.__str__()}

        return payload
