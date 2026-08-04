import zipfile

zip_path = "datasets/HCS.zip"
parsed_tags = []

with zipfile.ZipFile(zip_path, "r") as archive:
  with archive.open("data/training_tags.txt") as file:
    for line in file:
      line_str = line.decode("utf-8").strip()
      if not line_str:
        continue

      parts = line_str.split()
      filename_tag = parts[0]  # e.g., "001_0_1_white.png"
      move_label = parts[1]  # e.g., "d4"

      # Remove extension and split into exact tokens
      base_name = filename_tag.replace(".png", "")
      tokens = base_name.split("_")

      if len(tokens) == 4:
        game_num, page_num, move_num, color = tokens
        parsed_tags.append({
            "game": game_num,
            "page": page_num,
            "move": move_num,
            "color": color,
            "label": move_label,
            "filename": f"data/{filename_tag}",
        })

print(f"Successfully parsed {len(parsed_tags)} tags.")
print("First 3 records:")
print(parsed_tags[:3])