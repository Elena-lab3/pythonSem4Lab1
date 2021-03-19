#!/usr/bin/env python3

import logging

logging.basicConfig(format="%(message)s", level=logging.INFO)

def main():
    logging.info("Hello! This is Info message!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.info("Oh no!!!")
