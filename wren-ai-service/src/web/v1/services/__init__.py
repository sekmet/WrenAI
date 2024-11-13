from datetime import datetime
from typing import Optional

import pytz
from pydantic import BaseModel


class MetadataTraceable:
    def with_metadata(self) -> dict:
        return {
            "resource": self,
            "metadata": {
                **self._error_metadata(),
            },
        }

    def _error_metadata(self):
        return {
            "error_type": self.error and self.error.code,
            "error_message": self.error and self.error.message,
        }


class Configuration(BaseModel):
    class FiscalYear(BaseModel):
        start: str
        end: str

    class Timezone(BaseModel):
        name: str = "Asia/Taipei"

    def show_current_time(self):
        # Get the current time in the specified timezone
        tz = pytz.timezone(
            self.timezone.name
        )  # Assuming timezone.name contains the timezone string
        current_time = datetime.now(tz)

        return f'{current_time.strftime("%Y-%m-%d %A")}'  # YYYY-MM-DD weekday_name, ex: 2024-10-23 Wednesday

    fiscal_year: Optional[FiscalYear] = None
    language: Optional[str] = "English"
    timezone: Optional[Timezone] = Timezone()