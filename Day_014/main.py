import os
from PIL import Image, ImageDraw, ImageFont

template_path = "cert.png"
output_folder = "certificate"

name_font_path = "ToThePointRegular-n9y4.ttf"
dept_font_path = "ToThePointRegular-n9y4.ttf"

names = [
    "Parameswaran M V",
    "Velavan R",
    "Ganeshan G",
    "Prabhakaran"
]

department = "III EEE"

name_font_size = 50
dept_font_size = 50
name_center_x = 374
dept_center_x = 799
text_center_y = 439
LEFT_BUFFER = 35

def generate_certificates(names, department):
    os.makedirs(output_folder, exist_ok=True)
    # Loading fonts
    name_font = ImageFont.truetype(name_font_path, name_font_size)
    dept_font = ImageFont.truetype(dept_font_path, dept_font_size)
    for name in names:
        img = Image.open(template_path).convert("RGB")
        draw = ImageDraw.Draw(img)
        name_bbox = draw.textbbox((0, 0), name, font=name_font)
        name_w = name_bbox[2] - name_bbox[0]
        name_h = name_bbox[3] - name_bbox[1]

        name_x = name_center_x - name_w // 2
        name_x = max(name_x, LEFT_BUFFER)  # ensures it never goes too far left

        name_y = text_center_y - name_h // 2

        draw.text((name_x, name_y), name, font=name_font, fill="#004aad")
        dept_bbox = draw.textbbox((0, 0), department, font=dept_font)
        dept_w = dept_bbox[2] - dept_bbox[0]
        dept_h = dept_bbox[3] - dept_bbox[1]

        dept_x = dept_center_x - dept_w // 2
        dept_x = max(dept_x, LEFT_BUFFER)

        dept_y = text_center_y - dept_h // 2

        draw.text((dept_x, dept_y), department, font=dept_font, fill="#004aad")
        safe_name = name.replace(" ", "_")
        output_path = os.path.join(output_folder, f"{safe_name}_certificate.jpg")
        img.save(output_path)
        print(f"Saved: {output_path}")

generate_certificates(names, department)
