import os.path

FILES_DIR = os.path.dirname(__file__)


def get_path(filename: str):
    return os.path.join(FILES_DIR, filename)

CSV_FILE_PATH = get_path(filename="oc_customer.csv")
ADMIN_CREDENTIALS = get_path(filename="admin_credentials.csv")
