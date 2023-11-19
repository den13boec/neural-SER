import os
import kaggle


def cut_of_beginning(url: str) -> str:
    res: str = url.strip()
    if url.startswith("https://www.kaggle.com/datasets"):
        res = res.replace("https://www.kaggle.com/datasets/", "")
    return res

def download_datasets(urls: list[str]):
    base_dir = "./data"

    # Create the base directory if it doesn't exist
    os.makedirs(base_dir, exist_ok=True)

    # Set the Kaggle API credentials
    kaggle.api.authenticate()

    for url in urls:
        dataset_name = cut_of_beginning(url)
        
        # Create the dataset directory
        dataset_folder = dataset_name.split("/")[-1]
        dataset_dir = os.path.join(base_dir, dataset_folder)
        os.makedirs(dataset_dir, exist_ok=True)

        # Download the dataset
        kaggle.api.dataset_download_files(
            dataset_name, path=dataset_dir, unzip=True)

        print(f"Downloaded {dataset_name} to {dataset_dir}")


# List of Kaggle dataset URLs
urls = [
    "https://www.kaggle.com/datasets/ejlok1/toronto-emotional-speech-set-tess",
    "https://www.kaggle.com/datasets/ejlok1/surrey-audiovisual-expressed-emotion-savee",
    "https://www.kaggle.com/datasets/uwrfkaggler/ravdess-emotional-speech-audio",
    "https://www.kaggle.com/datasets/ejlok1/cremad"
]

download_datasets(urls)
