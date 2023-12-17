from PIL import Image
import pytesseract
import sys
import re
import json
import os

def extract_text_from_image(image_path):
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img, lang='eng')
        return text
    except Exception as e:
        return f"Error during text extraction: {e}"

def extract_transaction_id(text):
    transaction_id_patterns = [
        re.compile(r'TXN ID:\s*(\S+)', re.DOTALL),
        re.compile(r'Transaction ID\n\n(\S+)', re.DOTALL),
    ]

    for pattern in transaction_id_patterns:
        match = pattern.search(text)
        if match:
            return match.group(1).strip()

    return None

def process_transactions(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

    for transaction in data['transactions']:
        image_path = transaction.get('image_path')
        expected_transaction_id = transaction.get('expected_transaction_id')

        if image_path and expected_transaction_id:
            print(f"\nProcessing image: {image_path}")
            extracted_text = extract_text_from_image(image_path)

            if "Error" not in extracted_text:
                transaction_id = extract_transaction_id(extracted_text)

                if transaction_id and transaction_id == expected_transaction_id:
                    print(f"Success: \nTransaction ID '{transaction_id}' match found in json file.")
                else:
                    print(f"Failure: \nTransaction ID '{transaction_id}' match not found.")
            else:
                print(f"Cannot process image. {extracted_text}")
        else:
            print("Error: Image path or expected transaction ID not provided in the JSON file.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <json_file>")
    else:
        json_file = sys.argv[1]

        if os.path.isfile(json_file):
            process_transactions(json_file)
        else:
            print(f"Error: The specified JSON file '{json_file}' does not exist.")
