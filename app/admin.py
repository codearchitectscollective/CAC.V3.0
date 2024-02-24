from django.contrib import admin
from .models import Post
from .models import News
from .models import Featured
from .models import Trending
from .models import Profile

admin.site.register(Post)
admin.site.register(News)
admin.site.register(Featured)
admin.site.register(Trending)
admin.site.register(Profile)

