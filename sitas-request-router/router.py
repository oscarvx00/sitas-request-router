from .dtos.download_request import DownloadRequest
import logging
import random

ALL_MODULES = ["soundcloud", "youtube"]

def route(download_request : DownloadRequest) -> str:

    available_modules = []
    for module in ALL_MODULES:
        if(getattr(download_request, module)):
            available_modules.append(module)

    if len(available_modules) == 0:
        logging.error(f'No modules available for download id: {download_request.downloadId}')
        exit(-1)
    
    selected_module = random.choice(available_modules)
    logging.info(f'Selected {selected_module} for download id {download_request.downloadId}')

    return selected_module