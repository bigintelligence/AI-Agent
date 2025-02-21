import datetime
import pytz
from dateutil.relativedelta import relativedelta


def my_custom_tool(timezone1: str, timezone2: int) -> str:
    """A tool that get the time diference between two timezones
    Args:
        timezone1: the first timezone
        timezone2: the second timezone
    """
    try:
        utcnow = pytz.timezone('utc').localize(datetime.datetime.utcnow())  # generic time
        here = utcnow.astimezone(pytz.timezone(timezone1)).replace(tzinfo=None)
        there = utcnow.astimezone(pytz.timezone(timezone2)).replace(tzinfo=None)

        offset = relativedelta(here, there)
        offset.hours
        return f"The time diference for timezone '{timezone1}' and timezone '{timezone2}' is: {str(offset.hours)} hours."
    except Exception as e:
        return f"Error fetching time diference for timezone '{timezone1}' and timezone '{timezone2}': {str(e)}"


def get_current_time_in_timezone(timezone: str) -> str:
    """A tool that fetches the current local time in a specified timezone.
    Args:
        timezone: A string representing a valid timezone (e.g., 'America/New_York').
    """
    try:
        # Create timezone object
        tz = pytz.timezone(timezone)
        # Get current time in that timezone
        local_time = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
        return f"The current local time in {timezone} is: {local_time}"
    except Exception as e:
        return f"Error fetching time for timezone '{timezone}': {str(e)}"


if __name__ == "__main__":
    resp = my_custom_tool('Europe/Madrid', 'Asia/Ho_Chi_Minh')
    print(resp)
    resp2 = get_current_time_in_timezone('Asia/Ho_Chi_Minh')
    print(resp2)

