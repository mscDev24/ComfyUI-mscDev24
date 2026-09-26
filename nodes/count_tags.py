class CountTags:
    """
    Counts non-empty tags in a string using a configurable separator.
    """

    DESCRIPTION = (
        "Counts non-empty elements in a string separated by the specified delimiter. "
        "Whitespace around elements is ignored and empty elements are not counted."
    )

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
                "separator": ("STRING", {
                    "default": ","
                }),
            }
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("count",)

    FUNCTION = "count_tags"
    CATEGORY = "mscDev24"

    def count_tags(self, text, separator):
        if not separator:
            return (0,)

        tags = [
            tag.strip()
            for tag in text.split(separator)
            if tag.strip()
        ]

        return (len(tags),)


NODE_CLASS_MAPPINGS = {
    "CountTags": CountTags,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CountTags": "Count Tags",
}
