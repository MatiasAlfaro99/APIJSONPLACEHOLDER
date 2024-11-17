import requests

class CRUDAPI:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    @staticmethod
    def get_data(endpoint, sort_key=None):
        """Obtener y ordenar datos de un endpoint específico."""
        response = requests.get(f"{CRUDAPI.BASE_URL}/{endpoint}")
        if response.status_code == 200:
            data = response.json()
            if sort_key:  # Ordenar datos si se especifica una clave
                data = sorted(data, key=lambda x: x.get(sort_key))
            return data
        else:
            print(f"Error al obtener datos de {endpoint}: {response.status_code}")
            return []

    @staticmethod
    def create_data(endpoint, data):
        """Crear un nuevo registro en un endpoint específico."""
        response = requests.post(f"{CRUDAPI.BASE_URL}/{endpoint}", json=data)
        if response.status_code == 201:
            print(f"Registro creado exitosamente en {endpoint}.")
            return response.json()
        else:
            print(f"Error al crear registro en {endpoint}: {response.status_code}")
            return None

    @staticmethod
    def update_data(endpoint, record_id, data):
        """Actualizar un registro en un endpoint específico."""
        response = requests.put(f"{CRUDAPI.BASE_URL}/{endpoint}/{record_id}", json=data)
        if response.status_code == 200:
            print(f"Registro actualizado exitosamente en {endpoint}.")
            return response.json()
        else:
            print(f"Error al actualizar registro en {endpoint}: {response.status_code}")
            return None

    @staticmethod
    def delete_data(endpoint, record_id):
        """Eliminar un registro de un endpoint específico."""
        response = requests.delete(f"{CRUDAPI.BASE_URL}/{endpoint}/{record_id}")
        if response.status_code == 200:
            print(f"Registro eliminado exitosamente de {endpoint}.")
        else:
            print(f"Error al eliminar registro de {endpoint}: {response.status_code}")
