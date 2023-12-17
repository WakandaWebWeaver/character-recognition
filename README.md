# Payment Verification Script

This Python script processes payment images and verifies whether the extracted transaction ID matches the expected ID specified in a JSON file.

## Requirements

- Python 3.x
- Pillow library (PIL fork) for image processing
- [Tesseract](https://tesseract-ocr.github.io/tessdoc/Installation.html) OCR engine (Make sure Tesseract is installed and its executable is in the system PATH)

## Usage

1. Clone the repository or download the script.
2. Install the required dependencies:

    ```
    pip install pillow
    ```
- To install Tesseract on a Mac, run
  ```
  brew install tesseract
  ```
  in a shell.
3. Run the script with the JSON file containing payment information:

    ```
    python/python3 script.py transfers.json
    ```

### JSON File Format

The 'transfers.json' file should have the following structure:

```
{
  "transactions": [
    {
      "image_path": "payment1.png",
      "expected_transaction_id": "T1234567890"
    },
    {
      "image_path": "payment2.png",
      "expected_transaction_id": "T9876543210"
    },
    {
      "image_path": "payment3.png",
      "expected_transaction_id": "T5678901234"
    }
  ]
}
```

- Each transaction includes an "image_path" representing the payment image path.
- It also includes an "expected_transaction_id" representing the expected transaction ID.

## Output

- For each processed image, the script will print success if the transaction ID matches the expected ID.
- If there is no match or an error occurs during processing, it will print a failure message
