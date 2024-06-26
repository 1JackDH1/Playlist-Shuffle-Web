'''
Script to experiment with the Youtube Data API.
Retrieval of playlist(s) from authenticated account.
'''

# pylint: disable=E1101
# pylint: disable=R0801

import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def get_playlist():
    ''' Function that obtains data of Youtube playlists from account 
    via Google OAuth 2.0 credentials. '''
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

    request = youtube.playlists().list(
        part = "snippet,contentDetails",
        mine = True
    )
    response = request.execute()
    print(response)

if __name__ == "__main__":
    get_playlist()
