# Thanks to Twitter Python SDK
# https://github.com/bear/python-twitter/blob/master/twitter/models.py

import json


class HyperwalletModel(object):
    '''
    The base Hyperwallet Model from which all other models will inherit.

    :param data:
        A dictionary containing the attributes for the Model.
    '''

    def __init__(self, data):
        '''
        Create an instance of the base HyperwalletModel.
        '''

        self.defaults = {}

    def __str__(self):
        '''
        Return a string representation of the HyperwalletModel. By default this
        is the same as asJsonString().
        '''

        return self.asJsonString()

    def asJsonString(self):
        '''
        Return a JSON string of the HyperwalletModel based on key/value pairs
        returned from the asDict() function.
        '''

        return json.dumps(self.asDict(), sort_keys=True)

    def asDict(self):
        '''
        Return a dictionary representation of the Model.
        '''

        data = {}

        for (key, value) in self.defaults.items():
            if isinstance(getattr(self, key, None), (list, tuple, set)):
                data[key] = list()
                for subobj in getattr(self, key, None):
                    if getattr(subobj, '_to_dict', None):
                        data[key].append(subobj._to_dict())
                    else:
                        data[key].append(subobj)

            elif getattr(getattr(self, key, None), '_to_dict', None):
                data[key] = getattr(self, key)._to_dict()

            elif getattr(self, key, None):
                data[key] = getattr(self, key, None)

        return data


class User(HyperwalletModel):
    '''
    The User Model.

    :param data:
        A dictionary containing the attributes for the User.
    '''

    def __init__(self, data):
        '''
        Create a new User with the provided attributes.
        '''

        self.defaults = {
            'token': None,
            'createdOn': None,
            'status': None,
            'verificationStatus': None,
            'email': None,
            'profileType': None,
            'firstName': None,
            'middleName': None,
            'lastName': None,
            'dateOfBirth': None,
            'countryOfBirth': None,
            'countryOfNationality': None,
            'gender': None,
            'phoneNumber': None,
            'mobileNumber': None,
            'governmentId': None,
            'passportId': None,
            'driversLicenseId': None,
            'employerId': None,
            'businessType': None,
            'businessName': None,
            'businessRegistrationId': None,
            'businessRegistrationStateProvince': None,
            'businessRegistrationCountry': None,
            'businessContactRole': None,
            'addressLine1': None,
            'addressLine2': None,
            'city': None,
            'stateProvince': None,
            'country': None,
            'postalCode': None,
            'language': None,
            'programToken': None,
            'clientUserId': None
        }

        for (param, default) in self.defaults.items():
            setattr(self, param, data.get(param, default))

    def __repr__(self):
        return "User({date}, {token})".format(
            date=self.createdOn,
            token=self.token
        )


class TransferMethod(HyperwalletModel):
    '''
    The TransferMethod Model.

    :param data:
        A dictionary containing the attributes for the Transfer Method.
    '''

    def __init__(self, data):
        '''
        Create a new Transfer Method with the provided attributes.
        '''

        self.defaults = {
            'token': None,
            'createdOn': None,
            'status': None,
            'type': None,
            'transferMethodCountry': None,
            'transferMethodCurrency': None
        }

        for (param, default) in self.defaults.items():
            setattr(self, param, data.get(param, default))

    def __repr__(self):
        return "TransferMethod({date}, {token})".format(
            date=self.createdOn,
            token=self.token
        )


