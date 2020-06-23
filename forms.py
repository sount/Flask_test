from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField, IntegerField, DateField,FloatField
from wtforms.validators import DataRequired, Length, EqualTo
import email_validator


class FupForm(FlaskForm):
    #Ordering Party
    ibanorder = StringField("IBAN")
    bicorder = StringField("BIC", validators=[DataRequired(), Length(min=2, max=20)])
    banknameorder = StringField("Bank Name", validators=[DataRequired(), Length(min=2, max=20)])
    creditor =StringField(u"Ult. Creditor/Debitor")
    nameorder =StringField("Name")
    adress1order = StringField("Adress 1", validators=[DataRequired(), Length(min=2, max=20)])
    adress2order = StringField(u"Adress 2")
    countryorder = StringField("Country")

    #Ordering Party
    ibancount = StringField("IBAN")
    biccount = StringField("BIC", validators=[DataRequired(), Length(min=2, max=20)])
    namecount =StringField("Name")
    banknamecount= StringField("Bank Name", validators=[DataRequired(), Length(min=2, max=20)])
    adress1count = StringField("Adress 1", validators=[DataRequired(), Length(min=2, max=20)])
    adress2count = StringField(u"Adress 2")
    countrycount = StringField("Country")

    #Test Data Parameters
    inputchannel = SelectField(u'Input Channel', choices=["fup_australia", "I_CCI_HQ_EBA", "I_CCI_HQ_EBAREP", "I_EBI_HQ_PRIS_C", "I_EBI_HQ_PRIS_L", "I_EBI_HQ_PRIS_ZIP", "I_EBI_BE_PBC_ISABEL","I_EBI_BE_GTB_ISABEL"])
    messagetype = SelectField(u'Message Type', choices=["Pain_001_001_03_SCT","Pain_001_001_02","SCT"])
    transactiontype = SelectField(u'Transaction Type', choices=["SCT", "B2B","CORE"])
    numberoftransactions = IntegerField(u"Number of Transaction(s)",validators=[DataRequired()])

    #Dates
    settlementdate = DateField("Settelment Date", validators=[DataRequired()])

    #Details
    detailsofpayment = StringField(u"Details of Payment", validators=[DataRequired()])
    endtoendid = IntegerField(u"End to End ID", validators=[DataRequired()])
    localonly = BooleanField(u"Local Only")

    #amount
    settlementamount = FloatField(u"Settlement Amount")

    #submit
    submit = SubmitField("Submit")






