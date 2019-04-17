class TimeoutLinux:
    """
    Usage:
        with Timeout(seconds=3):
            do_things
    """
    def __init__(self, seconds=1, error_message='Timeout'):
        self.seconds = seconds
        self.error_message = error_message

    def handle_timeout(self, signum, frame):
        raise TimeoutError(self.error_message)

    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.alarm(self.seconds)

    def __exit__(self, type, value, traceback):
        signal.alarm(0)


class TimeoutMac:
    """
    Does nothing. This class is not possible on a Mac.
    """
    def __init__(self, seconds=1, error_message='Timeout'):
        pass

    def __enter__(self):
        pass

    def __exit__(self, type, value, traceback):
        pass


if platform.system() == 'Linux':
    signal = __import__('signal')
    Timeout = TimeoutLinux
else:
    Timeout = TimeoutMac