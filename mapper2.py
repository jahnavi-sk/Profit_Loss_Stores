import sys
import json

def process_large_json():
    try:
        # Initialize variables to handle JSON object parsing
        buffer = ""
        for line in sys.stdin:
            buffer += line.strip()
            
            # Try to parse the buffer as a JSON object
            try:
                data = json.loads(buffer)
                if isinstance(data, dict):
                    city = data.get('city')
                    if city:
                        print(city)
                elif isinstance(data, list):
                    for item in data:
                        if isinstance(item, dict):
                            city = item.get('city')
                            if city:
                                print(city)
                # Reset buffer after successful parse
                buffer = ""
            except json.JSONDecodeError:
                # Continue reading lines until a valid JSON object is complete
                continue
    except Exception as e:
        print(f"An error occurred: {e}")

process_large_json()
print("\nProcessing completed.")
