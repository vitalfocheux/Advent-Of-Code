content = File.read("03.txt")

houses = [[0, 0]]

santa_pos = [0, 0]
robo_pos = [0, 0]

content.each_char.each_with_index do |c, i|
  if i % 2 == 0
    case c
    when '^'
        santa_pos[1] += 1
    when 'v'
        santa_pos[1] -= 1
    when '>'
        santa_pos[0] += 1
    when '<'
        santa_pos[0] -= 1
    end
    unless houses.includes?(santa_pos)
       houses << santa_pos.dup
    end
  else
    case c
    when '^'
        robo_pos[1] += 1
    when 'v'
        robo_pos[1] -= 1
    when '>'
        robo_pos[0] += 1
    when '<'
        robo_pos[0] -= 1
    end
    unless houses.includes?(robo_pos)
       houses << robo_pos.dup
    end
  end
  
end

puts houses.size