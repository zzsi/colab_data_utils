`colab_data_utils` is a library for data visualization and labeling in colab. This is adapted from [tensorflow's models repo](https://github.com/tensorflow/models/blob/master/research/object_detection/utils/colab_utils.py).

Example usage:

```
import colab_data_utils as cdu

# Label bounding boxes.
gt_boxes = []
cdu.annotate(train_images_np, box_storage_pointer=gt_boxes)
```

