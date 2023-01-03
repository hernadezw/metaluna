from rest_framework import permissions

class IsAdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        if request.method =='GET':
            return True
        staff_permission = bool(request.user and request.user.is_staff)
        return staff_permission
    
class IsDepartamentoUserOrReadonly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.user == request.user or request.user.is_staff
        