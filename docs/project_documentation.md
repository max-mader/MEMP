# Project Documentation

This documentation provides an overview of the LLM Prompt Optimization project. It includes information about the project structure, file descriptions, and usage instructions.

## Project Structure

The project follows the following directory structure:

```
LLM-Prompt-Optimisation
├── src
│   ├── extract_meta.py
│   ├── create_memp.py
│   ├── evaluate_memp.py
│   └── main.py
├── tests
│   ├── test_extract_meta.py
│   ├── test_create_memp.py
│   └── test_evaluate_memp.py
├── data
│   ├── raw_responses.txt
│   └── processed_prompts.txt
├── docs
│   └── project_documentation.md
├── .gitignore
├── requirements.txt
└── README.md
```

The project consists of the following files and directories:

- `src`: This directory contains the source code files for the project.
  - `extract_meta.py`: This file contains the code for extracting meta-information from LLM responses. It includes functions to identify key components and reflect the model's understanding.
  - `create_memp.py`: This file contains the code for creating a Minimal Edit Meta-Prompt (MEMP) based on the first paragraph of an LLM's response. It includes functions to formulate the MEMP and generate short bullet points.
  - `evaluate_memp.py`: This file contains the code for evaluating and rating different versions of the Minimal Edit Meta-Prompt. It includes functions to rate the effectiveness of each transformation and determine the overall better version.
  - `main.py`: This file is the main entry point of the project. It includes the code to execute the prompt optimization process, calling the functions from the other modules.

- `tests`: This directory contains the unit test files for the project.
  - `test_extract_meta.py`: This file contains unit tests for the `extract_meta.py` module.
  - `test_create_memp.py`: This file contains unit tests for the `create_memp.py` module.
  - `test_evaluate_memp.py`: This file contains unit tests for the `evaluate_memp.py` module.

- `data`: This directory contains the data files used in the project.
  - `raw_responses.txt`: This file contains the raw LLM responses that will be used for prompt optimization.
  - `processed_prompts.txt`: This file contains the processed prompts that will be used for creating the Minimal Edit Meta-Prompt.

- `docs`: This directory contains the project documentation files.
  - `project_documentation.md`: This file contains the documentation for the project, including an overview, usage instructions, and explanations of the different modules.

- `.gitignore`: This file specifies the files and directories that should be ignored by version control.

- `requirements.txt`: This file lists the dependencies required for the project.

- `README.md`: This file contains the README for the project, providing an introduction, installation instructions, and usage examples.

## Usage

To use the LLM Prompt Optimization project, follow these steps:

1. Install the required dependencies listed in `requirements.txt`.

2. Place the raw LLM responses in the `data/raw_responses.txt` file.

3. Run the `main.py` script in the `src` directory to execute the prompt optimization process.

4. The optimized prompts will be generated and saved in the `data/processed_prompts.txt` file.

5. Use the optimized prompts for further interactions with the LLM.

For more detailed information on each module and its functionality, refer to the respective source code files and the project documentation.

## Conclusion

The LLM Prompt Optimization project provides a framework for extracting meta-information from LLM responses and creating Minimal Edit Meta-Prompts. By optimizing the prompts, the project aims to enhance the clarity and effectiveness of interactions with the LLM.