from .coco import CocoDataset
from .registry import DATASETS

@DATASETS.register_module
class SignsDataset(CocoDataset):

    CLASSES = ('2.4', '3.24', '2.1', '4.1', '4.2', '5.20', 
               '5.19', '8.22', 'OTH', '3.1', '3.27')