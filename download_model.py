import gdown
import os

# Google Drive file ID and destination path
file_id = "1YzgNWDV9YMF0rp0nL4G3mIfKPhn8_MhL"
output = "kc_House_prediction.pkl"

# Download only if the file does not exist
if not os.path.exists(output):
    url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(url, output, quiet=False)

