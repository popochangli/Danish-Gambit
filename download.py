import requests

# URL of the Lichess database (January 2024)
URL = "https://database.lichess.org/standard/lichess_db_standard_rated_2020-01.pgn.zst"
FILENAME = "lichess_partial_2020-01.pgn.zst"  # Output file
MAX_SIZE_MB = 500  # Change this to adjust the partial size
MAX_BYTES = MAX_SIZE_MB * 1024 * 1024  # Convert to bytes

def partial_download(url, filename, max_bytes):
    response = requests.get(url, stream=True)
    downloaded = 0

    with open(filename, "wb") as file:
        for chunk in response.iter_content(chunk_size=1024*1024):  # Download in 1MB chunks
            if downloaded + len(chunk) > max_bytes:
                file.write(chunk[:max_bytes - downloaded])  # Write only the remaining allowed part
                break
            file.write(chunk)
            downloaded += len(chunk)

    print(f"Partial download complete: {filename} ({downloaded / (1024*1024)} MB)")

if __name__ == "__main__":
    partial_download(URL, FILENAME, MAX_BYTES)
