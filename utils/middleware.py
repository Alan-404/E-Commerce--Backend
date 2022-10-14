import jwt

class MiddleWare:
    def generate_token(self, account_id):
        payload = {
            "account_id": account_id
        }

        return jwt.encode(payload, key="dfadffa", algorithm='HS256')