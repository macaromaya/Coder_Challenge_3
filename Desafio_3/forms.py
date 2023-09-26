from django import forms 


class LeadForm (forms.Form):
    
    lead_group= forms.Charfield()
    group_id= forms.IntegerField()
