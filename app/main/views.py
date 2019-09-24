from flask import render_template,request,redirect,url_for, abort
from . import main
from ..models import User, Pitch, Category, Words, Tora
from flask_login import login_required, current_user
from .forms import UpdateProfile, PitchForm, CommentForm, CategoryForm
from .. import db, photos

@main.route('/')
def index():
    ibyiciro = Category.get_ibyiciro()


    return render_template('index.html',  ibyiciro = ibyiciro)

@main.route('/ibyiciro', methods=['GET','POST'])
@login_required
def ibyiciro_bishya():
    
    form = CategoryForm()

    if form.validate_on_submit():
        name = form.name.data
        ibyiciro_bishya = Category(name=name)
        ibyiciro_bishya.save_ikiciro()

        return redirect(url_for('.index'))

    title = 'Category'
    return render_template('ibyiciro_bishya.html', category_form = form,title=title)

@main.route('/ibyiciro/<int:id>')
def category(id):
    ibyiciro = Category.query.get(id)
    pit = Pitch.query.filter_by(ibyiciro=ibyiciro_.id).all()

    return render_template('ibyiciro.html', pit=pit, ibyiciro=ibyiciro)

@main.route('/ibyiciro/pitch/plus/<int:id>', methods=['GET', 'POST'])
@login_required
def new_pitch(id):
                                           
    form = PitchForm()
    ibyiciro = Category.query.filter_by(id=id).first()

    if ibyiciro is None:
        abort(404)

    if form.validate_on_submit():
        content = form.content.data
        plus_pitch= Pitch(content=content,ibyiciro= ibyiciro.id,user_id=current_user.id)
        plus_pitch.save_pitch()
        return redirect(url_for('.ibyiciro', id=ibyiciro.id))


    title = 'Pitch'
    return render_template('nouveau_pitch.html', title = title, pitch_form = form,ibyiciro = ibyiciro)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)
    
@main.route('/ibyiciro/pitch/<int:id>', methods=['GET', 'POST'])
@login_required
def view_pitch(id):

    print(id)
    pitches = Pitch.query.get(id)

    if pitches is None:
        abort(404)

    comment = Words.get_comments(id)
    return render_template('pitch.html', pitches=pitches, comment=comment, ibyiciro_id=id)


@main.route('/user/<uname>/update/pic', methods = ['POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)
    
    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname = user.username))
    
    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

    