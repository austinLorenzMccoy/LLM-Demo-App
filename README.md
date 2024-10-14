# Austin's LLM Application Documentation

Welcome to **Austin's LLM Application**, a demo Streamlit-based application that integrates Google's Generative AI (Gemini model) and Google Cloud Vision API to provide an interactive Q&A chatbot with image processing capabilities.

This documentation provides comprehensive guidance on setting up, configuring, and using the application. It covers the three primary scripts involved in the application:

1. [`app.py`](#1-apppy)
2. [`vision.py`](#2-visionpy)
3. [`qachat.py`](#3-qachatpy)

---

## Table of Contents

1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Setup Instructions](#setup-instructions)
4. [Configuration](#configuration)
5. [Script Overview](#script-overview)
    - [1. app.py](#1-apppy)
    - [2. vision.py](#2-visionpy)
    - [3. qachat.py](#3-qachatpy)
6. [Running the Application](#running-the-application)
7. [Usage Guide](#usage-guide)
8. [Troubleshooting](#troubleshooting)
9. [Additional Recommendations](#additional-recommendations)
10. [Contact and Support](#contact-and-support)

---

## Introduction

**Austin's LLM Application** is an interactive chatbot built using Streamlit that leverages Google's Generative AI (Gemini model) for natural language understanding and generation, alongside the Google Cloud Vision API for image processing. The application allows users to ask questions, upload images, and receive detailed responses based on their inputs.

---

## Prerequisites

Before setting up the application, ensure you have the following:

1. **Python 3.8 or higher** installed on your machine.
2. **Google Cloud Account** with the following APIs enabled:
    - [Google Generative AI (Gemini)](https://developers.generativeai.google/)
    - [Google Cloud Vision API](https://cloud.google.com/vision)
3. **Service Account Credentials** for Google Cloud Vision API.
4. **Git** installed for version control (optional but recommended).

---

## Setup Instructions

Follow these steps to set up the application:

### 1. Clone the Repository (Optional)

If the application is hosted on a version control system like GitHub, clone the repository:

```bash
git clone https://github.com/yourusername/LLM_project.git
cd LLM_project/geminiLLMapp
```

*Replace `yourusername` and the repository URL with your actual GitHub username and repository link.*

### 2. Create a Virtual Environment

It's best practice to use a virtual environment to manage dependencies:

```bash
python3 -m venv venv
```

### 3. Activate the Virtual Environment

- **On macOS and Linux:**

    ```bash
    source venv/bin/activate
    ```

- **On Windows:**

    ```bash
    venv\Scripts\activate
    ```

### 4. Install Required Packages

Install all necessary Python packages using `pip`:

```bash
pip install -r requirements.txt
```

*If a `requirements.txt` file is not provided, manually install the required packages:*

```bash
pip install streamlit google-generativeai google-cloud-vision python-dotenv Pillow watchdog
```

---

## Configuration

Proper configuration is crucial for the application to interact with Google APIs securely and effectively.

### 1. Setting Up Google Cloud Credentials

#### a. **Create a Service Account for Vision API**

1. **Navigate to Google Cloud Console:**

    Visit the [Google Cloud Console](https://console.cloud.google.com/).

2. **Select or Create a Project:**

    Ensure you're working within the correct project where the Vision API and Generative AI are enabled.

3. **Enable APIs:**

    - **Cloud Vision API:**
        - Go to **APIs & Services** > **Library**.
        - Search for **Cloud Vision API** and enable it.
    - **Google Generative AI (Gemini):**
        - Similarly, search for **Google Generative AI** and enable it.

4. **Create a Service Account:**

    - Navigate to **IAM & Admin** > **Service Accounts**.
    - Click **Create Service Account**.
    - Provide a name and description.
    - Assign the **Vision API User** role.
    - Click **Done**.

5. **Generate a Key for the Service Account:**

    - In the **Service Accounts** list, find your newly created account.
    - Click on it, then go to the **Keys** tab.
    - Click **Add Key** > **Create New Key**.
    - Select **JSON** and click **Create**.
    - Download the JSON key file and store it securely.

#### b. **Set Environment Variables**

Create a `.env` file in the root directory of your project (`geminiLLMapp`) and add the following:

```env
GOOGLE_API_KEY="AIzaSyCBUl8J-cB4sEdB0x1..."
GOOGLE_APPLICATION_CREDENTIALS="/absolute/path/to/your/credentials.json"
```

- **`GOOGLE_API_KEY`:** Your actual API key for Google Generative AI.
- **`GOOGLE_APPLICATION_CREDENTIALS`:** The absolute path to the JSON key file you downloaded for the Vision API.

*Example:*

```env
GOOGLE_API_KEY="AIzaSyCBUl8J-cB4sEdB0x1..."
GOOGLE_APPLICATION_CREDENTIALS="/Users/a/Downloads/DataScience_World/LLM_project/geminiLLMapp/credentials.json"
```

**Important:** Ensure the `.env` file is **not** tracked by version control to protect your sensitive information. Add `.env` to your `.gitignore` file:

```gitignore
# .gitignore
.env
```

---

## Script Overview

The application consists of three primary scripts:

1. [`app.py`](#1-apppy)
2. [`vision.py`](#2-visionpy)
3. [`qachat.py`](#3-qachatpy)

Each script serves a specific purpose within the application.

### 1. app.py

**Note:** Based on the provided conversation, `app.py` seems to be an earlier or alternate version of the main application. For clarity and to avoid confusion, focus on using `qachat.py` as the primary application script. However, if `app.py` serves a distinct purpose, ensure its documentation aligns accordingly.

### 2. vision.py

**Purpose:** Handles image processing by interacting with the Google Cloud Vision API to generate descriptive labels for uploaded images.

### 3. qachat.py

**Purpose:** Acts as the main Streamlit application script, providing an interactive Q&A interface that integrates both text inputs uploads to generate responses using Google's Gemini model with history.


**Explanation:**

- **Environment Variables:** Loads `GOOGLE_API_KEY` and `GOOGLE_APPLICATION_CREDENTIALS` from the `.env` file.
- **API Configuration:** Configures both Google Generative AI and Vision API using the provided credentials.
- **Model Loading:** Uses Streamlit's caching to load the Gemini model efficiently.
- **Image Processing:** Utilizes `describe_image` function from `vision.py` to extract descriptive labels from uploaded images.
- **Chatbot Functionality:** Implements a chat interface where users can input text, upload images, or both, and receive responses generated by the Gemini model.
- **Session State:** Maintains chat history across interactions using Streamlit's session state.
- **Error Handling:** Includes comprehensive error handling to manage API errors and invalid inputs gracefully.

---

## Running the Application

After setting up and configuring the environment, follow these steps to run the application:

1. **Activate the Virtual Environment:**

    ```bash
    source venv/bin/activate
    ```

2. **Set Environment Variables:**

    Ensure your `.env` file is correctly set up with the necessary environment variables.

3. **Run the Streamlit App:**

    ```bash
    streamlit run qachat.py
    ```

    *Note:* Replace `qachat.py` with `app.py` or `vision.py` if you intend to run them separately. However, based on the provided scripts, `qachat.py` serves as the main application script.

4. **Access the Application:**

    Open your browser and navigate to the **Local URL** (typically `http://localhost:8501`) displayed in the terminal to interact with the app.

---

## Usage Guide

### 1. **Launching the App**

Upon running the Streamlit app, you'll see a web interface with the following components:

- **Header:** "Austin's LLM Application"
- **Input Field:** For entering text prompts/questions.
- **Image Uploader:** To upload images (`.jpg`, `.jpeg`, `.png` formats).
- **Submit Button:** "Tell me about the image"
- **Chat History:** Displays the conversation history between the user and the bot.

### 2. **Interacting with the Chatbot**

- **Text Input:**
    - Enter a question or prompt in the input field.
    - Example: "What is the capital of France?"

- **Image Upload:**
    - Upload an image using the uploader.
    - Example: Upload a picture of the Eiffel Tower.

- **Combined Input:**
    - Provide both text and an image to receive a more contextual response.
    - Example: "Describe this landmark." + Upload an image of the Eiffel Tower.

- **Generating Response:**
    - Click the "Tell me about the image" button to receive a response.
    - The bot will process the input and display the response in real-time.
    - The chat history will update accordingly, showing both user inputs and bot responses.

### 3. **Viewing Chat History**

- The **Chat History** section displays the entire conversation, allowing you to review previous interactions.

---

## Troubleshooting

### Common Errors and Solutions

1. **`ModuleNotFoundError: No module named 'google.generativeai'`**

    **Cause:** The `google-generativeai` package is not installed in your virtual environment.

    **Solution:**

    ```bash
    pip install google-generativeai
    ```

2. **`DefaultCredentialsError: Your default credentials were not found.`**

    **Cause:** The application cannot locate the Google Cloud credentials required for the Vision API.

    **Solution:**

    - Ensure that the `GOOGLE_APPLICATION_CREDENTIALS` environment variable is set correctly in your `.env` file.
    - Verify the path to your service account JSON key file.
    - Example `.env` entry:

        ```env
        GOOGLE_APPLICATION_CREDENTIALS="/absolute/path/to/your/credentials.json"
        ```

    - Alternatively, set the environment variable directly in your terminal:

        ```bash
        export GOOGLE_APPLICATION_CREDENTIALS="/absolute/path/to/your/credentials.json"
        ```

3. **`StreamlitSetPageConfigMustBeFirstCommandError`**

    **Cause:** `st.set_page_config()` is not the first Streamlit command in your script.

    **Solution:**

    - Ensure that `st.set_page_config()` is placed immediately after all import statements and before any other Streamlit commands.

    - Example:

        ```python
        import streamlit as st
        from dotenv import load_dotenv
        load_dotenv()

        st.set_page_config(page_title="Q&A Demo", page_icon="💬")
        ```

4. **`ModuleNotFoundError: No module named 'IPython'`**

    **Cause:** The `IPython` package is not installed, but it's being imported in your script.

    **Solution:**

    - Install the `IPython` package:

        ```bash
        pip install ipython
        ```

    - *Note:* If `IPython` is not essential for your application, consider removing the import statements related to it to avoid unnecessary dependencies.

5. **Deprecation Error:**

    ```
    google.api_core.exceptions.NotFound: 404 Gemini 1.0 Pro Vision has been deprecated on July 12, 2024. Consider switching to different model, for example gemini-1.5-flash.
    ```

    **Cause:** Using a deprecated Gemini model.

    **Solution:**

    - Update the model reference in your script to use a supported model like `gemini-1.5-flash`.

    - Example:

        ```python
        model = genai.GenerativeModel("gemini-1.5-flash")
        ```

### Additional Tips

- **Clear Streamlit Cache:**

    Sometimes, cached data can cause unexpected behaviors. Clear the cache using:

    ```bash
    streamlit cache clear
    ```

- **Check API Quotas:**

    Ensure you haven't exceeded your Google Cloud API quotas, which could prevent the application from making successful API calls.

- **Verify File Paths:**

    Double-check all file paths, especially for environment variables pointing to credentials files.

---

## Additional Recommendations

### 1. **Security Best Practices**

- **Protect API Keys and Credentials:**

    - Never expose your `.env` file or credentials in public repositories.
    - Use environment variables to manage sensitive information securely.

- **Use `.gitignore`:**

    Ensure your `.gitignore` includes the `.env` file and any credential files to prevent accidental commits.

    ```gitignore
    # .gitignore
    .env
    *.json
    ```

### 2. **Optimizing Performance**

- **Image Processing:**

    - Resize and compress images before processing to reduce API latency.
    - Implement asynchronous processing if dealing with large volumes of images.

- **Caching:**

    Utilize Streamlit's caching mechanisms (`@st.cache_resource`, `@st.cache_data`) to store and reuse expensive computations or API calls.

### 3. **Enhancing User Experience**

- **Responsive Layouts:**

    Use Streamlit's layout features like `st.columns()`, `st.sidebar()`, and `st.expander()` to create a more organized and user-friendly interface.

- **Progress Indicators:**

    Implement spinners or progress bars to inform users about ongoing processes.

    ```python
    with st.spinner("Generating response..."):
        # API call or processing
    ```

- **Error Messages:**

    Provide clear and actionable error messages to guide users in resolving issues.

### 4. **Logging and Monitoring**

- **Implement Logging:**

    Use Python's `logging` module to track application behavior and debug issues.

    ```python
    import logging

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    logger.info("Application started")
    ```

- **Monitor API Usage:**

    Regularly monitor your Google Cloud API usage to manage costs and ensure availability.

### 5. **Extending Functionality**

- **Support More Image Features:**

    Explore additional features of the Vision API, such as OCR, face detection, or object localization, to enhance the application's capabilities.

- **Interactive Chat Features:**

    Implement features like context retention, follow-up questions, or multi-turn conversations to create a more engaging chatbot experience.

---

## Contact and Support

For further assistance or to report issues, please contact:

- **Austin**
- **Email:** austin@example.com
- **GitHub:** [github.com/yourusername](https://github.com/yourusername)

*Replace `austin@example.com` and `yourusername` with your actual contact information and GitHub profile.*

---

# Appendix

### 1. `requirements.txt` Example

Create a `requirements.txt` file in the root directory with the following content to manage dependencies:

```
streamlit
google-generativeai
google-cloud-vision
python-dotenv
Pillow
watchdog
ipython
```

**Installation:**

```bash
pip install -r requirements.txt
```

### 2. `.env` File Example

```env
GOOGLE_API_KEY="AIzaSyCBUl8J-cB4sEdB0x1..."
GOOGLE_APPLICATION_CREDENTIALS="/absolute/path/to/your/credentials.json"
```

**Note:** Ensure that the path to the credentials JSON file is absolute and correctly points to the file's location.

---

# Final Notes

This documentation aims to provide a clear and comprehensive guide to setting up and using **Austin's LLM Application**. By following the outlined steps and adhering to best practices, you can ensure a smooth and secure experience while interacting with the application.

Should you encounter any challenges or require further customization, refer to the official documentation of the respective tools and APIs:

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Google Generative AI Documentation](https://developers.generativeai.google/)
- [Google Cloud Vision API Documentation](https://cloud.google.com/vision/docs)

Happy Chatting!
