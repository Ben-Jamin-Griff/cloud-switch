import cloudsync

# Get a generic client_id and client_secret. Do not use this in production code.
# For more information on getting your own client_id and client_secret, see README_OAUTH.md
oauth_config = cloudsync.command.utils.generic_oauth_config('gdrive')

# get an instance of the gdrive provider class
provider = cloudsync.create_provider('gdrive', oauth_config=oauth_config)

# Start the oauth process to login in to the cloud provider
creds = provider.authenticate()

# Use the credentials to connect to the cloud provider
provider.connect(creds)

# Perform cloud operations
for entry in provider.listdir_path("/"):
    print(entry.path)