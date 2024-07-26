from ultralytics import YOLO
from PIL import Image, ImageFilter

model_1 = YOLO("header_footer.pt")
def blur_boxes(image, predictions):
    """
    Blur the regions inside the bounding boxes on the image based on the predictions.
    """
    for pred in predictions:
        x1, y1, x2, y2, conf, cls = pred
        # Convert tensor coordinates to integers
        x1, y1, x2, y2 = int(x1.item()), int(y1.item()), int(x2.item()), int(y2.item())
        
        box = (x1, y1, x2, y2)
        
        # Crop the bounding box region from the image
        region = image.crop(box)
        
        # Apply a blur filter to the region
        blurred_region = region.filter(ImageFilter.GaussianBlur(10))
        
        # Paste the blurred region back onto the image
        image.paste(blurred_region, box)
    
    return image

def blur_image_with_yolo(img):
    # Load the YOLOv5 model
    

    # Open the image


    # Run the YOLO model on the image
    results = model_1(img)

    predictions = []
    for r in results:
         for box in r.boxes.xyxy:
                x1, y1, x2, y2 = box
                conf = r.boxes.conf[0]
                cls = r.boxes.cls[0]
                predictions.append((x1, y1, x2, y2, conf, cls))



    # Blur the regions inside the bounding boxes
    img_with_blur = blur_boxes(img, predictions)

    return img_with_blur


