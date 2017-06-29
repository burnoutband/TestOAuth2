# We Stores All of the permission classes for our application.

from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile."""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile."""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id



class PostOwnStatus(permissions.BasePermission):
    """Allow users to update their own status."""

    def has_object_permission(self, request, view, obj):
        """Checks the user is trying to update their own status."""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id




class IsAuthenticatedOrCreate(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return super(IsAuthenticatedOrCreate, self).has_permission(request, view)


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    객체의 소유자에게만 쓰기를 허용하는 커스텀 권한
    """

    def has_object_permission(self, request, view, obj):
        # 읽기 권한은 모두에게 허용하므로,
        # GET, HEAD, OPTIONS 요청은 항상 허용함
        if request.method in permissions.SAFE_METHODS:
            return True

        # 이 부분이 중요한데, 매개변수로 받는 obj는 우리가 해당앱에서 다루기 위해
        # 모델링하고 직렬화한 인스턴스이므로 user 인스턴스와 동일한 타입이다.
        # 즉, 항상 request.user와 동일한 인스턴스는 아니라는 것이다.
        # obj는 object의 약자로 목적이나 대상을 의미하니.
        return obj == request.user
