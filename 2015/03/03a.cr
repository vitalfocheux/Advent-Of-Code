content = File.read("03.txt")

houses = { [0, 0] => 1 }
pos = [0, 0]

content.each_char do |c|
    case c
    when '^'
        pos[1] += 1
    when 'v'
        pos[1] -= 1
    when '>'
        pos[0] += 1
    when '<'
        pos[0] -= 1
    end
    if houses.has_key?(pos)
        houses[pos] += 1
    else
        houses[pos] = 1
    end
end

puts houses.size