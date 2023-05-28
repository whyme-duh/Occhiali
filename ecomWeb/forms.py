from django import forms

class BillingAddressForm(forms.Form):
    first_name = forms.CharField(label = "Your first name ", max_length=80)
    last_name = forms.CharField(label = "Your last name ", max_length=80)
    address = forms.CharField(label ='Your address 1', max_length=100)
    address2 = forms.CharField(label ='Your address 2', max_length=100, required=False)
  

class CardForm(forms.Form):
    name_on_card = forms.CharField(label = 'Your card name', max_length=100)
    credit_card_number = forms.CharField(label = 'Your credit card number', max_length=100)
    expiration = forms.DateTimeField(label = 'Your expiration date')
    cvv = forms.CharField(label = 'Your cvv', max_length=100)



class CouponForm(forms.Form):
    code = forms.CharField(max_length=5)

  
