from blog.model import Post
from flask import render_template, request , Blueprint
main = Blueprint('main',__name__)

@main.route("/")
@main.route("/home")
def index():
    page= request.args.get('page',1, type=int )
    post= Post.query.order_by(Post.date_posted.desc()).paginate(page=page,per_page=5)
    return render_template("home.html", post=post)

@main.route("/about")
def about():
    return render_template("about.html", title='About')

