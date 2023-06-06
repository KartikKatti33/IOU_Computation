#include <iostream>
#include <algorithm>

float calculate_iou(const std::vector<float>& box1, const std::vector<float>& box2) {
    // Get the coordinates of the intersection rectangle
    float x1 = std::max(box1[0], box2[0]);
    float y1 = std::max(box1[1], box2[1]);
    float x2 = std::min(box1[2], box2[2]);
    float y2 = std::min(box1[3], box2[3]);

    // Calculate the area of intersection rectangle
    float intersection_area = std::max(0.0f, x2 - x1 + 1) * std::max(0.0f, y2 - y1 + 1);

    // Calculate the area of both bounding boxes
    float box1_area = (box1[2] - box1[0] + 1) * (box1[3] - box1[1] + 1);
    float box2_area = (box2[2] - box2[0] + 1) * (box2[3] - box2[1] + 1);

    // Calculate the Union area by subtracting the intersection area
    float union_area = box1_area + box2_area - intersection_area;

    // Calculate the Intersection over Union
    float iou = intersection_area / union_area;

    return iou;
}

int main() {
    std::vector<float> box1 = {10, 10, 100, 100};
    std::vector<float> box2 = {50, 50, 150, 150};

    float iou = calculate_iou(box1, box2);
    std::cout << "IoU: " << iou << std::endl;

    return 0;
}
