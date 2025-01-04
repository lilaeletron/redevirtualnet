import os

class ImageCarousel:
    def __init__(self, directory):
        """
        Inicializa a classe com o diretório onde as imagens estão localizadas.
        """
        self.directory = directory
        self.images = self._list_images()

    def _list_images(self):
        """
        Lista os arquivos de imagem válidos no diretório.
        """
        valid_extensions = ['.png', '.jpg', '.jpeg', '.webp']
        return [
            file for file in os.listdir(self.directory)
            if os.path.splitext(file)[1].lower() in valid_extensions
        ]

    def get_images(self):
        """
        Retorna a lista de nomes de arquivos de imagem.
        """
        return self.images


if __name__ == '__main__':
    carousel = ImageCarousel('.\core\static\img')
    for img in carousel.get_images():
        print(img)