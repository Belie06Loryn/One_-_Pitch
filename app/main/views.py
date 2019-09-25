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

@main.route('/add/ibyiciro', methods=['GET','POST'])
@login_required
def ibyiciro_bishya():
    
    form = CategoryForm()

    if form.validate_on_submit():
        type_cate = form.type_cate.data
        ibyiciro_bishya = Category(type_cate=type_cate)
        ibyiciro_bishya.ububiko()

        return redirect(url_for('.index'))

    title = 'Category'
    return render_template('ibyiciro_bishya.html', category_form = form,title=title)

@main.route('/ibyiciro/<int:id>')
def category(id):
    ibyiciros = Category.query.get(id)
    pit = Pitch.query.filter_by(ibyiciro=ibyiciros.id).all()

    return render_template('ibyiciro.html', pit=pit, category=ibyiciros)

@main.route('/ibyiciro/nouveau_pitch/<int:id>', methods=['GET', 'POST'])
@login_required
def nouveau_pitch(id):
                                           
    form = PitchForm()
    ibyiciro = Category.query.filter_by(id=id).first()

    if ibyiciro is None:
        abort(404)

    if form.validate_on_submit():
        text = form.text.data
        nouveau_pitch= Pitch(text=text,ibyiciro= ibyiciro.id)
        nouveau_pitch.ububiko_pitch()
        return redirect(url_for('.view_pitch', id=ibyiciro.id))


    title = 'Pitch'
    return render_template('nouveau_pitch.html', title = title, pitch_form = form,ibyiciro = ibyiciro)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)
    
@main.route('/ibyiciro/view_pitch/<int:id>', methods=['GET', 'POST'])
@login_required
def view_pitch(id):

    
    pitches = Pitch.query.get(id)
    print(pitches.text)
    if pitches is None:
        abort(404)

    comment = Words.get_words(id)
    return render_template('pitch.html', pitches=pitches, comment=comment, ibyiciro=id)


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

    