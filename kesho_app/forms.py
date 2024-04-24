# create interfaces that represent our models
#the form file connects to the particular model to html
from django.forms import ModelForm
from.models import *
 #create forms related to models
class Addbabe(ModelForm):
    class Meta:
         model = Baby
         fields = "__all__"

class AddpaymentForm(ModelForm):
    class Meta:
         model = Payment
         fields = "__all__"
