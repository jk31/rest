from rest_framework import permissions

class OnlyOwnerGET(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj