# Instructions to Edit and Run the App Locally

This repository contains code for an app. Follow the steps below to edit and run the app on your local machine.

## Running the App Locally

To run the app locally, follow these steps:

1. Clone the repository and extract the files to your desired location.

2. Navigate to the project directory in your terminal.

3. Create a virtual environment by running the following command:

    ```
    python3 -m venv .venv
    ```

4. Activate the virtual environment:

    - On Windows:
    
        ```
        .venv\Scripts\activate
        ```

    - On macOS and Linux:
    
        ```
        source .venv/bin/activate
        ```

5. Install the necessary libraries by running the following command:

    ```
    pip install -r requirements.txt
    ```

6. Download the en_core_web_sm model using spaCy's command line interface:

    ```
    python -m spacy download en_core_web_sm
    ```

7. Run the following command in the terminal to start the app:

    ```
    streamlit run app.py
    ```


8. You can now interact with the app locally.


## Interface
<img width="1433" alt="image" src="https://github.com/meetarthi/search_wiki/assets/112666126/f7319b2c-1863-4aec-89c2-3c7ec0d89999">

