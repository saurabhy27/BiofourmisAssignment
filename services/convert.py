import calendar


def convert_into_timestamp(timestamp):
    return calendar.timegm(timestamp.to_pydatetime().timetuple())
