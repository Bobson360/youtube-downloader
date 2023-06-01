import re

def clean_title(title):
    """Removes invalid characters from title to use as filename."""
    return re.sub(r'[\\/*?:"<>|]', "", title)
