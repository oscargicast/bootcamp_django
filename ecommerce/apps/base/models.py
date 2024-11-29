from model_utils.models import TimeStampedModel, UUIDModel, SoftDeletableModel


class BaseModel(UUIDModel, TimeStampedModel, SoftDeletableModel):
    class Meta:
        abstract = True
