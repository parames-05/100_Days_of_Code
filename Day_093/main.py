from PIL import Image

def add_watermark(base_image_path, watermark_path, output_path,
                  position="bottom_right", opacity=128, scale=0.25):

    base = Image.open(base_image_path).convert("RGBA")
    watermark = Image.open(watermark_path).convert("RGBA")

    base_width, base_height = base.size
    watermark_width = int(base_width * scale)
    watermark_ratio = watermark_width / watermark.width
    watermark_height = int(watermark.height * watermark_ratio)

    watermark = watermark.resize((watermark_width, watermark_height), Image.LANCZOS)

    watermark_layer = Image.new("RGBA", watermark.size)
    watermark_mask = watermark.split()[3].point(lambda i: opacity)
    watermark_layer.paste(watermark, (0, 0), watermark_mask)

    if position == "bottom_right":
        x = base_width - watermark_width - 10
        y = base_height - watermark_height - 10
    elif position == "bottom_left":
        x = 10
        y = base_height - watermark_height - 10
    elif position == "top_right":
        x = base_width - watermark_width - 10
        y = 10
    elif position == "top_left":
        x = 10
        y = 10
    else:  #centre
        x = (base_width - watermark_width) // 2
        y = (base_height - watermark_height) // 2

    # Paste watermark onto base image
    base.paste(watermark_layer, (x, y), watermark_layer)

    # Save final image
    base.convert("RGB").save(output_path)

# Example usage
add_watermark(
    base_image_path="exampaper.jpg",
    watermark_path="logo1.png",
    output_path="watermarked_top_right.jpg",
    position="top_right",
    opacity=120,
    scale=0.2
)