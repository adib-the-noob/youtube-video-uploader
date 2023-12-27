from pydantic import BaseModel

class UserRegister(BaseModel):
    full_name : str
    password : str
    phone_number : str
    password : str
    # confirm_password : str = None

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise ValueError("Passwords do not match")
        return data

