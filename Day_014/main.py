import os
from PIL import Image, ImageDraw, ImageFont

# ==== USER INPUT ====
template_path = "cert.png"   # certificate background
output_folder = "certiii"    # folder where certificates will be saved

# Fonts
name_font_path = "Agrandir Narrow Bold.ttf"   # font for names
dept_font_path = "Agrandir Narrow Bold.ttf"       # font for department (change to your dept font)

names = [
    "Guru R",
    "Devendran J P",
    "Jerone Blesswin J",
    "Jagathratchagan A",
    "Malavaraj P",
    "Semesh S",
    "Bineesh B U",
    "Nilavarasu C",
    "Joel Jackson A",
    "Praneeth S",
    "Dhananjayan R",
    "Asvaddhaman V",
    "Arjith S K",
    "BharathShakthivasan A N",
    "Arun Prasath M G",
    "Sarvesh K",
    "Shanthan A",
    "Saurav Krishna S",
    "Suryaprakash A",
    "Surendran M",
    "Mithra A R",
    "Varsha A",
    "Santhiya R",
    "Sathish Ganapathi G",
    "Harshitha V",
    "Ashruthi N",
    "Benitaa Paulin E A",
    "Fana P Felix",
    "Akshita Sri V G",
    "Shri Ram Vijay M",
    "Saran A",
    "Saravanavel M",
    "Sriman Varun S",
    "Ajay Y"
]


department = "II RA"

# Font sizes
name_font_size = 50
dept_font_size = 50

# Center positions (x, y) on the certificate
name_center = (750, 740)
dept_center = (1453, 740)

# ==== SCRIPT ====
def generate_certificates(names, department):
    # Make sure output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Load fonts
    name_font = ImageFont.truetype(name_font_path, name_font_size)
    dept_font = ImageFont.truetype(dept_font_path, dept_font_size)

    for name in names:
        # Open template
        img = Image.open(template_path).convert("RGB")
        draw = ImageDraw.Draw(img)

        # ====== NAME (auto-centered) ======
        name_bbox = draw.textbbox((0, 0), name, font=name_font)
        name_width = name_bbox[2] - name_bbox[0]
        name_height = name_bbox[3] - name_bbox[1]
        name_x = name_center[0] - name_width // 2
        name_y = name_center[1] - name_height // 2
        draw.text((name_x, name_y), name, font=name_font, fill="#004aad")

        # ====== DEPARTMENT (auto-centered) ======
        dept_bbox = draw.textbbox((0, 0), department, font=dept_font)
        dept_width = dept_bbox[2] - dept_bbox[0]
        dept_height = dept_bbox[3] - dept_bbox[1]
        dept_x = dept_center[0] - dept_width // 2
        dept_y = dept_center[1] - dept_height // 2
        draw.text((dept_x, dept_y), department, font=dept_font, fill="#004aad")

        # Save certificate
        safe_name = name.replace(" ", "_")
        output_path = os.path.join(output_folder, f"{safe_name}_certificate.jpg")
        img.save(output_path)
        print(f"Saved: {output_path}")

# Run
generate_certificates(names, department)
