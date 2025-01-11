import re

# Define the function to perform the replacement
def replace_ymd_hms_blocks_in_file(input_file, output_file):
    # Regular expression to match the block structure with `ymd_hms`
    pattern = r"(\&\[\s*(?:ymd_hms\([^\)]*\),\s*)+\])"

    # Read the content of the input file
    with open(input_file, 'r') as file:
        content = file.read()

    # Replacement function
    def replace_func(match):
        block = match.group(1)
        # Replace `ymd_hms` with `ymd_hmso` within the matched block
        return block.replace("ymd_hms", "ymd_hmso")

    # Apply the replacement
    updated_content = re.sub(pattern, replace_func, content)

    # Write the updated content to the output file
    with open(output_file, 'w') as file:
        file.write(updated_content)

# Example usage
input_file = 'rrule.rs'  # Replace with the path to your input file
output_file = 'new.rs'  # Replace with the desired path for the output file
replace_ymd_hms_blocks_in_file(input_file, output_file)

print(f"The updated file has been saved as {output_file}.")
