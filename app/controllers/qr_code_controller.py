from flask import Blueprint, request, send_file, jsonify
from ..models.qr_code_model import *
import io

# Define the blueprint
qr_code_blueprint = Blueprint('qr_code', __name__)

@qr_code_blueprint.route('/generate_qr_with_logo', methods=['POST'])
def generate_qr_with_logo_endpoint():
    try:
        # Get the 'data' field from the form
        data = request.form.get('data')
        if not data:
            return jsonify({"error": "Missing 'data' in form data"}), 400

        # Get the uploaded 'logo' file from the form
        logo_file = request.files.get('logo')
        if not logo_file:
            return jsonify({"error": "Missing 'logo' file in form data"}), 400

        # Generate the QR code with the logo
        qr_image = generate_qr_with_logo(data, logo_file)

        # Save the QR code to a bytes buffer
        buffer = io.BytesIO()
        qr_image.save(buffer, format="PNG")
        buffer.seek(0)

        # Return the QR code image as a response
        return send_file(buffer, mimetype='image/png')

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@qr_code_blueprint.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the QR Code Generator API with Logo Upload!"})


@qr_code_blueprint.route('/generate_qr', methods=['POST'])
def generate_qr_endpoint():
    try:
        data = request.form.get('data')
        if not data:
            return jsonify({"error": "Missing 'data' in form data"}), 400

        qr_image = generate_qr_with_no_logo(data)
        # Save the QR code to a bytes buffer
        buffer = io.BytesIO()
        qr_image.save(buffer, format="PNG")
        buffer.seek(0)

        # Return the QR code image as a response
        return send_file(buffer, mimetype='image/png')

    except Exception as e:
        return jsonify({"error": str(e)}), 500