class BankAccount(TransferMethod):
    '''
    The BankAccount Model.

    :param data:
        A dictionary containing the attributes for the Bank Account.
    '''

    def __init__(self, data):
        '''
        Create a new Bank Account with the provided attributes.
        '''

        TransferMethod.__init__(self, data)

        self.defaults = {
            'email': None,
            'profileType': None,
            'firstName': None,
            'middleName': None,
            'lastName': None,
            'dateOfBirth': None,
            'countryOfBirth': None,
            'countryOfNationality': None,
            'gender': None,
            'phoneNumber': None,
            'mobileNumber': None,
            'governmentId': None,
            'passportId': None,
            'driverLicenseId': None,
            'businessType': None,
            'businessName': None,
            'businessRegistrationId': None,
            'businessRegistrationStateProvince': None,
            'businessRegistrationCountry': None,
            'businessContactRole': None,
            'addressLine1': None,
            'addressLine2': None,
            'city': None,
            'stateProvince': None,
            'country': None,
            'postalCode': None,
            'bankName': None,
            'bankId': None,
            'bankAccountRelationship': None,
            'branchName': None,
            'branchId': None,
            'bankAccountId': None,
            'bankAccountPurpose': None,
            'branchAddressLine1': None,
            'branchAddressLine2': None,
            'branchCity': None,
            'branchStateProvince': None,
            'branchCountry': None,
            'branchPostalCode': None,
            'wireInstructions': None,
            'intermediaryBankId': None,
            'intermediaryBankName': None,
            'intermediaryBankAccountId': None,
            'intermediaryBankAddressLine1': None,
            'intermediaryBankAddressLine2': None,
            'intermediaryBankCity': None,
            'intermediaryBankStateProvince': None,
            'intermediaryBankCountry': None,
            'intermediaryBankPostalCode': None
        }

        for (param, default) in self.defaults.items():
            setattr(self, param, data.get(param, default))

    def __repr__(self):
        return "BankAccount({date}, {token})".format(
            date=self.createdOn,
            token=self.token
        )


class BankCard(TransferMethod):
    '''
    The BankCard Model.

    :param data:
        A dictionary containing the attributes for the Bank Card.
    '''

    def __init__(self, data):
        '''
        Create a new Bank Card with the provided attributes.
        '''

        TransferMethod.__init__(self, data)

        self.defaults = {
            'profileType': None,
            'businessName': None,
            'addressLine1': None,
            'city': None,
            'stateProvince': None,
            'country': None,
            'postalCode': None,
            'cardNumber': None,
            'cardType': None,
            'cardBrand': None,
            'dateOfExpiry': None,
            'isDefaultTransferMethod': None
        }

        for (param, default) in self.defaults.items():
            setattr(self, param, data.get(param, default))

    def __repr__(self):
        return "BankCard({date}, {token})".format(
            date=self.createdOn,
            token=self.token
        )


class PrepaidCard(TransferMethod):
    '''
    The PrepaidCard Model.

    :param data:
        A dictionary containing the attributes for the Prepaid Card.
    '''

    def __init__(self, data):
        '''
        Create a new Prepaid Card with the provided attributes.
        '''

        TransferMethod.__init__(self, data)

        self.defaults = {
            'cardType': None,
            'cardPackage': None,
            'cardNumber': None,
            'cardBrand': None,
            'dateOfExpiry': None
        }

        for (param, default) in self.defaults.items():
            setattr(self, param, data.get(param, default))

    def __repr__(self):
        return "PrepaidCard({date}, {token})".format(
            date=self.createdOn,
            token=self.token
        )


