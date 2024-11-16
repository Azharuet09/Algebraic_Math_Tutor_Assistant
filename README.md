
# Algebraic Math Tutor Assistant

## Overview
The **Algebraic Math Tutor Assistant** is a Streamlit web application powered by using Prompt Engineering Techniques. It specializes in solving algebra-related problems and providing step-by-step explanations. This tool is designed to help students, educators, and enthusiasts gain a deeper understanding of algebraic concepts through detailed, interactive solutions.


## Prerequisites
1. **OpenAI API Key**: You need a valid API key from OpenAI.
2. **Python Environment**: Ensure Python 3.8 or higher is installed.


### Step 1: Set Up a Virtual Environment

#### For Windows
1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:
   ```bash
   .\venv\Scripts\activate
   ```

#### For Ubuntu
1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```
2. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

### Step 2: Install Dependencies
Install the required Python libraries using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### Step 3: Set Up the Environment
1. Create a `.env` file in the root directory. I am providing you the ```sample.env.txt``` file, just open it and set the API key accordingly.
2. Add your OpenAI API key:
   ```
   OPENAI_API_KEY=your-api-key-here
   ```
## Usage

### Step 4: Run the Application
Start the Streamlit app with the following command:
```bash
streamlit run app.py
```

### Step 2: Interact with the Application
1. Enter your algebra problem in the text input field.
2. Click the **Solve** button.
3. View the detailed solution and explanation.


## Example Usage
1. **Input**: `Solve for x: 2x + 3 = 7`
2. **Output**:
   ```
   Step 1: Subtract 3 from both sides: 2x = 4
   Step 2: Divide both sides by 2: x = 2
   ```
