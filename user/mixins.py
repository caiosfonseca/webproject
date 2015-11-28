class SuccessMixin(object):

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return self.success_url
