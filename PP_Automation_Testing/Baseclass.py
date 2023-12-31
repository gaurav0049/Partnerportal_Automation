import inspect
import logging

class Logging:
    def get_logger(self):
        loggername=inspect.stack()[1][3]
        logger= logging.getLogger(loggername)

        filehandler= logging.FileHandler("logfile.log")
        formatter= logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        filehandler.setFormatter(formatter)

        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        return logger