class PaperCheck(TransferMethod):
    '''
    The PaperCheck Model.

    :param data:
        A dictionary containing the attributes for the Paper Check.
    '''

    def __init__(self, data):
        '''
        Create a new Paper Check with the provided attributes.
        '''

        TransferMethod.__init__(self, data)

        self.defaults = {
            'profileType': None,
            'firstName': None,
            'middleName': None,
            'lastName': None,
            'dateOfBirth': None,
            'countryOfBirth': None,
            'countryOfNationality': None,
            'phoneNumber': None,
            'mobileNumber': None,
            'governmentId': None,
            'businessName': None,
            'businessRegistrationId': None,
            'businessRegistrationCountry': None,
            'addressLine1': None,
            'city': None,
            'stateProvince': None,
            'country': None,
            'postalCode': None,
            'bankName': None,
            'bankId': None,
            'bankAccountRelationship': None,
            'branchName': None,
            'branchId': None,
            'bankAccountId': None,
            'bankAccountPurpose': None,
            'branchAddressLine1': None,
            'branchAddressLine2': None,
            'branchCity': None,
            'branchStateProvince': None,
            'branchCountry': None,
            'branchPostalCode': None,
            'wireInstructions': None,
            'intermediaryBankId': None,
            'intermediaryBankName': None,
            'intermediaryBankAccountId': None,
            'intermediaryBankAddressLine1': None,
            'intermediaryBankAddressLine2': None,
            'intermediaryBankCity': None,
            'intermediaryBankStateProvince': None,
            'intermediaryBankCountry': None,
            'intermediaryBankPostalCode': None,
            'shippingMethod': None,
            'isDefaultTransferMethod': None
        }

        for (param, default) in self.defaults.items():
            setattr(self, param, data.get(param, default))

    def __repr__(self):
        return "PaperCheck({date}, {token})".format(
            date=self.createdOn,
            token=self.token
        )


class Payment(HyperwalletModel):
    '''
    The Payment Model.

    :param data:
        A dictionary containing the attributes for the Payment.
    '''

    def __init__(self, data):
        '''
        Create a new Payment with the provided attributes.
        '''

        self.defaults = {
            'token': None,
            'status': None,
            'createdOn': None,
            'programToken': None,
            'clientPaymentId': None,
            'amount': None,
            'currency': None,
            'notes': None,
            'memo': None,
            'purpose': None,
            'releaseOn': None,
            'expiresOn': None,
            'destinationToken': None
        }

        for (param, default) in self.defaults.items():
            setattr(self, param, data.get(param, default))

    def __repr__(self):
        return "Payment({date}, {token})".format(
            date=self.createdOn,
            token=self.token
        )


class Balance(HyperwalletModel):
    '''
    The Balance Model.

    :param data:
        A dictionary containing the attributes for the Balance.
    '''

    def __init__(self, data):
        '''
        Create a new Balance with the provided attributes.
        '''

        self.defaults = {
            'currency': None,
            'amount': None
        }

        for (param, default) in self.defaults.items():
            setattr(self, param, data.get(param, default))

    def __repr__(self):
        return "Balance({currency}, {amount})".format(
            currency=self.currency,
            amount=self.amount
        )


class ReceiptDetail(HyperwalletModel):
    '''
    The Receipt Detail Model.

    :param data:
        A dictionary containing the attributes for the Receipt Detail.
    '''

    def __init__(self, data):
        '''
        Create a new Receipt Detail with the provided attributes.
        '''

        self.defaults = {
            'clientPaymentId': None,
            'notes': None,
            'memo': None,
            'returnOrRecallReason': None,
            'website': None,
            'payerName': None,
            'payeeName': None,
            'charityName': None,
            'cardHolderName': None,
            'bankName': None,
            'bankId': None,
            'branchName': None,
            'branchId': None,
            'bankAccountId': None,
            'bankAccountPurpose': None,
            'branchAddressLine1': None,
            'branchAddressLine2': None,
            'branchCity': None,
            'branchStateProvince': None,
            'branchCountry': None,
            'branchPostalCode': None,
            'checkNumber': None,
            'cardNumber': None,
            'cardExpiryDate': None,
            'payeeEmail': None,
            'payeeAddressLine1': None,
            'payeeAddressLine2': None,
            'payeeCity': None,
            'payeeStateProvince': None,
            'payeeCountry': None,
            'payeePostalCode': None,
            'paymentExpiryDate': None,
            'securityQuestion': None,
            'securityAnswer': None
        }

        for (param, default) in self.defaults.items():
            setattr(self, param, data.get(param, default))

    def __repr__(self):
        return "ReceiptDetail({identifier})".format(
            identifier=self.clientPaymentId or self.cardNumber or 'Unknown'
        )


