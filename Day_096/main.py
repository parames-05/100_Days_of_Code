import os
import base64
import numpy as np
from io import BytesIO
from PIL import Image
from flask import Flask, render_template, request, url_for
from sklearn.cluster import KMeans

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB limit
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


def extract_palette(image_stream, num_colors=6):
    img = Image.open(image_stream).convert('RGB')
    img.thumbnail((200, 200))  # Smaller image = faster K-Means

    # Convert image data to a list of pixels
    img_data = np.array(img)
    pixels = img_data.reshape(-1, 3)

    # Run K-Means to find dominant color clusters
    kmeans = KMeans(n_clusters=num_colors, n_init=10)
    kmeans.fit(pixels)

    # Get the central colors of the clusters
    colors = kmeans.cluster_centers_.astype(int)

    # Convert RGB to Hex strings
    palette = []
    for color in colors:
        hex_code = '#{:02x}{:02x}{:02x}'.format(color[0], color[1], color[2])
        palette.append({'hex': hex_code})

    return palette


@app.route('/')
def index():
    return render_template('base.html', image_uploaded=False)


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return "No file part", 400

    file = request.files['image']
    if file.filename == '':
        return "No selected file", 400

    if file:
        image_bytes = file.read()
        palette_data = extract_palette(BytesIO(image_bytes))
        encoded_image = base64.b64encode(image_bytes).decode('utf-8')
        image_url = f"data:{file.content_type};base64,{encoded_image}"

        return render_template(
            'base.html',
            image_uploaded=True,
            image_url=image_url,
            filename=file.filename,
            palette=palette_data
        )


if __name__ == '__main__':
    app.run(debug=True, port=3000)