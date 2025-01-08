import json


def convert_format(input_file, output_file):
    """
    Convert the input JSON data to the specified format and save to a new file.

    Args:
        input_file (str): Path to the input JSON file.
        output_file (str): Path to save the converted JSON file.
    """
    # Load the original data
    with open(input_file, "r") as f:
        data = json.load(f)

    # Transform the data
    formatted_data = [
        {
            "instruction": entry["rephrase"],
            "input": "",
            "output": entry["alt"]
        }
        for entry in data
    ]

    # Save the transformed data
    with open(output_file, "w") as f:
        json.dump(formatted_data, f, indent=4)

    print(f"Conversion complete. Transformed data saved to {output_file}")


# Example usage
if __name__ == "__main__":
    input_file_path = "zsre_mend_eval_portability_gpt4.json"  # Replace with your input file path
    output_file_path = "zsre_mend_eval_portability_gpt4_llama_factory_eval.json"  # Replace with your desired output file path
    convert_format(input_file_path, output_file_path)