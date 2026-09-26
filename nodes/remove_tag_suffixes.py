import re


class RemoveTagSuffixes:
    """
    Removes user-defined suffixes from the end of each tag
    and counts the remaining non-empty tags.

    Example:
        painting_\(object\) -> painting
        drawing_\(animal\) -> drawing
        photo_\(person\) -> photo
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
                "suffixes": ("STRING", {
                    "multiline": True,
                    "default": r"\(object\)"
                }),
                "separator": ("STRING", {
                    "default": ","
                }),
            }
        }

    RETURN_TYPES = ("STRING", "INT")
    RETURN_NAMES = ("tags", "tags_count")

    FUNCTION = "remove_suffixes"
    CATEGORY = "mscDev24"

    def remove_suffixes(self, text, suffixes, separator):
        if not separator:
            return (text, 0)

        tags = [
            tag.strip()
            for tag in text.split(separator)
            if tag.strip()
        ]

        suffix_list = [
            suffix.strip()
            for suffix in suffixes.split(",")
            if suffix.strip()
        ]

        result = []

        for tag in tags:
            for suffix in suffix_list:
                if tag.endswith(suffix):
                    tag = tag[:-len(suffix)]

                    # "_" direkt vor dem Suffix ebenfalls entfernen
                    if tag.endswith("_"):
                        tag = tag[:-1]

            tag = tag.strip()

            if tag:
                result.append(tag)

        tags_count = len(result)

        return (", ".join(result), tags_count)


NODE_CLASS_MAPPINGS = {
    "RemoveTagSuffixes": RemoveTagSuffixes,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "RemoveTagSuffixes": "Remove Tag Suffixes",
}