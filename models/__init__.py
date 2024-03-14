from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
classes = ["BaseModel", "FileStorage", "User", "State",
           "City", "Amenity", "Place", "Review"]
