from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        return False


class IsPublic(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff:
            return request.method is SAFE_METHODS

# class IsPublic(BasePermission):
#
#     def has_object_permission(self, request, view, obj):
#         return obj.is_public
