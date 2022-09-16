from datetime import datetime

class LoggingConsole:
    """ 
    Class responsible to create a logging pattern for jobs execution.
    
    Attributes
    ----------
    component : str
        The name of the component that will use the logs.
    additional_infos : dict
        Additional informations to compose the log message,
        only the values in the dict will be used in the log.
        For example {'country': 'country'}
    """

    def __init__(self, component: str, additional_infos: dict = None):
        self.component = component
        self.additional_infos = additional_infos
        self.start_execution_time = datetime.utcnow()

    def prepare_additional_info_string(self):
        if self.additional_infos is None:
            return ''
        keys_values = self.additional_infos.items()
        additional_infos_list = [f'{str(value)}' for key, value in keys_values]
        additional_infos_str = ' '.join(additional_infos_list)
        return additional_infos_str

    def log_info(self, message):
        """
        Prints a log information message with the following structure:
        <yyyy-mm-dd> - <h.mm.ss>.<ms> - <component name> <additional_infos_str> - <message>
        """
        additional_infos_str = self.prepare_additional_info_string()
        print(
            f''' {datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]} - {self.component} {additional_infos_str} - {message}''')

    def log_error(self, message):
        """
        Prints an error information message with the following structure:
        <yyyy-mm-dd> - <h.mm.ss>.<ms> [ERROR] - <component name> <additional_infos_str> - Error: <message>
        """
        additional_infos_str = self.prepare_additional_info_string()
        print(
            f''' {datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]} [ERROR] - {self.component} {additional_infos_str} - Error: {message} ''')

    def log_exception(self, message):
        """
        Prints an exception information message with the following structure:
        <yyyy-mm-dd> - <h.mm.ss>.<ms>  [EXCEPTION] - <component name> <additional_infos_str> - An Exception Occurred: <message>
        """
        additional_infos_str = self.prepare_additional_info_string()
        print(
            f''' {datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]} [EXCEPTION] - {self.component} {additional_infos_str} - An Exception Occurred: {message} ''')
