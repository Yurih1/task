from django.db import models


class SoftDeleteQuerySet(models.QuerySet):
    def delete(self, *args, **kwargs):
        return self.update(is_deleted=True)

    def hard_delete(self, *args, **kwargs):
        return super().delete(*args, **kwargs)

    def all(self):
        return super().filter(is_deleted=False)

class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return SoftDeleteQuerySet(self.model, using=self._db)

    def delete(self, *args, **kwargs):
        return self.get_queryset().delete(*args, **kwargs)

    def hard_delete(self, *args, **kwargs):
        return self.get_queryset().hard_delete(*args, **kwargs)