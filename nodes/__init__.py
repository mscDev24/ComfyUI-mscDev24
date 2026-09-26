from .count_tags import CountTags
from .remove_tag_suffixes import RemoveTagSuffixes

NODE_CLASS_MAPPINGS = {
    "CountTags": CountTags,
    "RemoveTagSuffixes": RemoveTagSuffixes,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CountTags": "Count Tags",
    "RemoveTagSuffixes": "Remove Tag Suffixes",
}