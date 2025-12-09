import csv
import json

# Since the file is large, we will process it in chunks
# However, since this is a JSON file, we need to read the whole file to parse it.
# The previous attempt to read the whole file failed because it was too large.
# Let's try to read the file line by line and construct the JSON object.

with open(
    "D:\\writing\\clirnet\\econnect\\data_content_project.json", encoding="utf-8"
) as f:
    data = json.load(f)

with open(
    "D:\\writing\\clirnet\\econnect\\content_data.csv",
    "w",
    newline="",
    encoding="utf-8",
) as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["content ID", "content name", "content description"])
    for item in data["data"]["project_contents"]:
        if item.get("fetch_with_contents"):
            # The 'fetch_with_contents' is a list, so we need to iterate over it
            for content_item in item.get("fetch_with_contents"):
                writer.writerow(
                    [
                        content_item.get("content_id"),
                        content_item.get("content_title"),
                        content_item.get("content_description"),
                    ]
                )
