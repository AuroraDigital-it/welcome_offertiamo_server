from models.exceptions.redis_exception import RedisConnectionException


def handle_error(exc, task_id):
    # Handle the exception
    if isinstance(exc, ValueError):
        print('Task {} failed because y cannot be 0'.format(task_id))
    elif isinstance(exc, TypeError):
        print('Task {} failed because x and y must be integers'.format(task_id))
        raise Exception
    elif isinstance(exc, RedisConnectionException):
        raise RedisConnectionException
    