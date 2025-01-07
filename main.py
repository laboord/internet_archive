import csv
import internetarchive as ia
import json
import logging
import os

OUTPUT_FOLDER = './data/'
COLLECTIONS = ['librivoxaudio',]
FIELDS = ['identifier', 'title', 'creator', 'date', 'language',]

logging.basicConfig(
    level=logging.INFO,
    format='[{asctime}] {levelname}: {message}',
    style='{',
    datefmt='%Y/%m/%d %H:%M:%S',
)

class InternetArchiveData():
    def __init__(self, collections):
        self.collections = collections
        self.json_folder = OUTPUT_FOLDER + 'json/'
        self.csv_folder = OUTPUT_FOLDER + 'csv/'
        
        os.makedirs(self.json_folder, exist_ok=True)
        os.makedirs(self.csv_folder, exist_ok=True)
    
    def fetch_metatdata_json(self, collection_id):
        """
        Fetch metadata in JSON and save to a local file.
        """
        logging.info(f'Fetching metadata for collection: {collection_id}')
        
        json_file_path = os.path.join(self.json_folder, f'{collection_id}_metadata.json')
        search_results = ia.search_items(
            f'collection:{collection_id}',
            fields=FIELDS
        )

        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(list(search_results), json_file, ensure_ascii=False, indent=4)
        
        logging.info(f'Metadata saved as JSON: {json_file_path}')
        
        return json_file_path
    
    def convert_json_to_csv(self, json_file_path, collection_id):
        """
        Convert the JSON metadata file to CSV file.
        """
        logging.info(f'Converting JSON to CSV for collection: {collection_id}')
        
        csv_file_path = os.path.join(self.csv_folder, f'{collection_id}_metadata.csv')

        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            items = json.load(json_file)
        
        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(FIELDS)
            for item in items:
                row = [item.get(field, '') for field in FIELDS]
                writer.writerow(row)
        
        logging.info(f'Metadata saved as csv: {csv_file_path}')
        
        return csv_file_path

if __name__ == '__main__':
    ia_data = InternetArchiveData(COLLECTIONS)
    for collection in COLLECTIONS:
        json_file = ia_data.fetch_metatdata_json(collection)
        ia_data.convert_json_to_csv(json_file, collection)
