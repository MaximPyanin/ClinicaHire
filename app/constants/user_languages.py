from enum import Enum

class UsersLanguages(Enum):
    ENGLISH = "English"
    GERMAN = "German"
    FRENCH = "French"
    SPANISH = "Spanish"
    POLISH = "Polish"
    ITALIAN = "Italian"
    DUTCH = "Dutch"
    PORTUGUESE = "Portuguese"
    SWEDISH = "Swedish"
    DANISH = "Danish"
    FINNISH = "Finnish"
    GREEK = "Greek"
    HUNGARIAN = "Hungarian"
    CZECH = "Czech"
    SLOVAK = "Slovak"
    ROMANIAN = "Romanian"


class LanguageLevels(Enum):
    A1 = "Beginner (A1)"
    A2 = "Elementary (A2)"
    B1 = "Intermediate (B1)"
    B2 = "Upper-Intermediate (B2)"
    C1 = "Advanced (C1)"
    C2 = "Proficient (C2)"
    NATIVE = "Native"
