from user.models import User
from utils.lib import create_id
class UserService:
    def create_user(self, user_data):
        user_instance = User()
        for key in user_data.__dict__.keys():
            user_instance.__dict__[key] = user_data.__dict__[key]
        user_instance.id = create_id()
        user_instance.save()
        return user_instance

    def all_users(self):
        return User.objects.all()

    def get_user_by_email(self, email):
        return User.objects.get(email=email)
