import hashlib

from django.db import models


class Record(models.Model):
    text = models.BinaryField(max_length=10000)
    iv = models.BinaryField(max_length=16, null=True)
    locked_till = models.DateTimeField(null=True, blank=True)
    can_be_deleted = models.BooleanField(default=True)
    uuid = models.CharField(max_length=32, null=True)
    creation_date = models.DateTimeField(auto_now=True)

    @property
    def md5_key_for_delete(self):
        control_string = f"{self.id}{self.uuid}"
        return hashlib.md5(control_string.encode()).hexdigest()

    @property
    def bytes_text_to_str(self):
        bytes_to_str = str(self.text.tobytes())
        slice_max = len(bytes_to_str) 
        if slice_max > 50:
            slice_max = 50
        slice_max -= 2
        return "%s..." % bytes_to_str[2:slice_max]
