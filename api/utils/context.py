from strawberry.fastapi import BaseContext
from api.dataloaders import get_all_dataloaders


class Context(BaseContext):

    def __init__(self):
        super(BaseContext, self).__init__()
        self.dataloaders = get_all_dataloaders()
