content = File.read("01.txt")

floor = 0
character = 0

content.each_char do |c|
  character += 1
  if c == '('
    floor += 1
  elsif c == ')'
    floor -= 1
  end
  if floor == -1
    puts "Basement at character #{character}"
    break
  end
end