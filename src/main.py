from utility import get_logger
from mycodo_api import MycodoApi

logger = get_logger()
mycodo = MycodoApi()

def main():
    logger.info("Initializing Mycodo Prometheus Exporter")
    mycodo.get_inputs()
    


main()

if __file__ == "__main__":
    main()
    

    