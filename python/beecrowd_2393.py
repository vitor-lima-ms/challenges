while True:
    try:
        N = int(input())


        coordinates = list()

        for _ in range(N):
            xi, xf, yi, yf = input().split()
            coordinate = [int(xi), int(xf), int(yi), int(yf)]
            coordinates.append(coordinate)
        
        areas = list()
        intersection = list()
        for point in coordinates:
            point_area = (point[1] - point[0]) * (point[3] - point[2])
            areas.append(point_area)
            
            for other_point in coordinates:
                if point == other_point:
                    continue
                
                if ((other_point[0] < point[1] <= other_point[1]) and (other_point[2] < point[3] <= other_point[3]) and ((point[0] <= other_point[0]) and (point[2] <= other_point[2]))):
                    
                    intersect_area = (point[1] - other_point[0]) * (point[3] - other_point[2])

                    intersection.append(intersect_area)

                    '''If the xf of the point is between the x's of the other point'''
                
                elif ((other_point[0] <= point[1] <= other_point[1]) and (other_point[0] <= point[0] <= other_point[1]) and (other_point[2] <= point[3] <= other_point[3]) and other_point[2] <= point[2] <= other_point[3]):
                    point_area = (point[1] - point[0]) * (point[3] - point[2])

                    intersection.append(intersect_area)

                    '''If the xi and xf of the point are between the x's of the other point'''
                
            coordinates.remove(point)    
        
        last_point_area = (coordinates[0][1] - coordinates[0][0]) * (coordinates[0][3] - coordinates[0][2])
        total_individual_area = sum(areas) + last_point_area
        total_intersection_area = sum(intersection)
        total = total_individual_area - total_intersection_area

        print(total)

    except EOFError:
        break