import logging

logging.basicConfig(
    filename="system.log",
    level=logging.DEBUG,
    format="%(asctime)s-%(levelname)s-%(message)s"
)

#log message
logging.info("System initialized")
logging.info("User login Successful")
logging.error("Running out of error")
logging.warning("High memory usage")
logging.error("Unable to connect to the server")