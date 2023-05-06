from rest_framework import permissions
from rest_framework.views import View, Request
from schemes.models import Scheme
from requests.models import Request as Req
from .models import User


class IsAdminUserCreate(permissions.BasePermission):
    def has_permission(self, req: Request, view: View):
        if req.method == "POST":
            return True

        return req.user.is_superuser


class IsAdminUserDestroy(permissions.BasePermission):
    def has_permission(self, req: Request, view: View):
        if req.method == "DELETE":
            return req.user.is_superuser

        return True


class IsAuthRead(permissions.BasePermission):
    def has_permission(self, req: Request, view: View):
        if req.method == "GET":
            return bool(req.user and req.user.is_authenticated)

        return req.user.is_superuser or bool(
            req.user.is_authenticated and req.user.role == "Manager"
        )


class IsAuthEmployee(permissions.BasePermission):
    def has_object_permission(self, req: Request, view: View, obj: User):
        return req.user.is_superuser or req.user.is_authenticated and obj == req.user


class IsAuthEmployeeScheme(permissions.BasePermission):
    def has_object_permission(self, req: Request, view: View, obj: Scheme):
        return (
            req.user.is_superuser
            or req.user.is_authenticated
            and obj.department == req.user.department
        )


class IsAuthEmployeeRequest(permissions.BasePermission):
    def has_object_permission(self, req: Request, view: View, obj: Req):
        return (
            req.user.is_superuser or req.user.is_authenticated and obj.user == req.user
        )
