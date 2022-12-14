from django.contrib.auth import get_user_model
from django.db.models import signals
from django.dispatch import receiver
from fishingbs.accounts.models import Profile

UserModel = get_user_model()


# def create_profile_on_registration(instance, created, *args, **kwargs):
#     if not created:
#         return
#
#     profile = Profile(
#         user=instance
#     )
#     profile.save()
#
#
# signals.pre_save.connect(sender=UserModel)

