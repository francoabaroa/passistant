from enum import Enum

class Source(Enum):
    SMS = 'SMS'
    EMAIL = 'EMAIL'
    CALENDAR = 'CALENDAR'
    VOICE_NOTE = 'VOICE NOTE'
    IMAGE = 'IMAGE'