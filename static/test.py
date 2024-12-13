def create_header_id_dict(json_data):
    # Create a dictionary with header as key and id as value
    header_id_dict = {}
    
    for item in json_data:
        header = item['header']
        id = item['id']
        header_id_dict[header] = id
        
    return header_id_dict

# Sample usage:
import json

# Read the JSON file
with open(r"D:\Files\@PreviousProjects\UH-1\uh-1.github.io\static\data_list_config.json", 'r') as f:
    data = json.load(f)

# Create the header-id dictionary
result = create_header_id_dict(data)

# Print the result
print(json.dumps(result, indent=4))
