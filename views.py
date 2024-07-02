import os
from flask import render_template, redirect, url_for, flash, request, current_app
from . import db
from .models import Reel
from .forms import UploadForm
from werkzeug.utils import secure_filename

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

@current_app.route('/', methods=['GET', 'POST'])
def upload_reel():
    form = UploadForm()
    if form.validate_on_submit():
        if 'video' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['video']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            new_reel = Reel(title=form.title.data, filename=filename)
            db.session.add(new_reel)
            db.session.commit()
            flash('Video uploaded successfully')
            return redirect(url_for('view_reels'))
    return render_template('upload.html', form=form)

@current_app.route('/reels')
def view_reels():
    reels = Reel.query.all()
    return render_template('reels.html', reels=reels)
