from ultralytics.data.annotator import auto_annotate

auto_annotate(data=r"F:\dataset\autodataset\dataset", det_model="yolov8x.pt",device='cuda',output_dir=r'F:\dataset\autodataset\label')