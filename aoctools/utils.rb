require 'digest'

def md5(data)
    # Return the md5 hash of the input data
    return Digest::MD5.hexdigest(data)
end

def sha256(data)
    # Return the sha256 hash of the input data
    return Digest::SHA256.hexdigest(data)
end

def min_max(data)
    # Return the min and max values of the input data
    return data.min, data.max
end

def manhattan_distance(p1, p2)
    # Return the Manhattan distance between two points
    return (p1[0] - p2[0]).abs + (p1[1] - p2[1]).abs
end

def shoelace(points)
    # Return the area of a polygon defined by the input points
    n = points.length
    return 0.5 * (points.each_cons(2).map { |(x1, y1), (x2, y2)| x1 * y2 - x2 * y1 }.sum).abs
end