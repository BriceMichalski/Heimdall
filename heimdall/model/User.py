from flask_restful import reqparse
from flask_bcrypt import generate_password_hash, check_password_hash

class User:

    attribute = reqparse.RequestParser()
    attribute.add_argument("id", type=str)
    attribute.add_argument("name", type=str, help="name is missing", required=True)
    attribute.add_argument("password", type=str, help="password is missing", required=True)

    def hashPassword(password: str) -> str:
        return generate_password_hash(password).decode('utf8')
    
    def check_password(hashedPassword: str,password: str) -> bool:
        return check_password_hash(hashedPassword,password)