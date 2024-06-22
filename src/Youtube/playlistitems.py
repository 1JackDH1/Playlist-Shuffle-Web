'''
Retrieval of playlist videos from authenticated account.
'''

# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=R0801

import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
video_list = []


def get_playlist_items(playlistID):
    ''' Function that retrieves video items from select Youtube playlist, 
    from account via Google OAuth 2.0 credentials. '''
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = input("Filename for OAuth 2.0 credentials:\n")

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    # run_console deprecated in newer versions of Google OAuth - replaced with run_local_server
    credentials = flow.run_local_server()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.playlistItems().list(
        part = "contentDetails",
        playlistId = playlistID,
        maxResults = 50
    )
    response = request.execute()
    next_page_token = extract_data(response)
    
    while True:
        try:
            request = youtube.playlistItems().list(
                part = "contentDetails",
                playlistId = playlistID,
                maxResults = 50,
                pageToken = next_page_token
            )
            response = request.execute()
            next_page_token = extract_data(response)
        except KeyError:
            break
    print(len(video_list))


def extract_data(full_data):
    ''' Function for extracting proceeding page tokens and video IDs
    from content details '''
    for item in full_data["items"]:
        video_list.append(item["contentDetails"]["videoId"])
    next_page_token = full_data["nextPageToken"]
    return next_page_token


if __name__ == "__main__":
    get_playlist_items(input("Provide playlist ID:\n"))
