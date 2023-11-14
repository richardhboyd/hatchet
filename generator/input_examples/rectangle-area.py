def rectangle_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
  # Calculate area of first rectangle
  width1 = ax2 - ax1
  height1 = ay2 - ay1
  area1 = width1 * height1
  
  # Calculate area of second rectangle  
  width2 = bx2 - bx1
  height2 = by2 - by1
  area2 = width2 * height2

  # Find overlap area
  overlap_width = max(0, min(ax2, bx2) - max(ax1, bx1))
  overlap_height = max(0, min(ay2, by2) - max(ay1, by1))
  overlap_area = overlap_width * overlap_height
  
  # Total area is sum of two areas minus overlap area
  return area1 + area2 - overlap_area
