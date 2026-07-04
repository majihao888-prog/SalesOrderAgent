from app_config import SETTINGS
from logger import logger
from services.pipeline import Pipeline


def print_banner():

    print("=" * 60)
    print(
        f"{SETTINGS['project_name']} Version {SETTINGS['version']}"
    )
    print("=" * 60)


def main():

    print_banner()

    logger.info("Program Started")

    Pipeline().run()

    logger.info("Program Finished")


if __name__ == "__main__":
    main()