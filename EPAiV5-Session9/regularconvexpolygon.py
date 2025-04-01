import math


class RegConvexPolygon:
    '''
    Regular Convex Polygon class. A polygon is called "Regular Convex Polygon" if and only if:
        a. Equal Side Lengths: All the sides of the polygon are of equal length.
        b. Equal Angles: All the interior angles are equal.
        c. Convexity: The polygon is convex, meaning all its interior angles are less than 180 degrees, 
           and no part of the polygon "caves in."
    '''
    def __init__(self, edges: int, circum_radius: float) -> None:
        '''
        Initialize the convex polygon with its number of edges and circumradius.
        '''
        if not isinstance (edges, int):
            raise TypeError ('Polygons will have edges of type int')
        
        if not (isinstance(edges, float) or isinstance(edges, int)):
            raise TypeError ('Polygon circumradius must be either int or float')

        if circum_radius <= 0:
            raise ValueError ('Polygon\'s circum radius must a valid positive real number')
        
        if edges < 3:
            raise ValueError ('Polygon should have atleast 3 sides')

        self.no_edges = edges
        self.circum_radius = circum_radius

        # Calculate number of vertices, which is equal to number of edges
        self.calculate_parameters()


    def calculate_parameters(self):
        '''
        Calculates area and perimeter of the regular polygon. To calculate those, 
        we also need to calculate edge length (equal for all polygons) and apothem
        '''
        self.vertices = self.no_edges
        self.interior_angle = (self.no_edges - 2) * (180 / self.no_edges)
        self.edge_len = 2 * self.circum_radius * math.sin(math.radians(180 / self.no_edges))
        self.apothem = self.circum_radius * math.cos(math.radians(180 / self.no_edges))
        self.area = 0.5 * self.no_edges * self.edge_len * self.apothem
        self.perimeter = self.no_edges * self.edge_len

    def __repr__(self) -> str:
        '''
        String representation of the object.
        '''
        return (f'RegConvexPolygon(edges={self.no_edges}, circum_radius={self.circum_radius}, '
                f'interior_angle={self.interior_angle:.2f}, edge_len={self.edge_len:.2f}, '
                f'apothem={self.apothem:.2f}, area={self.area:.2f}, perimeter={self.perimeter:.2f})')

    def __eq__(self, other) -> bool:
        ''' 
        Checks if two RegConvexPolygon objects are equal.
        '''
        if not isinstance(other, RegConvexPolygon):
            raise TypeError(f'Argument must be an instance of RegConvexPolygon, not {type(other).__name__}')
        return (self.no_edges == other.no_edges) and (self.circum_radius == other.circum_radius)

    def __gt__(self, other) -> bool:
        ''' 
        Checks if the current RegConvexPolygon object is greater than another RegConvexPolygon object.
        '''
        if not isinstance(other, RegConvexPolygon):
            raise TypeError(f'Argument must be an instance of RegConvexPolygon, not {type(other).__name__}')
        return self.vertices > other.vertices