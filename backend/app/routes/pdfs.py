from flask import Blueprint, request, jsonify, send_file
from werkzeug.utils import secure_filename
from app.models.pdf import PDF
from app.models.project import Project
from app import db
from app.utils.auth import login_required, current_user
import os

bp = Blueprint('pdfs', __name__, url_prefix='/pdfs')

UPLOAD_FOLDER = 'app/uploads/pdfs'
ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@bp.route('/upload', methods=['POST'])
@login_required
def upload_pdf():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if not allowed_file(file.filename):
        return jsonify({'error': 'File type not allowed'}), 400
    
    project_id = request.form.get('project_id')
    if not project_id:
        return jsonify({'error': 'Project ID is required'}), 400
    
    project = Project.query.get_or_404(project_id)
    if project.user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403
    
    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)
    
    new_pdf = PDF(filename=filename, filepath=filepath, project_id=project_id)
    db.session.add(new_pdf)
    db.session.commit()
    
    return jsonify({'message': 'PDF uploaded successfully', 'pdf': new_pdf.to_dict()}), 201

@bp.route('/<int:pdf_id>', methods=['GET'])
@login_required
def get_pdf(pdf_id):
    pdf = PDF.query.get_or_404(pdf_id)
    if pdf.project.user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403
    return send_file(pdf.filepath, as_attachment=True)

@bp.route('/<int:pdf_id>', methods=['DELETE'])
@login_required
def delete_pdf(pdf_id):
    pdf = PDF.query.get_or_404(pdf_id)
    if pdf.project.user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403
    
    # Remove the file from the filesystem
    os.remove(pdf.filepath)
    
    db.session.delete(pdf)
    db.session.commit()
    
    return jsonify({'message': 'PDF deleted successfully'}), 200