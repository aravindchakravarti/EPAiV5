from regularconvexpolygon import RegConvexPolygon

class PolygonSequence(RegConvexPolygon):
    def __init__(self, circum_radius: float, largest_polygon: int) -> None:
        ''' 
        Initializes the class PolygonSequence to calculate area to perimeters ratio 
        of sequence of numbers starting from 3 to "largest_polygon"
        '''
        if not isinstance(largest_polygon, int):
            raise TypeError('Expected largest polygon as type int')
        
        if circum_radius <=0 :
            raise ValueError('Circum Radius must a valid positive number')
        
        if largest_polygon < 3:
            raise ValueError('Polygons are defined only with 3 or more edges')
        
        self.circum_radius = circum_radius
        self.largest_polygon = largest_polygon
        self.polygon_data = []

        # Calculate sequence of polygons
        self.calculate_sequences()

    def calculate_sequences(self):
        '''
        Caluclates the area to perimeter ratio for all polygons from 3 to largest polygon 
        provided by user
        '''
        for edge_count in range(0, self.largest_polygon + 1):
            if (edge_count < 3):
                self.polygon_data.append(0)
            else:
                # Create a RegConvexPolygon instance for each edge count
                polygon = RegConvexPolygon(edge_count, self.circum_radius)
                # Append to the list of polygon data
                # data_dict = {'edge' : edge_count, 'area' : polygon.area, 'perimeter' : polygon.perimeter, 'a_to_p_ratio' : (polygon.area/polygon.perimeter)}
                # self.polygon_data.append(data_dict)
                self.polygon_data.append(polygon.area/polygon.perimeter)

    def largest_area_to_perimeter_ratio(self):
        '''
        Returns a tuple containing, 
        max value of area to perimeter ratio and index at which it has occured
        Note: index will be the polygon number at which max area to perimeter ratio has occured rather 
        than index of the array
        '''
        polygon_reprs = ', '.join(repr(p) for p in self.polygon_data)
        print(max(self.polygon_data), self.polygon_data.index(max(self.polygon_data)))

    def __repr__(self) -> str:
        '''
        String representation of the PolygonSequence object, including details of all polygons in the sequence.
        '''
        polygon_reprs = ', '.join(repr(p) for p in self.polygon_data)
        return (f'PolygonSequence(largest_polygon={self.largest_polygon}, '
                f'polygon with area to perimeter ratio from 3 to {self.largest_polygon}=[{polygon_reprs}])')

    def __len__(self) -> int:
        ''' 
        Returns the length of the Calculated Sequences stored in memory
        '''
        return(len(self.polygon_data))
    
    def __getitem__(self, index:int) -> int:
        '''
        returns the area to perimeter ratio stored at a index 
        '''
        return(self.polygon_data[index])