import jwt

class MiddleWare:
    def generate_token(self, account_id):
        payload = {
            "account_id": account_id
        }
        token = jwt.JWT.encode(payload, key="sdfasdf")
        print(token)
        return jwt.JWT.encode(payload, key="sdfasdf")