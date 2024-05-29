# LLM Prompt Optimisation

This project aims to optimize prompts for Large Language Models (LLMs) by extracting meta-information from LLM responses and creating Minimal Edit Meta-Prompts (MEMPs). The MEMPs represent the ideal prompts that the LLM would prefer to be given for similar tasks, enhancing the model's understanding and execution.

## Project Structure

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

- `src/extract_meta.py`: Contains code for extracting meta-information from LLM responses. Includes functions to identify key components and reflect the model's understanding.
- `src/create_memp.py`: Contains code for creating MEMPs based on the first paragraph of LLM responses. Includes functions to formulate the MEMPs and generate short bullet points.
- `src/evaluate_memp.py`: Contains code for evaluating and rating different versions of MEMPs. Includes functions to rate the effectiveness of each transformation and determine the overall better version.
- `src/main.py`: Main entry point of the project. Executes the prompt optimization process by calling functions from other modules.
- `tests/test_extract_meta.py`: Unit tests for the `extract_meta.py` module.
- `tests/test_create_memp.py`: Unit tests for the `create_memp.py` module.
- `tests/test_evaluate_memp.py`: Unit tests for the `evaluate_memp.py` module.
- `data/raw_responses.txt`: Raw LLM responses used for prompt optimization.
- `data/processed_prompts.txt`: Processed prompts used for creating MEMPs.
- `docs/project_documentation.md`: Documentation for the project, including an overview, usage instructions, and explanations of the different modules.
- `.gitignore`: Specifies files and directories to be ignored by version control.
- `requirements.txt`: Lists project dependencies.
- `README.md`: This file, providing an introduction, installation instructions, and usage examples.

## Installation

To use this project, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/LLM-Prompt-Optimisation.git`
2. Install the required dependencies: `pip install -r requirements.txt`

## Usage

1. Prepare the raw LLM responses in `data/raw_responses.txt`.
2. Run the prompt optimization process by executing `src/main.py`.
3. The optimized MEMPs will be generated and stored in `data/processed_prompts.txt`.
4. Evaluate the MEMPs using `src/evaluate_memp.py` to determine the better version.
5. Refer to the project documentation in `docs/project_documentation.md` for more details.

## Contributing

Contributions are welcome! Please refer to the [contribution guidelines](docs/contributing.md) for more information.

## License

This project is licensed under the [MIT License](LICENSE).