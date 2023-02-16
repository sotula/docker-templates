"""
Setup service module
"""
import time
import logging

SERVICE_NAME = 'ServiceTest'
INPUT_TOPIC = ''
INPUT_EXCHANGE = 'input_queue'
LOGGER = logging
LOGGER.basicConfig(level=LOGGER.DEBUG)

def runner_service():
    """
    main function for run service
    """
    # service = Service(log=LOGGER)
    # rabbit = Rabbit(heartbeat=58,
    #                 log=LOGGER)

    print(
        "%s started listen exchange: `%s` topic `%s`",
        SERVICE_NAME,
        INPUT_EXCHANGE,
        INPUT_TOPIC)
    # rabbit.consume_jobs(topic=INPUT_TOPIC,
    #                     exchange=INPUT_EXCHANGE,
    #                     function_handler=service.sync_queue_handler)


if __name__ == '__main__':
    while True:
        try:
            LOGGER.info("Started %s",
                        SERVICE_NAME)
            runner_service()
        except KeyboardInterrupt:
            break
        except Exception as e:
            LOGGER.exception("Exception: %s, Traceback: %s",
                             e,
                             format_exc())
        time.sleep(5 * 60)
        LOGGER.info("Finished %s",
                    SERVICE_NAME)
