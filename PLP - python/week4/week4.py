import sys

def process_file():
    input_filename = input("Enter the name of the input file (e.g., input.txt): ")
    
    # Use a try...except block to gracefully handle file-related errors.
    try:
        with open(input_filename, 'r') as input_file:
            original_content = input_file.read()
        
        print(f"\nSuccessfully read content from '{input_filename}'.")
        print("Original content:")
        print("--------------------")
        print(original_content)
        print("--------------------")

        modified_content = original_content.upper()
        output_filename = input(f"Enter the name for the new output file (e.g., {input_filename.split('.')[0]}_modified.txt): ")
        
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
            
        print(f"\nSuccessfully wrote the modified content to '{output_filename}'.")

    # Error handling for specific scenarios.
    except FileNotFoundError:
        print(f"\nError: The file '{input_filename}' was not found.")
        print("Please check the filename and try again.")
    except IOError as e:
        print(f"\nAn I/O error occurred: {e}")
        print("You may not have the necessary permissions to read the file.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

# Run the program
if __name__ == "__main__":
    process_file()

