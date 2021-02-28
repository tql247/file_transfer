from file_transfer.access.access import get_video_file_name
from file_transfer.config import IS_TRANSFER_ALL, FROM_DIR, TO_DIR
from file_transfer.utils.helper import file_transferring


def handle():
    success = None
    if IS_TRANSFER_ALL:
        success = file_transferring(FROM_DIR, TO_DIR)
    else:
        list_file = get_video_file_name()
        success = file_transferring(list_file, FROM_DIR, TO_DIR)
    if success:
        print('Transfer successfully')
        return True

    return False
