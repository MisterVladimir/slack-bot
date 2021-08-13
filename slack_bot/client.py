import os
from typing import List

import requests
from slack import WebClient

SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
# Create a slack client
slack_web_client = WebClient(token=SLACK_BOT_TOKEN)

all_channels = slack_web_client.api_call(
    "conversations.list", params={"types": "private_channel"}
)
private_channel_ids = {
    channel["name"]: channel["id"]
    for channel in all_channels.data["channels"]
    if channel["is_private"]
}

files_in_private_channels = [
    slack_web_client.api_call(
        "files.list", params={"channel": id_}
    )
    for id_ in private_channel_ids.values()
]
public_files_in_private_channels = [
    file
    for private_channel_files in files_in_private_channels
    for file in private_channel_files.data['files']
    if file['is_public']
]
public_file_urls = [file["url_private_download"] for file in public_files_in_private_channels]
public_images: List[bytes] = [
    requests.get(file_url, headers={'Authorization': f'Bearer {SLACK_BOT_TOKEN}'}).content
    for file_url in
    public_file_urls
]
print()  # placeholder for breakpoint
