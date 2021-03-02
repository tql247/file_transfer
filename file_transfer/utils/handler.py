from file_transfer.access.access import get_video_file_name
from file_transfer.config import IS_TRANSFER_ALL, FROM_DIR, TO_DIR
from file_transfer.utils.helper import file_transferring, file_transferring_all


def handle(connection):
    success = None
    if IS_TRANSFER_ALL:
        success = file_transferring_all(FROM_DIR, TO_DIR)
    else:
        list_file = get_video_file_name(connection)
        success = file_transferring(list_file, FROM_DIR, TO_DIR)
    if success:
        print('Transfer successfully')
        return True

    return False
