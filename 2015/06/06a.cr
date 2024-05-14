content = File.read("06.txt")

matrix = Array.new(1000) { Array(Bool).new(1000, false) }

content.each_line do |line|
    if line =~ /(\d+),(\d+) through (\d+),(\d+)/
        x1, y1, x2, y2 = $1.to_i, $2.to_i, $3.to_i, $4.to_i
        action = case line
                 when /turn on/
                     ->(x : Int32, y : Int32) { matrix[x][y] = true }
                 when /turn off/
                     ->(x : Int32, y : Int32) { matrix[x][y] = false }
                 when /toggle/
                     ->(x : Int32, y : Int32) { matrix[x][y] = !matrix[x][y] }
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

puts matrix.flatten.count(true)