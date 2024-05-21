from django.contrib import admin
from xmainsite.models import PcBase, PcType
import inspect
import xmainsite.models
from django.utils.safestring import mark_safe

admin.site.register(PcBase)
admin.site.register(PcType)



# ms = inspect.getmembers(xmainsite.models, inspect.isclass)
# for model in ms:
#     print(model[0])
#     admin.site.register(model[1])
