from ultralytics import YOLO
from PIL import Image, ImageFilter

# Define a color map for the classes
#class_colors = {
 #   0: "red",
  #  1: "green",
   # 2: "blue",
    #3: "yellow",
    #4: "purple"
#}
model_2= YOLO("table_img_debris.pt")
def blur_boxes(image, predictions, blur_class_0):
    """
    Blur the regions inside the bounding boxes on the image based on the predictions.
    """
    for pred in predictions:
        x1, y1, x2, y2, conf, cls = pred
        
        if cls == 0 and not blur_class_0:
            continue
        
        # Convert tensor coordinates to integers
        x1, y1, x2, y2 = int(x1.item()), int(y1.item()), int(x2.item()), int(y2.item())
        
        # Crop the bounding box region from the image
        region = image.crop((x1, y1, x2, y2))
        
        # Apply a blur filter to the region
        blurred_region = region.filter(ImageFilter.GaussianBlur(10))
        
        # Paste the blurred region back onto the image
        image.paste(blurred_region, (x1, y1, x2, y2))
    
    return image

def blur_objects_in_image(img, blur_class_0):
    # Load the YOLOv8 model
    

    # Run the YOLO model on the image
    results = model_2(img)

    # Extract predictions from results
    predictions = []
    for r in results:
        for box in r.boxes.xyxy:
            x1, y1, x2, y2 = box
            conf = r.boxes.conf[0]
            cls = r.boxes.cls[0]
            predictions.append((x1, y1, x2, y2, conf, cls))

    # Blur the regions inside the bounding boxes
    img_with_blur = blur_boxes(img, predictions, blur_class_0)

    return img_with_blur

