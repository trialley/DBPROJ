from django.contrib import admin

from .models import House
from .models import Village
from .models import Trader
from .models import User
from .models import Deal
from .models import Collection
from .models import Browse

admin.site.register(House)
admin.site.register(Village)
admin.site.register(Trader)
admin.site.register(User)
admin.site.register(Deal)
admin.site.register(Collection)
admin.site.register(Browse)
