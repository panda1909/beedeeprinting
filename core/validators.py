def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.jpeg', '.gif', '.png', '.eps', '.ai', '.pdf', '.zip', '.tar', '.rar', '.cdr', '.psd', '.tif', '.csv', '.xls', '.xlsx']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')