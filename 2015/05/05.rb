def nice_string(input)
    num = 0
    input.split("\n").map do |line|
        if line.scan(/[aeiou]/i).count >= 3 && line.match(/(.)\1/) && !line.match(/ab|cd|pq|xy/)
            num += 1
        end
    end
    num
end

def nice_string_2(input)
    num = 0
    input.split("\n").map do |line|
        if line.match(/(..).*\1/) && line.match(/(.).\1/)
            num += 1
        end
    end
    num
end


input = File.read("05.txt")

puts "#{nice_string(input)}"
puts "#{nice_string_2(input)}"