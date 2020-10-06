import cloudsync

prov = cloudsync.create_provider("onedrive")
creds = prov.authenticate()
prov.connect(creds)
with open("/my/local/file", "wb") as f:
    prov.download_path("/path/to/file/on/onedrive", f):