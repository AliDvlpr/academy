from django.core.files.storage import FileSystemStorage

class ChunkedFileSystemStorage(FileSystemStorage):
    def _save(self, name, content):
        full_path = self.path(name)
        with open(full_path, 'wb+') as destination:
            for chunk in content.chunks():
                destination.write(chunk)
        return name
