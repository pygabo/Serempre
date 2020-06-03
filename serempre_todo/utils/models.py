# Python Utils
from uuid import uuid4

# Django
from django.db.models import UUIDField
# Third party imports
from model_utils.models import SoftDeletableModel, TimeStampedModel


class BaseModel(TimeStampedModel, SoftDeletableModel):
    id = UUIDField(primary_key=True, default=uuid4, editable=False)

    class Meta:
        abstract = True
