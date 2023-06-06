

def calculate_iou(box1, box2):
    """
    Calculate Intersection over Union (IoU) of two bounding boxes.
    
    Args:
        box1: List of 4 values representing [x1, y1, x2, y2] of the first box.
        box2: List of 4 values representing [x1, y1, x2, y2] of the second box.
    
    Returns:
        IoU: Intersection over Union value.
    """
    # Get the coordinates of the intersection rectangle
    x1 = max(box1[0], box2[0])
    y1 = max(box1[1], box2[1])
    x2 = min(box1[2], box2[2])
    y2 = min(box1[3], box2[3])

    # Calculate the area of intersection rectangle
    intersection_area = max(0, x2 - x1 + 1) * max(0, y2 - y1 + 1)

    # Calculate the area of both bounding boxes
    box1_area = (box1[2] - box1[0] + 1) * (box1[3] - box1[1] + 1)
    box2_area = (box2[2] - box2[0] + 1) * (box2[3] - box2[1] + 1)

    # Calculate the Union area by subtracting the intersection area
    union_area = box1_area + box2_area - intersection_area

    # Calculate the Intersection over Union
    iou = intersection_area / union_area

    return iou

if __name__=="__main__":
    box1 = [10, 10, 100, 100]
    box2 = [50, 50, 150, 150]
    iou = calculate_iou(box1, box2)
    print("IoU:", iou)
