from PIL import Image
from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(default="slug",editable=False)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Category,self).save(*args,**kwargs)

    def post_count(self):
        return self.posts.all().count()

class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(editable=False)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Tag,self).save(*args,**kwargs)

    def post_count(self):
        return self.posts.all().count()

class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    publishing_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True,null=True,upload_to='uploads/',default='uploads/blog-3.jpg')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=1)
    slug = models.SlugField(default="slug",editable=False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1,related_name="posts")
    tag = models.ManyToManyField(Tag,related_name="posts",blank=True)
    slider_post = models.BooleanField(default=False)
    hit = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Post,self).save(*args,**kwargs)

        img = Image.open(self.image.path)
        if (img.height != 340 or img.width != 770) and (self.slider_post==False):
            img = img.resize((int(770), int(340)), Image.ANTIALIAS)
            img.save(self.image.path)

    def tags(self):
        return self.tag.all()

    def post_tag(self):
        return ','.join(str(tag) for tag in self.tag.all())

    def comment_count(self):
        return self.comments.all().count()



class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    content = models.TextField()
    publishing_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post.title








