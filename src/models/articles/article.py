import datetime


class Article(object):
    def __int__(self, url, slack_channel, earliest_time=None, date=None):
        self.url = url
        self.date = datetime.datetime() if date is None else date
        self.slack_channel = slack_channel
        self.time_period = datetime.datetime() - datetime.timedelta(days=1) if earliest_time is None else earliest_time


    # """
    # Example: slack_channel
    # """

