# coding: utf-8
from ninja import Schema


class PermissionSchema(Schema):
    ADMIN: bool
    STAFF: bool


class UserSchema(Schema):
    id: int
    name: str
    username: str
    first_name: str
    last_name: str
    email: str
    avatar: str = None
    bio: str = None
    permissions: PermissionSchema


class LoggedUserSchema(Schema):
    user: UserSchema
    authenticated: bool
