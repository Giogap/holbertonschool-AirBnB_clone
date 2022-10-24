#!/usr/bin/python3
""""""

import uuid
import datetime

class BaseModel:

    def __init__(self, id, create_at, update_at):
        self.id = str(uuid.uuid4())
        self.create_at = datetime.now()
        self.update_at = datetime.now()


    def __str__(self):
        return "[BaseModel] {} {}".format(self.id, self.__dict__)

    
    def save(self):
        pass


