houses = Hash(Array(Int32), Int32).new(0)
pos = [0, 0]

File.read("03.txt").each_char do |c|
    case c
    when '^' then pos[1] += 1
    when 'v' then pos[1] -= 1
    when '>' then pos[0] += 1
    when '<' then pos[0] -= 1
    end

    houses[pos] += 1
end

puts houses.size