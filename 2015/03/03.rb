require 'set'

def part1(input)
  x = y = 0
  visited = { [x, y] => 1 }

  input.each_char do |c|
    case c
    when '^' then y += 1
    when 'v' then y -= 1
    when '<' then x -= 1
    when '>' then x += 1
    end

    visited[[x, y]] = 1
  end

  visited.size
end

def part2(input)
    santa_x = santa_y = robot_x = robot_y = 0
    visited = { [santa_x, santa_y] => 1 }

    input.each_char.with_index do |c, i|
        if i % 2 == 0
            case c
            when '^' then santa_y += 1
            when 'v' then santa_y -= 1
            when '<' then santa_x -= 1
            when '>' then santa_x += 1
            end

            visited[[santa_x, santa_y]] = 1
        else
            case c
            when '^' then robot_y += 1
            when 'v' then robot_y -= 1
            when '<' then robot_x -= 1
            when '>' then robot_x += 1
            end

            visited[[robot_x, robot_y]] = 1
        end
    end

    visited.size
end


input = File.read('03.txt')

puts "#{part1(input)}"
puts "#{part2(input)}"