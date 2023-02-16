import sys
from pathlib import Path


def main():
    """
    Main function for call by cron
    """
    body = {'limit': 30}
    header = {
        'command': 'getInfo'
    }
    print(header)
    # Rabbit().send_msg(topic=INPUT_TOPIC,
    #                   msg=body,
    #                   headers=header,
    #                   exchange=INPUT_EXCHANGE)


if __name__ == '__main__':
    main()
