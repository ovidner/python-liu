        if len(kwargs) != 1 or not any(i in self.accepted_params for i in kwargs.keys()):
            # Raises a TypeError if called with other than exactly 1 argument or with other parameter than the ones
            # accepted.
            raise TypeError('Called with invalid argument(s) or wrong number of arguments.')