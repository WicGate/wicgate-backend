from django.utils.deconstruct import deconstructible
from storages.backends.dropbox import DropBoxStorage


@deconstructible
class ExtendedDropBoxStorage(DropBoxStorage):

    def _full_path(self, name):
        if name[0] != '/':
            name = '/' + name
        # return safe_join(self.root_path, name).replace('\\', '/')
        return name.replace('\\', '/')
