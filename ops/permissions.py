from rest_framework import permissions

class EmergencyCallPermission (permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve']:
            return request.user.is_authenticated() or request.user.is_staff
        elif view.action in ['create', 'update', 'partial_update', 'destroy']:
            return request.user.is_authenticated() or request.user.is_staff
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if view.action in ['retrieve']:
            return request.user.is_authenticated() or request.user.is_staff
        elif view.action in ['update', 'partial_update', 'destroy']:
            return (obj.user == request.user or request.user.is_staff)
        else:
            return False


class EmergencyTeamPermission (permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve']:
            return request.user.is_authenticated() or request.user.is_staff
        elif view.action in ['create', 'update', 'partial_update', 'destroy']:
            return request.user.is_authenticated() or request.user.is_staff
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if view.action in ['retrieve']:
            return request.user.is_authenticated() or request.user.is_staff
        elif view.action in ['update', 'partial_update', 'destroy']:
            return (obj.user == request.user or request.user.is_staff)
        else:
            return False
