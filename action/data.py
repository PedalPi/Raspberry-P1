class Data:

    def __init__(self, controller, token):
        self.token = token
        self.controller = controller

    @property
    def data(self):
        return self.controller[self.token]

    @data.setter
    def data(self, data):
        self.controller[self.token] = data

    def patch(self, patch):
        bank_data = self.bank(patch.bank)

        try:
            return bank_data[str(patch.index)]
        except KeyError:
            self.update_patch(patch, {})
            return {}

    def update_patch(self, patch, patch_data):
        bank = patch.bank

        bank_data = self.bank(bank)
        bank_data[str(patch.index)] = patch_data
        self.update_bank(bank, bank_data)

    def bank(self, bank):
        banks_data = self.banks

        try:
            return banks_data[str(bank.index)]
        except KeyError:
            self.update_bank(bank, {})
            return {}

    def update_bank(self, bank, bank_data):
        banks_data = self.banks
        banks_data[str(bank.index)] = bank_data

        data = self.data
        data['banks'] = banks_data

        self.data = data

    @property
    def banks(self):
        data = self.data
        try:
            return data['banks']
        except KeyError:
            data['banks'] = {}
            self.data = data
            return {}
