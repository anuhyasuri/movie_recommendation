import pandas as pd
import logging
from tqdm import tqdm
import httpx
import pathlib

def store_data_from_wiki():
    try:
        base_url:str = "<link to the dataset>"
        start:int = 1970
        end:int = 2020
        sample = 1.0
        path = "./raw_data/"
        decades = [start+(i*10) for i in range(int((end-start)/10)+1)]
        results =[]
        for decade in tqdm(decades, colour="cyan"):
            response = httpx.get(url=base_url.format(decade),follow_redirects=True)
            logging.info(f"Respose status: {response.status_code}")
            logging.info(f"Response text: {response.text}")
            movies_json = response.json()
            movies_df = pd.DataFrame.from_dict(movies_json)
            results.append(movies_df)
        movies_df = pd.concat(results, axis=0)
        path = pathlib.Path(path)
        target_path = f"{str(path)}/movies.json"
        if sample < 1.0:
            movies_df = movies_df.sample(frac=sample)
        print(target_path)
        movies_df.to_json(target_path, orient="records")
    except Exception as exception:
        logging.error(f"Error: {str(exception)}")
        raise exception

store_data_from_wiki()
