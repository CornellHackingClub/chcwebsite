try:
    from systemd.journal import JournalHandler
    class CHCLogHandler(JournalHandler):
        pass
except ImportError:
    from logging import NullHandler
    CHCLogHandler = NullHandler
