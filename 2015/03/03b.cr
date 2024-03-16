content = File.read("03.txt")

houses = [[0, 0]]
santa_pos = [0, 0]
robo_pos = [0, 0]

content.each_char.each_with_index do |c, i|
    pos = i.even? ? santa_pos : robo_pos

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

    houses << pos.dup unless houses.includes?(pos)
end

puts houses.size