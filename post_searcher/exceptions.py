class DataSourceBrokenExceptions(Exception):
    """Класс для вывода ошибки, когда файл с данными поврежден """
    pass


class PictureNotUploadError(Exception):
    """Класс для вывода ошибки, когда не удалось загрузить файл"""
    pass
