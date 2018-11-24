class Parameters:
    parameters = {}
    
    @staticmethod
    def set_parameters(new_parameters):
        Parameters.parameters.update(new_parameters)

    @staticmethod
    def get_parameters():
        return Parameters.parameters