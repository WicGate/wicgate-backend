from django.utils.deconstruct import deconstructible
from storages.backends.dropbox import DropBoxStorage


@deconstructible
class ExtendedDropBoxStorage(DropBoxStorage):

    def _full_path(self, name):
        if name[0] != '/':
            name = '/' + name
        return name.replace('\\', '/')

    def url(self, name):
        return name

    def _save(self, name, content):
        print(name)
        super(ExtendedDropBoxStorage, self)._save(name, content)
        shared_link = self.client.sharing_create_shared_link(path=name)
        return shared_link.url
