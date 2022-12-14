from django.core.exceptions import ValidationError


def age_validator(age):
    if not 16 <= age <= 90:
        raise ValidationError('You should be at least 16 and less than 90 years old.')


def image_max_size_validator(image):
    max_size = 5
    image_size = image.file.size
    max_size_in_mb = max_size * 1024 * 1024
    if image_size > max_size_in_mb:
        raise ValidationError('The image should be less than 5MB.')


def chars_only_validator(name):
    if not name.isalpha():
        raise ValidationError('Only letters allowed.')
