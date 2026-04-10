# Spatial Searching (Quadtrees and Octrees)

## Concept Definition
In 2D and 3D geometric spaces, physical searching isn't merely about finding an arbitrary value in a flat array; it’s about mathematically **narrowing down a physical location in a volume**. 

## The Problem vs. The Solution
### The Problem: Global Iteration
Checking for physical collisions, particle proximities, or rendering bounds across a game engine usually requires iterating through every single coordinate entity globally ($O(N)$ scanning), utterly destroying execution speed hardware side.

### The Solution: N-ary Domain Division
By dynamically and recursively slicing the physical volume into specific sub-regions ($2^d$, where $d$ is the number of dimensions), we generate a localized indexing tree.
- **2D (The Quadtree / $n=4$):** Treats geometric space like a square grid. Nodes are sliced 4 times into North-West, North-East, South-West, and South-East limits.
- **3D (The Octree / $n=8$):** Slices voxel cube limits simultaneously across the $XY$, $YZ$, and $XZ$ coordinate planes into 8 specific octants.

This allows the hardware to evaluate large coordinate subsets rapidly and instantly discard 3/4 (or 7/8) of the volume per check cycle! The "search" fundamentally becomes a highly compact **bit-masking** operation on space relative to a geometric center point line.

## Example Code (Pseudo-code)

```python
class OctreeNode:
    def __init__(self, boundary, capacity):
        self.boundary = boundary  # A Cube object with (x, y, z, size)
        self.capacity = capacity  # Max vectors before splitting
        self.points = []
        self.divided = False
        self.children = [] # Will hold 8 initialized OctreeNodes

    def subdivide(self):
        # Hardware logic: Execute generation of 8 localized Cube boundaries
        self.divided = True

    def insert(self, point):
        # 1. Coordinate check: Is the physics point inside this cube target?
        if not self.boundary.contains(point):
            return False

        # 2. Add locally if there is structural space remaining
        if len(self.points) < self.capacity:
            self.points.append(point)
            return True
        
        # 3. Otherwise, shatter the grid boundary and abstract downwards 
        if not self.divided:
            self.subdivide()
            
        # Recursive branching operation (The exact "Search" mechanism)
        for child in self.children:
            if child.insert(point):
                return True
```

## Complexity Analysis

**Time Complexity:**
- **2D Quadtree Lookup:** $O(\log_{4} N)$.
- **3D Octree Lookup:** $O(\log_{8} N)$. 
- Branching factor complexity ensures physical spatial checks perform exceptionally fast regardless of the total geometric mass density scale.

**Space Complexity:**
- **Tree Overhead:** $O(N \log_{n} N)$ limits. While lookup speeds surge to exponential peaks, tracking coordinate branches scales up the structural metadata size significantly inside memory arrays.
