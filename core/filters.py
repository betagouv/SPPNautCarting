from logging import Filter


class SkipStaticFilter(Filter):
    def filter(self, record):
        return not record.getMessage().startswith('"GET /static/')
