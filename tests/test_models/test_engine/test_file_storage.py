#!/usr/bin/python3

import unittest
import os
from models.base_model import BaseModel
from file_storage import FileStorage

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        # Crear instancias para las pruebas
        self.obj1 = BaseModel()
        self.obj2 = BaseModel()
        self.obj3 = BaseModel()

        # Configurar el FileStorage para las pruebas
        self.storage = FileStorage()
        self.storage.new(self.obj1)
        self.storage.new(self.obj2)
        self.storage.new(self.obj3)

    def tearDown(self):
        # Limpiar archivos creados durante las pruebas
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        # Verificar que el método all devuelve un diccionario no vacío
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertNotEqual(len(all_objects), 0)

    def test_save_and_reload(self):
        # Verificar que los objetos se guardan correctamente y se pueden recargar
        self.storage.save()

        # Crear un nuevo almacenamiento para simular la recarga
        new_storage = FileStorage()
        new_storage.reload()

        # Verificar que los objetos recargados son instancias válidas de BaseModel
        for key, value in new_storage.all().items():
            obj = new_storage.all()[key]
            self.assertIsInstance(obj, BaseModel)

    def test_new(self):
        # Verificar que el método new agrega correctamente un objeto al diccionario
        obj4 = BaseModel()
        self.storage.new(obj4)
        all_objects = self.storage.all()
        key = f"{obj4.__class__.__name__}.{obj4.id}"
        self.assertIn(key, all_objects)
        self.assertEqual(all_objects[key], obj4)

if __name__ == '__main__':
    unittest.main()

