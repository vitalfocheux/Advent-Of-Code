content = File.read("02.txt")

wrapping_paper = 0

content.each_line do |line|
    l, w, h = line.split("x")
    l, w, h = l.to_i, w.to_i, h.to_i

    wrapping_paper += 2*l*w + 2*w*h + 2*h*l + [l*w, w*h, h*l].min
end

puts wrapping_paper