#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        # Initialize instance attributes
        self.id = str(uuid.uuid4())  # Generate a unique identifier
        self.created_at = datetime.now()  # Set the creation time
        self.updated_at = datetime.now()  # Set the update time

    def __str__(self):
        # Return a string representation of the object
        class_name = self.__class__.__name__()  # Corrected to add parentheses
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        # Update the 'updated_at' attribute with the current datetime
        self.updated_at = datetime.now()

    def to_dict(self):
        # Return a dictionary containing all keys/values of __dict__ of the instance
        instance_dict = self.__dict__.copy()

        # Convert 'created_at' and 'updated_at' to string objects in ISO format
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()

        # Add a key '__class__' to the dictionary with the class name of the object
        instance_dict['__class__'] = self.__class__.__name__

        return instance_dict
