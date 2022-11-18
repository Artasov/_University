from rest_framework import permissions


class IsAdministrator(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.isAdministrator()


class IsCurator(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.isCurator()


class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.isStudent()
