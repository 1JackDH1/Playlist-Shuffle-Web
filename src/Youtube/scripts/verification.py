''' Verification and use case checks for user input and external files '''

# pylint: disable=W0718

import os

def credential_file_verification() -> str:
    ''' Verification of user input file. Checking for FileNotFoundError
    and if the file provided is empty. '''
    while True:
        try:
            client_secrets_file = input("Filename for OAuth 2.0 credentials:\n")
            client_file_size = os.stat(client_secrets_file).st_size
            if client_file_size == 0:
                print("File provided is empty.")
        except FileNotFoundError:
            print("File not found or incompatible.")
        else:
            break
    return client_secrets_file