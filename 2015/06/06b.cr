content = File.read("06.txt")

matrix = Array.new(1000) { Array(Int32).new(1000, 0) }

content.each_line do |line|
    if line =~ /(\d+),(\d+) through (\d+),(\d+)/
        x1, y1, x2, y2 = $1.to_i, $2.to_i, $3.to_i, $4.to_i
        action = case line
                 when /turn on/
                     ->(x : Int32, y : Int32) { matrix[x][y] += 1 }
                 when /turn off/
                     ->(x : Int32, y : Int32) { matrix[x][y] -= 1 if matrix[x][y] > 0}
                 when /toggle/
                     ->(x : Int32, y : Int32) { matrix[x][y] += 2}
                 else
                    raise "Unknown action"
                 end
        (x1..x2).each do |x|
            (y1..y2).each do |y|
                action.call(x, y)
            end
        end
    end
end

puts matrix.flatten.sum