from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to create their own profile"""

    def has_object_permission(self, request, view, obj):
        """ Check user is trying to edit their own profile"""

        """ Check the HTTP method being used for the request"""
        """ 'SAFE' methods are those methods that don't make any change to the object e.g. PUT"""
        """ users should only be able to make changes to their own profile - being checked below -> whether object ID = user id"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
