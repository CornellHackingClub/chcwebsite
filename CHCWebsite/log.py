try:
    from systemd.journal import JournalHandler
    class CHCLogHandler(JournalHandler):
        def emit(self, record):
            if record.exc_info:
                record.exc_info = ", ".join(record.exc_info)
            super(CHCLogHandler, self).emit(record)
except ImportError:
    from logging import NullHandler
    CHCLogHandler = NullHandler
