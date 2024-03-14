content = File.read("05.txt")

def nice_string(string)
  return false if string.match(/ab|cd|pq|xy/)
  return false unless string.match(/[aeiou].*[aeiou].*[aeiou]/) 
  return false unless string.match(/(.)\1/)
  true
end

nb = 0

content.each_line do |line|
  nb += 1 if nice_string(line)
end

puts nb