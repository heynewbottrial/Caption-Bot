import os


class Config(object):
    # env vars
    BOT_TOKEN = "6260622606:AAF6CzWlP0mrHpcqZZsEMhi-rNyXQLQ5SKs"  # string
    API_ID = 24262622  # int
    API_HASH = "50831eb3329ed9c0557aa2bc6aa34376"  # string
    
    # db vars
    # keep empty if don't want to add any extra caption
    CAPTION_TEXT = "Download By:- Electric Hacker"  
    # BOTTOM or TOP or NIL
    CAPTION_POSITION = "BOTTOM"  
    ADMIN_USERNAME = "ElectricHacker"  # without "@". 

    # a list of strings of words to remove from the existing caption
    WORDS_TO_REMOVE = [
        "TheOne🤡", "@theone1second", "Uploaded by :", "sabka boyfriend", 
        "『 🅰🅸🆁 🅿🅷🅴🅾🅽🅸🆇™』", "@ImTgLoki", "[©🅢🅐🅚🅢🅗🅐🅜™]", "LOSER 💔", 
        "𝐋ᴏşϯ :･ﾟ✧ °”𝕃ⲟꜱ𝙚𝑟”°💔💔", "Let's promote Free education♥️", 
        "DILDAAR YAARA 💚", "Downloaded by »", "@St2Master", "『ᎷΔŞŦᏋᏒ』", 
        "[MASOOM GURJAR™]", "🄼🄰🅂🅃🄴🅁", "Extracted By ➤", "[©Class_Tube]"
    ]    
    # a list of regex pattern strings to remove from the existing caption. 
    # For eg. r".*Join.*" will remove the entire line having word Join
    REGEX_PATTERNS = []  

    # keep empty to allow in all channels. Can add multiple channels separated by a comma.
    # Don't forget -100 before the channel ID
    ALLOWED_CHANNELS = []

    # REMOVE or POSTFIX or NIL. Useful for tamilblasters, tamilmv and other webites
    WEBSITE_PREFIX = "POSTFIX"  

    # True or False. Replaces YIFY website with YTS
    YTS_WEBSITE_REPLACE = True 

    # Dictionary of words to replace
    REPLACE_DICTIONARY = {}

    # Replace dot separator with space
    SEPARATOR_SPACE = True
