from model_utils.models import TimeStampedModel, UUIDModel

from apps.base.utils import camel_to_snake


class BaseModel(UUIDModel, TimeStampedModel):
    class Meta:
        abstract = True
        ordering = ['-created']

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        # Only set db_table for concrete subclasses
        if not cls._meta.abstract:
            cls._meta.db_table = camel_to_snake(cls.__name__)