class Receipt(HyperwalletModel):
    '''
    The Receipt Model.

    :param data:
        A dictionary containing the attributes for the Receipt.
    '''

    def __init__(self, data):
        '''
        Create a new Receipt with the provided attributes.
        '''

        self.defaults = {
            'journalId': None,
            'type': None,
            'createdOn': None,
            'entry': None,
            'sourceToken': None,
            'destinationToken': None,
            'amount': None,
            'fee': None,
            'currency': None,
            'foreignExchangeRate': None,
            'foreignExchangeCurrency': None,
            'details': None,
        }

        for (param, default) in self.defaults.items():
            setattr(self, param, data.get(param, default))

        if type(self.details) is dict:
            self.details = ReceiptDetail(self.details)

    def __repr__(self):
        return "Receipt({entry}, {amount})".format(
            entry=self.entry,
            amount=self.amount
        )


class Program(HyperwalletModel):
    '''
    The Program Model.

    :param data:
        A dictionary containing the attributes for the Program.
    '''

    def __init__(self, data):
        '''
        Create a new Program with the provided attributes.
        '''

        self.defaults = {
            'token': None,
            'createdOn': None,
            'name': None,
            'parentToken': None
        }

        for (param, default) in self.defaults.items():
            setattr(self, param, data.get(param, default))

    def __repr__(self):
        return "Program({date}, {token})".format(
            date=self.createdOn,
            token=self.token
        )


class Account(HyperwalletModel):
    '''
    The Account Model.

    :param data:
        A dictionary containing the attributes for the Account.
    '''

    def __init__(self, data):
        '''
        Create a new Account with the provided attributes.
        '''

        self.defaults = {
            'token': None,
            'createdOn': None,
            'type': None,
            'email': None
        }

        for (param, default) in self.defaults.items():
            setattr(self, param, data.get(param, default))

    def __repr__(self):
        return "Account({date}, {token})".format(
            date=self.createdOn,
            token=self.token
        )


class StatusTransition(HyperwalletModel):
    '''
    The StatusTransition Model.

    :param data:
        A dictionary containing the attributes for the Status Transition.
    '''

    def __init__(self, data):
        '''
        Create a new Status Transition with the provided attributes.
        '''

        self.defaults = {
            'token': None,
            'createdOn': None,
            'transition': None,
            'fromStatus': None,
            'toStatus': None,
            'notes': None,
            'statusCode': None
        }

        for (param, default) in self.defaults.items():
            setattr(self, param, data.get(param, default))

    def __repr__(self):
        return "StatusTransition({date}, {token})".format(
            date=self.createdOn,
            token=self.token
        )


class Webhook(HyperwalletModel):
    '''
    The Webhook Model.

    :param data: A dictionary containing the attributes for the Webhook.
    '''

    def __init__(self, data):
        '''
        Create a new Webhook with the provided attributes.
        '''

        self.defaults = {
            'token': None,
            'type': None,
            'createdOn': None,
            'object': None
        }

        for (param, default) in self.defaults.items():
            setattr(self, param, data.get(param, default))

        wh_object = Webhook.make_object(self.type, self.object)

        if wh_object is not None:
            self.object = wh_object

    def __repr__(self):
        return "Webhook({date}, {token})".format(
            date=self.createdOn,
            token=self.token
        )

    @staticmethod
    def make_object(wh_type, wh_object):

        if wh_type is None:
            return None

        if type(wh_object) is not dict:
            return None

        types = {
            'PAYMENTS': Payment,
            'BANK_ACCOUNTS': BankAccount,
            'PREPAID_CARDS': PrepaidCard,
            'USERS': User
        }

        base, sub = wh_type.split('.')[:2]

        if sub in types:
            return types[sub](wh_object)
        elif base in types:
            return types[base](wh_object)

        return None
