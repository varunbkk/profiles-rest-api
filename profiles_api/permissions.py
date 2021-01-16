from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to erdit their own profile"""

    def has_object_permission(self,request,view,obj):
        """Check user is trying to edit their own profile"""

        if request.method in permissions.SAFE_METHODS:
            return True

        """Basically checks through user's ID if they are try to update their own profile or somebody else's"""
        return obj.id == request.user.id
