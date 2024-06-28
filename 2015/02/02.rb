def wrapping_paper(input)
    input.split("\n").map do |line|
        l, w, h = line.split('x').map(&:to_i)
        sides = [l*w, w*h, h*l]
        2 * sides.sum + sides.min
    end.sum
end

def ribbon(input)
    input.split("\n").map do |line|
        l, w, h = line.split('x').map(&:to_i)
        wrap = 2 * [l, w, h].combination(2).map { |a, b| a + b }.min
        bow = l * w * h
        wrap + bow
    end.sum
end        

input = File.read('02.txt')

puts "#{wrapping_paper(input)}"
puts "#{ribbon(input)}"