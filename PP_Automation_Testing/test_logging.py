import logging

class Logging:
    def get_logger(self):
        logger= logging.getLogger(__name__)

        filehandler= logging.FileHandler("logfile.log")
        formatter= logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        filehandler.setFormatter(formatter)

        logger.addHandler(filehandler)
        return logger

        logger.setLevel(logging.DEBUG)
        logger.debug(" Debug statment is executed")                          #This Is  the order
        logger.info(" INFO Printed")                                         #This Is  the order
        logger.warning("Given warning")                                      #This Is  the order
        logger.error("A Major Error")                                        #This Is  the order
        logger.critical("Critical printed")                                  #This Is  the order