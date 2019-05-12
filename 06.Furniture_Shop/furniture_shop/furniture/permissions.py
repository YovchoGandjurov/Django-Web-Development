from django.shortcuts import render


class SameUserOnlyMixin(object):
    def has_permissions(self):
        result = self.get_object().user.id == self.request.user.id or \
                 self.request.user.is_superuser
        return result

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():
            return render(request, 'permission_denied.html')
        return super(SameUserOnlyMixin, self).dispatch(
                        request, *args, **kwargs)
