# Ouvre le fichier en mode lecture
content = File.read("01.txt")

floor = 0

content.each_char do |c|
  if c == '('
    floor += 1
  elsif c == ')'
    floor -= 1
  end
end

puts floor