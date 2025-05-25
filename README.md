# CSV-cleaning-using-LLMs

A simple Python script for cleaning CSV files using the power of Large Language Models (LLMs).

## Overview

This project aims to leverage LLMs to identify and correct common data quality issues within CSV files, such as inconsistent formatting, typos, and missing values.

## Getting Started

### Prerequisites

* Python 3.x
* `pandas` library
* An API key for your chosen LLM provider (e.g., OpenAI, Google Gemini). You will need to set this up as an environment variable or configure it directly within the script.

### Installation

1.  Clone this repository:
    ```bash
    git clone [https://github.com/your-username/CSV-cleaning-using-LLMs.git](https://github.com/your-username/CSV-cleaning-using-LLMs.git)
    cd CSV-cleaning-using-LLMs
    ```
2.  Install the required Python libraries:
    ```bash
    pip install pandas
    ```
3.  Install the specific LLM library you intend to use (e.g., `openai`, `google-generativeai`):
    ```bash
    pip install openai # Or pip install google-generativeai
    ```

### Usage

1.  **Prepare your CSV file:** Ensure your CSV file is in the root directory of the project or provide the full path to it within the `main.py` script.
2.  **Configure your LLM API Key:**
    * **Recommended (Environment Variable):** Set your API key as an environment variable (e.g., `OPENAI_API_KEY`, `GOOGLE_API_KEY`).
    * **Directly in code (Less Recommended):** If you absolutely must, you can hardcode your API key in the `main.py` file (though this is not recommended for security reasons).
3.  **Run the script:**
    ```bash
    python main.py your_input_file.csv your_output_file.csv
    ```
    Replace `your_input_file.csv` with the name of your CSV file to be cleaned, and `your_output_file.csv` with the desired name for the cleaned output.

## Testing

To test the functionality of the script, you can:

1.  **Create a sample CSV file** with known data quality issues. For example:

    `sample_dirty.csv`
    ```csv
    Name,Age,City
    John Doe,30,NewYork
    Jane Smith,25,london
    Bob,40,Paris,France
    Alice, ,Berlin
    Charlie,35,NYC
    ```

2.  **Run the script** with this sample file:

    ```bash
    python main.py sample_dirty.csv sample_cleaned.csv
    ```

3.  **Inspect `sample_cleaned.csv`** to verify that the LLM has correctly identified and cleaned the data. Expected improvements might include:
    * Correcting "london" to "London".
    * Handling the extra column in "Bob,40,Paris,France".
    * Attempting to fill the missing age for "Alice".
    * Normalizing "NYC" to "New York City" (depending on LLM configuration).

## Contributing

Currently, contributions are not being actively sought for this very simple initial version. However, feel free to fork the repository and experiment!

## License

[MIT License](LICENSE) (You'll need to create a `LICENSE` file in your repository with the MIT license text)