"""
Date Scheduling Utilities
Extracted from utils/date_scheduler.py

Handles calendar date calculations, unavailable dates, and scheduling constraints
"""

from datetime import datetime, timedelta, date
from typing import List, Dict, Optional
import re


def parse_unavailable_dates(unavailable_str: str) -> List[date]:
    """
    Parse unavailable dates string into list of date objects
    Supports formats like: "Nov 20-22, Dec 1", "2025-11-20, 2025-12-01"
    """
    if not unavailable_str or not unavailable_str.strip():
        return []

    unavailable_dates = []

    # Split by comma
    parts = [p.strip() for p in unavailable_str.split(',')]

    for part in parts:
        if not part:
            continue

        # Check for date range (e.g., "Nov 20-22" or "2025-11-20 to 2025-11-25")
        if '-' in part and 'to' not in part.lower():
            # Try to parse as range
            try:
                # Handle "Nov 20-22" format
                range_parts = part.split('-')
                if len(range_parts) == 2:
                    # Try parsing with different formats
                    start_date = parse_single_date(range_parts[0].strip())
                    end_date = parse_single_date(range_parts[1].strip(), reference_date=start_date)

                    if start_date and end_date:
                        current = start_date
                        while current <= end_date:
                            unavailable_dates.append(current)
                            current += timedelta(days=1)
            except:
                pass
        elif 'to' in part.lower():
            # Handle "Nov 20 to Nov 22" format
            try:
                range_parts = re.split(r'\s+to\s+', part, flags=re.IGNORECASE)
                if len(range_parts) == 2:
                    start_date = parse_single_date(range_parts[0].strip())
                    end_date = parse_single_date(range_parts[1].strip())

                    if start_date and end_date:
                        current = start_date
                        while current <= end_date:
                            unavailable_dates.append(current)
                            current += timedelta(days=1)
            except:
                pass
        else:
            # Single date
            single_date = parse_single_date(part)
            if single_date:
                unavailable_dates.append(single_date)

    return list(set(unavailable_dates))  # Remove duplicates


def parse_single_date(date_str: str, reference_date: date = None) -> Optional[date]:
    """
    Parse a single date string into a date object
    Supports: "Nov 20", "2025-11-20", "11/20/2025", "20"
    """
    if not date_str:
        return None

    date_str = date_str.strip()
    current_year = datetime.now().year

    # Try different formats
    formats = [
        "%Y-%m-%d",      # 2025-11-20
        "%m/%d/%Y",      # 11/20/2025
        "%m/%d/%y",      # 11/20/25
        "%b %d",         # Nov 20
        "%B %d",         # November 20
        "%b %d, %Y",     # Nov 20, 2025
        "%B %d, %Y",     # November 20, 2025
    ]

    for fmt in formats:
        try:
            parsed = datetime.strptime(date_str, fmt)
            # If year is not in format, use current year
            if "%Y" not in fmt and "%y" not in fmt:
                return parsed.replace(year=current_year).date()
            return parsed.date()
        except ValueError:
            continue

    # Try parsing just day number (e.g., "22")
    if date_str.isdigit() and reference_date:
        try:
            day = int(date_str)
            return reference_date.replace(day=day)
        except:
            pass

    return None


def is_day_available(
    check_date: date,
    unavailable_dates: List[date],
    skip_weekends: bool = False,
    skip_weekdays: List[int] = None
) -> bool:
    """
    Check if a specific date is available for work

    Args:
        check_date: Date to check
        unavailable_dates: List of specific unavailable dates
        skip_weekends: Whether to skip weekends
        skip_weekdays: List of weekdays to skip (0=Monday, 6=Sunday)

    Returns:
        True if date is available, False otherwise
    """
    # Check specific unavailable dates
    if check_date in unavailable_dates:
        return False

    weekday = check_date.weekday()  # 0=Monday, 6=Sunday

    # Check skip weekends
    if skip_weekends and weekday >= 5:  # 5=Saturday, 6=Sunday
        return False

    # Check skip specific weekdays
    if skip_weekdays and weekday in skip_weekdays:
        return False

    return True


def calculate_calendar_dates(
    start_date: date,
    topics: List[Dict],
    hours_per_day: float = 2.0,
    unavailable_dates: List[date] = None,
    skip_weekends: bool = False,
    skip_weekdays: List[int] = None
) -> List[Dict]:
    """
    Calculate calendar due dates for all topics based on scheduling constraints

    Args:
        start_date: When to start the learning path
        topics: List of topic dicts with 'estimated_hours' field
        hours_per_day: Average hours available per day
        unavailable_dates: List of specific unavailable dates
        skip_weekends: Whether to skip weekends
        skip_weekdays: List of weekdays to skip (0=Monday, 6=Sunday)

    Returns:
        Updated topics list with 'due_date' field added
    """
    if unavailable_dates is None:
        unavailable_dates = []

    current_date = start_date
    updated_topics = []

    for topic in topics:
        estimated_hours = topic.get('estimated_hours', 2.0)

        # Calculate how many days this topic will take
        days_needed = max(1, round(estimated_hours / hours_per_day))

        # Find the due date by counting available days
        days_counted = 0
        check_date = current_date

        while days_counted < days_needed:
            if is_day_available(check_date, unavailable_dates, skip_weekends, skip_weekdays):
                days_counted += 1
                if days_counted == days_needed:
                    due_date = check_date
                    break
            check_date += timedelta(days=1)

        # Update topic with due date
        topic_copy = topic.copy()
        topic_copy['due_date'] = due_date.strftime('%Y-%m-%d')
        updated_topics.append(topic_copy)

        # Next topic starts day after this one's due date
        current_date = due_date + timedelta(days=1)

        # Skip to next available day
        while not is_day_available(current_date, unavailable_dates, skip_weekends, skip_weekdays):
            current_date += timedelta(days=1)

    return updated_topics


def format_date_display(due_date_str: str) -> str:
    """
    Format a date string for display
    Converts "2025-11-16" to "📅 Nov 16, 2025"
    """
    if not due_date_str:
        return ""

    try:
        due_date = datetime.strptime(due_date_str, '%Y-%m-%d')
        return f"📅 {due_date.strftime('%b %d, %Y')}"
    except:
        return due_date_str

