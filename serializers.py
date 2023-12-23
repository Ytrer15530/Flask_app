from app import ma
from app import User, Post


class UserSerializer(ma.SQLAlchemyAutoSchema):
    models = User


class PostSerializer(ma.SQLAlchemyAutoSchema):
    models = Post
