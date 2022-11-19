import logging
import azure.functions as func
import json


from .dtos.download_request import DownloadRequest
from .router import route


def main(msg: func.ServiceBusMessage, msgSoundcloud: func.Out[str], msgYoutube: func.Out[str]):
    logging.info('Python ServiceBus queue trigger processed message: %s',
                 msg.get_body().decode('utf-8'))

    download_request = DownloadRequest.from_json(json.loads(msg.get_body().decode('utf-8')))

    selected_module = route(download_request)

    if selected_module == "soundcloud":
        msgSoundcloud.set(download_request.to_json())
    elif selected_module == "youtube":
        msgYoutube.set(download_request.to_json())
    else:
        logging.error(f'Error module switch for {download_request.downloadId}')

