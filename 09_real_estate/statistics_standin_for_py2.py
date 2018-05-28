def mean(data):
    if iter(data) is data:
        data = list(data)
    n = len(data)
    if n < 1:
        raise StatisticsError('mean requires at least one data point')
    return sum(data) / n


class StatisticsError(ValueError):
    """Value errors in Statistics module"""
