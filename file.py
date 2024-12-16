def read_and_write_file():
    try:
        input_file = input("Enter the name of the file to read: ")

        with open(input_file, 'r') as file:
            content = file.readlines()
        
        print("File read successfully!")

        modified_content = [line.upper() for line in content]

        output_file = input("Enter the name of the file to write to: ")

        with open(output_file, 'w') as file:
            file.writelines(modified_content)
        
        print(f"Modified content written to {output_file} successfully!")

    except FileNotFoundError:
        print("Error: The file you specified does not exist. Please try again.")
    except IOError as e:
        print(f"Error: An I/O error occurred - {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    read_and_write_file()
